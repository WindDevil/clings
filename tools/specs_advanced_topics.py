"""Advanced C and systems-programming exercises."""

from spec import ex

SPECS = [
    ex(
        topic="15_ub_safety",
        slug="11_implementation_defined",
        title="Implementation-defined behavior",
        objective="Observe implementation-defined char signedness and packing pragmas.",
        reference="",
        hint="CHAR_MIN tells you whether plain char is signed; #pragma pack changes padding.",
        code=r"""
#include <limits.h>
#include <stddef.h>

int char_is_signed(void)
{
    return CHAR_MIN < 0;
}

int int_width_at_least_16(void)
{
    return (int)(sizeof(int) * CHAR_BIT) >= 16;
}

int packed_size(void)
{
#pragma pack(push, 1)
    struct packed {
        char first;
        int second;
    };
#pragma pack(pop)
    return (int)sizeof(struct packed);
}
""",
        tests=r"""
CLINGS_CHECK_INT(char_is_signed() == 0 || char_is_signed() == 1, 1);
CLINGS_CHECK_INT(int_width_at_least_16(), 1);
CLINGS_CHECK_INT(packed_size(), (int)(sizeof(char) + sizeof(int)));
""",
        breaks=[
            (
                "#pragma pack(push, 1)",
                "/* TODO: pack the struct without padding. */\n#pragma pack(push, 4)",
            )
        ],
    ),
    ex(
        topic="03_types_variables",
        slug="12_integer_promotions",
        title="Integer promotions",
        objective="See that char operands are promoted to int in arithmetic expressions.",
        reference="",
        hint="sizeof(left + right) is sizeof(int) for char operands.",
        code=r"""
#include <stddef.h>

int char_addition_is_int(void)
{
    char left = 1;
    char right = 2;
    return sizeof(left + right) == sizeof(int);
}

int unsigned_char_promotion(void)
{
    unsigned char value = 255;
    return (int)value + 1;
}
""",
        tests=r"""
CLINGS_CHECK_INT(char_addition_is_int(), 1);
CLINGS_CHECK_INT(unsigned_char_promotion(), 256);
""",
        breaks=[
            (
                "return sizeof(left + right) == sizeof(int);",
                "/* TODO: the sum is promoted to int. */\n    return sizeof(left + right) == sizeof(char);",
            )
        ],
    ),
    ex(
        topic="12_standard_library",
        slug="16_default_argument_promotions",
        title="Default argument promotions",
        objective="Use the promoted types expected by variadic functions.",
        reference="",
        hint="char and short promote to int; float promotes to double.",
        code=r"""
#include <stdarg.h>

int sum_promoted(int count, ...)
{
    va_list arguments;
    va_start(arguments, count);
    int sum = 0;
    for (int i = 0; i < count; ++i) {
        sum += va_arg(arguments, int);
    }
    va_end(arguments);
    return sum;
}

double sum_double_promoted(int count, ...)
{
    va_list arguments;
    va_start(arguments, count);
    double sum = 0.0;
    for (int i = 0; i < count; ++i) {
        sum += va_arg(arguments, double);
    }
    va_end(arguments);
    return sum;
}
""",
        tests=r"""
CLINGS_CHECK_INT(sum_promoted(3, (char)1, (short)2, 3), 6);
CLINGS_CHECK_INT(sum_double_promoted(2, 1.5f, 2.5f) == 4.0, 1);
""",
        breaks=[
            (
                "sum += va_arg(arguments, int);",
                "/* TODO: read the promoted int argument. */\n        sum += 1;",
            )
        ],
    ),
    ex(
        topic="10_aggregates",
        slug="13_declaration_grammar",
        title="Declaration grammar and function-pointer tables",
        objective="Read a typedef for an array of function pointers.",
        reference="",
        hint="operation_table is typedef int (*[3])(int, int).",
        code=r"""
typedef int (*binary_operation)(int, int);
typedef binary_operation operation_table[3];

static int add(int left, int right)
{
    return left + right;
}

static int subtract(int left, int right)
{
    return left - right;
}

static int multiply(int left, int right)
{
    return left * right;
}

int apply_table(operation_table table, int index, int left, int right)
{
    return table[index](left, right);
}

int declaration_demo(void)
{
    operation_table table = {add, subtract, multiply};
    return apply_table(table, 1, 10, 3);
}
""",
        tests=r"""
operation_table table = {add, subtract, multiply};

CLINGS_CHECK_INT(apply_table(table, 0, 2, 3), 5);
CLINGS_CHECK_INT(apply_table(table, 1, 10, 3), 7);
CLINGS_CHECK_INT(apply_table(table, 2, 10, 3), 30);
CLINGS_CHECK_INT(declaration_demo(), 7);
""",
        breaks=[
            (
                "return table[index](left, right);",
                "/* TODO: call the selected table entry. */\n    return table[0](left, right);",
            )
        ],
    ),
    ex(
        topic="07_pointers",
        slug="11_restrict_aliasing",
        title="restrict and aliasing contracts",
        objective="Use restrict to promise that two pointer parameters do not alias.",
        reference="",
        hint="restrict tells the compiler that destination and source do not overlap.",
        code=r"""
#include <stddef.h>

void add_restrict(int *restrict destination, const int *restrict source,
                  size_t count)
{
    for (size_t i = 0; i < count; ++i) {
        destination[i] += source[i];
    }
}

int restrict_demo(void)
{
    int values[4] = {1, 2, 3, 4};
    int source[4] = {10, 20, 30, 40};
    add_restrict(values, source, 4);
    return values[0] + values[3];
}
""",
        tests=r"""
CLINGS_CHECK_INT(restrict_demo(), 55);
""",
        breaks=[
            (
                "destination[i] += source[i];",
                "/* TODO: use the matching source element. */\n        destination[i] += source[0];",
            )
        ],
    ),
    ex(
        topic="09_dynamic_memory",
        slug="09_arena_allocator",
        title="Arena allocator",
        objective="Implement a simple bump allocator with aligned allocations.",
        reference="",
        hint="Align each request to 8 bytes before bumping the used offset.",
        code=r"""
#include <stddef.h>

struct arena {
    unsigned char *memory;
    size_t capacity;
    size_t used;
};

void arena_init(struct arena *arena, void *memory, size_t capacity)
{
    arena->memory = memory;
    arena->capacity = capacity;
    arena->used = 0;
}

void *arena_alloc(struct arena *arena, size_t size)
{
    size_t aligned = (size + 7u) & ~(size_t)7u;
    if (arena->used + aligned > arena->capacity) {
        return NULL;
    }
    void *result = arena->memory + arena->used;
    arena->used += aligned;
    return result;
}

size_t arena_used(const struct arena *arena)
{
    return arena->used;
}
""",
        tests=r"""
unsigned char storage[64];
struct arena arena;

arena_init(&arena, storage, sizeof storage);
void *first = arena_alloc(&arena, 1);
void *second = arena_alloc(&arena, 8);
CLINGS_CHECK(first != NULL);
CLINGS_CHECK(second != NULL);
CLINGS_CHECK((unsigned char *)second - (unsigned char *)first == 8);
CLINGS_CHECK_INT(arena_used(&arena), 16);
CLINGS_CHECK(arena_alloc(&arena, 100) == NULL);
""",
        breaks=[
            (
                "size_t aligned = (size + 7u) & ~(size_t)7u;",
                "/* TODO: align the allocation size. */\n    size_t aligned = size;",
            )
        ],
    ),
    ex(
        topic="09_dynamic_memory",
        slug="10_allocation_stats",
        title="Allocation statistics",
        objective="Track outstanding allocations with wrapped malloc and free.",
        reference="",
        hint="Increment the free counter when a non-NULL pointer is freed.",
        code=r"""
#include <stddef.h>
#include <stdlib.h>

static size_t allocations = 0;
static size_t frees = 0;

void *tracked_malloc(size_t size)
{
    void *pointer = malloc(size);
    if (pointer != NULL) {
        ++allocations;
    }
    return pointer;
}

void tracked_free(void *pointer)
{
    if (pointer != NULL) {
        ++frees;
    }
    free(pointer);
}

size_t outstanding_allocations(void)
{
    return allocations - frees;
}
""",
        tests=r"""
void *first = tracked_malloc(1);
void *second = tracked_malloc(2);

CLINGS_CHECK_INT(outstanding_allocations(), 2);
tracked_free(first);
CLINGS_CHECK_INT(outstanding_allocations(), 1);
tracked_free(second);
CLINGS_CHECK_INT(outstanding_allocations(), 0);
""",
        breaks=[
            (
                "++frees;",
                "/* TODO: count the free. */",
            )
        ],
    ),
    ex(
        topic="17_translation_units",
        slug="05_dynamic_linking",
        title="Dynamic linking with dlopen",
        objective="Load a symbol from a shared library at runtime.",
        reference="",
        hint="Use dlopen, dlsym, and dlclose; convert the object pointer through a union.",
        code=r"""
#include <dlfcn.h>
#include <stddef.h>

typedef size_t (*strlen_function)(const char *);

int dynamic_strlen(void)
{
    void *handle = dlopen("libc.so.6", RTLD_LAZY);
    if (handle == NULL) {
        return -1;
    }

    union {
        void *object;
        strlen_function function;
    } converter;
    converter.object = dlsym(handle, "strlen");
    if (converter.function == NULL) {
        dlclose(handle);
        return -1;
    }

    int result = (int)converter.function("hello");
    dlclose(handle);
    return result;
}
""",
        tests=r"""
CLINGS_CHECK_INT(dynamic_strlen(), 5);
""",
        breaks=[
            (
                'converter.object = dlsym(handle, "strlen");',
                '/* TODO: look up the strlen symbol. */\n    converter.object = dlsym(handle, "strlen_missing");',
            )
        ],
    ),
    ex(
        topic="11_data_representation",
        slug="05_endianness",
        title="Endianness",
        objective="Detect byte order and inspect an integer's first byte.",
        reference="",
        hint="A uint16_t value of 1 stores 0x01 first on little-endian systems.",
        code=r"""
#include <stdint.h>
#include <string.h>

int is_little_endian(void)
{
    uint16_t value = 1;
    unsigned char bytes[2];
    memcpy(bytes, &value, sizeof bytes);
    return bytes[0] == 1;
}

int first_byte_of_0x01020304(void)
{
    uint32_t value = 0x01020304u;
    unsigned char bytes[4];
    memcpy(bytes, &value, sizeof bytes);
    return bytes[0];
}
""",
        tests=r"""
if (is_little_endian()) {
    CLINGS_CHECK_INT(first_byte_of_0x01020304(), 4);
} else {
    CLINGS_CHECK_INT(first_byte_of_0x01020304(), 1);
}
""",
        breaks=[
            (
                "return bytes[0] == 1;",
                "/* TODO: compare the low byte of value 1. */\n    return bytes[0] == 0;",
            )
        ],
    ),
    ex(
        topic="18_advanced_c",
        slug="12_stack_frame",
        title="Stack frames",
        objective="Observe that nested function calls use distinct activation records.",
        reference="",
        hint="__builtin_frame_address is a GCC/Clang extension.",
        code=r"""
#include <stddef.h>

static void *inner_frame(void)
{
    return __builtin_frame_address(0);
}

void *outer_frame_difference(void)
{
    void *inner = inner_frame();
    return __builtin_frame_address(0) == inner ? NULL : inner;
}
""",
        tests=r"""
CLINGS_CHECK(outer_frame_difference() != NULL);
""",
        breaks=[
            (
                "return __builtin_frame_address(0) == inner ? NULL : inner;",
                "/* TODO: return a distinct inner frame. */\n    return NULL;",
            )
        ],
    ),
]
