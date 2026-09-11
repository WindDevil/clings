"""Exercise specifications for topics 05 through 08."""

from spec import ex

SPECS = [
    # ------------------------------------------------------------------
    # 05_arrays_strings
    # ------------------------------------------------------------------
    ex(
        topic="08_arrays_strings",
        slug="01_array_basics",
        title="Array traversal",
        objective="Iterate over an array and compute a sum and maximum.",
        reference="",
        hint="Use values[i] inside the loop, not values[0].",
        code=r"""
int array_sum(const int *values, int count)
{
    int sum = 0;
    for (int i = 0; i < count; ++i) {
        sum += values[i];
    }
    return sum;
}

int array_max(const int *values, int count)
{
    int maximum = values[0];
    for (int i = 1; i < count; ++i) {
        if (values[i] > maximum) {
            maximum = values[i];
        }
    }
    return maximum;
}
""",
        tests=r"""
const int values[] = {3, -1, 7, 2};

CLINGS_CHECK_INT(array_sum(values, 4), 11);
CLINGS_CHECK_INT(array_max(values, 4), 7);
""",
        breaks=[
            (
                "sum += values[i];",
                "/* TODO: add the current element. */\n        sum += values[0];",
            )
        ],
    ),
    ex(
        topic="08_arrays_strings",
        slug="02_array_decay",
        title="Array-to-pointer decay",
        objective="See how an array parameter becomes a pointer.",
        reference="",
        hint="Inside a function, an array parameter has pointer type.",
        code=r"""
int local_array_length(void)
{
    int values[10];
    return (int)(sizeof(values) / sizeof(values[0]));
}

int parameter_is_pointer(const int *values)
{
    return sizeof(values) == sizeof(int *);
}
""",
        tests=r"""
int values[4] = {0};

CLINGS_CHECK_INT(local_array_length(), 10);
CLINGS_CHECK_INT(parameter_is_pointer(values), 1);
""",
        breaks=[
            (
                "return (int)(sizeof(values) / sizeof(values[0]));",
                "/* TODO: use the local array, not a pointer, to compute the length. */\n    return (int)(sizeof(values) / sizeof(int *));",
            )
        ],
    ),
    ex(
        topic="08_arrays_strings",
        slug="03_multidimensional",
        title="Two-dimensional arrays",
        objective="Transpose a 3x3 matrix with nested loops.",
        reference="",
        hint="The transposed element at [row][column] comes from input[column][row].",
        code=r"""
void transpose3x3(const int input[3][3], int output[3][3])
{
    for (int row = 0; row < 3; ++row) {
        for (int column = 0; column < 3; ++column) {
            output[column][row] = input[row][column];
        }
    }
}
""",
        tests=r"""
const int input[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
};
int output[3][3] = {{0}};

transpose3x3(input, output);
CLINGS_CHECK_INT(output[0][0], 1);
CLINGS_CHECK_INT(output[0][1], 4);
CLINGS_CHECK_INT(output[1][0], 2);
CLINGS_CHECK_INT(output[1][2], 8);
""",
        breaks=[
            (
                "output[column][row] = input[row][column];",
                "/* TODO: swap the row and column indices. */\n            output[row][column] = input[row][column];",
            )
        ],
    ),
    ex(
        topic="08_arrays_strings",
        slug="04_string_literals",
        title="String literals and mutable strings",
        objective="Scan a const string and modify a mutable char array.",
        reference="",
        hint="A string literal must not be modified; a char array may be modified.",
        code=r"""
int count_vowels(const char *text)
{
    int count = 0;
    for (const char *p = text; *p != '\0'; ++p) {
        switch (*p) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            ++count;
            break;
        default:
            break;
        }
    }
    return count;
}

void replace_char(char *text, char from, char to)
{
    for (char *p = text; *p != '\0'; ++p) {
        if (*p == from) {
            *p = to;
        }
    }
}
""",
        tests=r"""
char text[] = "hello";

CLINGS_CHECK_INT(count_vowels("hello"), 2);
replace_char(text, 'l', 'L');
CLINGS_CHECK_STR(text, "heLLo");
""",
        breaks=[
            (
                "*p = to;",
                "/* TODO: replace the character. */",
            )
        ],
    ),
    ex(
        topic="08_arrays_strings",
        slug="05_string_ops",
        title="Implementing string operations",
        objective="Implement strlen, strcmp, and strcpy with pointers.",
        reference="",
        hint="The destination pointer must advance after each copied character.",
        code=r"""
#include <stddef.h>

size_t my_strlen(const char *text)
{
    const char *p = text;
    while (*p != '\0') {
        ++p;
    }
    return (size_t)(p - text);
}

int my_strcmp(const char *left, const char *right)
{
    while (*left != '\0' && *left == *right) {
        ++left;
        ++right;
    }
    return (int)(unsigned char)*left - (int)(unsigned char)*right;
}

char *my_strcpy(char *destination, const char *source)
{
    char *result = destination;
    while ((*destination++ = *source++) != '\0') {
    }
    return result;
}
""",
        tests=r"""
char buffer[16];

CLINGS_CHECK_INT(my_strlen("hello"), 5);
CLINGS_CHECK_INT(my_strlen(""), 0);
CLINGS_CHECK_INT(my_strcmp("abc", "abc"), 0);
CLINGS_CHECK(my_strcmp("abc", "abd") < 0);
CLINGS_CHECK_STR(my_strcpy(buffer, "copy me"), "copy me");
""",
        breaks=[
            (
                "while ((*destination++ = *source++) != '\\0') {\n    }",
                "/* TODO: copy until the terminating NUL. */\n    while ((*destination++ = *source++) == '\\0') {\n    }",
            )
        ],
    ),
    ex(
        topic="08_arrays_strings",
        slug="06_tokenize",
        title="Tokenizing with strtok_r",
        objective="Split a string without modifying the caller's buffer.",
        reference="",
        hint="Pass both space and comma as delimiters.",
        code=r"""
#include <stdlib.h>
#include <string.h>

int count_tokens(const char *text)
{
    char *copy = malloc(strlen(text) + 1);
    if (copy == NULL) {
        return -1;
    }
    strcpy(copy, text);

    int count = 0;
    char *save = NULL;
    for (char *token = strtok_r(copy, " ,", &save); token != NULL;
         token = strtok_r(NULL, " ,", &save)) {
        ++count;
    }

    free(copy);
    return count;
}
""",
        tests=r"""
CLINGS_CHECK_INT(count_tokens("one,two three"), 3);
CLINGS_CHECK_INT(count_tokens("  a , b ,c  "), 3);
CLINGS_CHECK_INT(count_tokens(""), 0);
""",
        breaks=[
            (
                'strtok_r(copy, " ,", &save)',
                '/* TODO: include spaces and commas in the delimiter set. */\n         strtok_r(copy, ",", &save)',
            ),
            (
                'strtok_r(NULL, " ,", &save)',
                'strtok_r(NULL, ",", &save)',
            ),
        ],
    ),

    # ------------------------------------------------------------------
    # 06_pointers
    # ------------------------------------------------------------------
    ex(
        topic="07_pointers",
        slug="01_pointer_basics",
        title="Dereference and address-of",
        objective="Read and write through pointers.",
        reference="",
        hint="Assigning the parameter itself does not modify the caller's variable.",
        code=r"""
int read_through(const int *value)
{
    return *value;
}

void write_through(int *value, int new_value)
{
    *value = new_value;
}
""",
        tests=r"""
int value = 7;

CLINGS_CHECK_INT(read_through(&value), 7);
write_through(&value, 42);
CLINGS_CHECK_INT(value, 42);
""",
        breaks=[
            (
                "*value = new_value;",
                "/* TODO: write through the pointer, not to the local parameter. */\n    value = &new_value;",
            )
        ],
    ),
    ex(
        topic="07_pointers",
        slug="02_null_and_const",
        title="NULL and const correctness",
        objective="Check for NULL and respect pointer-to-const.",
        reference="",
        hint="A pointer-to-const can read but not write the pointed-to object.",
        code=r"""
#include <stddef.h>

int is_null(const void *pointer)
{
    return pointer == NULL;
}

int read_const(const int *value)
{
    return *value;
}

void write_through(int *value, int new_value)
{
    *value = new_value;
}
""",
        tests=r"""
int value = 5;

CLINGS_CHECK_INT(is_null(NULL), 1);
CLINGS_CHECK_INT(is_null(&value), 0);
CLINGS_CHECK_INT(read_const(&value), 5);
write_through(&value, 9);
CLINGS_CHECK_INT(value, 9);
""",
        breaks=[
            (
                "return pointer == NULL;",
                "/* TODO: return true only for a null pointer. */\n    return pointer != NULL;",
            )
        ],
    ),
    ex(
        topic="07_pointers",
        slug="03_pointer_arithmetic",
        title="Pointer arithmetic",
        objective="Walk an array with pointers and return a pointer into it.",
        reference="",
        hint="Advance one element at a time; p < values + count is the end condition.",
        code=r"""
#include <stddef.h>

int sum_pointer(const int *values, int count)
{
    int sum = 0;
    for (const int *p = values; p < values + count; ++p) {
        sum += *p;
    }
    return sum;
}

const int *find_value(const int *values, int count, int needle)
{
    for (const int *p = values; p < values + count; ++p) {
        if (*p == needle) {
            return p;
        }
    }
    return NULL;
}
""",
        tests=r"""
const int values[] = {10, 20, 30, 40};
const int *found = find_value(values, 4, 30);

CLINGS_CHECK_INT(sum_pointer(values, 4), 100);
CLINGS_CHECK(found != NULL);
CLINGS_CHECK_INT((int)(found - values), 2);
CLINGS_CHECK(find_value(values, 4, 99) == NULL);
""",
        breaks=[
            (
                "for (const int *p = values; p < values + count; ++p) {\n        sum += *p;",
                "/* TODO: visit every element. */\n    for (const int *p = values; p < values + count; p += 2) {\n        sum += *p;",
            )
        ],
    ),
    ex(
        topic="07_pointers",
        slug="04_pointer_to_pointer",
        title="Pointers to pointers",
        objective="Let a function allocate and update a caller-owned pointer.",
        reference="",
        hint="Assign through *slot, not to the local slot parameter.",
        code=r"""
#include <stdlib.h>

int allocate_int(int **out, int value)
{
    *out = malloc(sizeof **out);
    if (*out == NULL) {
        return -1;
    }
    **out = value;
    return 0;
}

void set_pointer(int **slot, int *value)
{
    *slot = value;
}
""",
        tests=r"""
int *allocated = NULL;
int value = 5;
int *slot = NULL;

CLINGS_CHECK_INT(allocate_int(&allocated, 99), 0);
CLINGS_CHECK(allocated != NULL);
CLINGS_CHECK_INT(*allocated, 99);
free(allocated);
set_pointer(&slot, &value);
CLINGS_CHECK(slot == &value);
""",
        breaks=[
            (
                "*slot = value;",
                "/* TODO: update the pointer that slot points to. */\n    slot = &value;",
            )
        ],
    ),
    ex(
        topic="07_pointers",
        slug="05_void_pointer",
        title="Generic byte-level swap",
        objective="Use void pointers and unsigned char for type-agnostic code.",
        reference="",
        hint="Copy the byte from a before overwriting it.",
        code=r"""
#include <stddef.h>

void swap_bytes(void *left, void *right, size_t size)
{
    unsigned char *a = left;
    unsigned char *b = right;

    for (size_t i = 0; i < size; ++i) {
        unsigned char temporary = a[i];
        a[i] = b[i];
        b[i] = temporary;
    }
}
""",
        tests=r"""
int a = 0x11223344;
int b = 0x55667788;
double x = 1.5;
double y = 2.5;

swap_bytes(&a, &b, sizeof a);
CLINGS_CHECK_INT(a, 0x55667788);
CLINGS_CHECK_INT(b, 0x11223344);
swap_bytes(&x, &y, sizeof x);
CLINGS_CHECK_INT(x == 2.5, 1);
CLINGS_CHECK_INT(y == 1.5, 1);
""",
        breaks=[
            (
                "b[i] = temporary;",
                "/* TODO: complete the byte swap. */\n        b[i] = a[i];",
            )
        ],
    ),
    ex(
        topic="07_pointers",
        slug="06_dangling_wild",
        title="Dangling pointers and safe free",
        objective="Set a freed pointer to NULL to prevent accidental reuse.",
        reference="",
        hint="After free(*pointer), assign NULL through the pointer-to-pointer.",
        code=r"""
#include <stdlib.h>

void safe_free(int **pointer)
{
    free(*pointer);
    *pointer = NULL;
}

int is_null(const void *pointer)
{
    return pointer == NULL;
}
""",
        tests=r"""
int *value = malloc(sizeof *value);

CLINGS_CHECK(value != NULL);
*value = 42;
safe_free(&value);
CLINGS_CHECK_INT(is_null(value), 1);
""",
        breaks=[
            (
                "*pointer = NULL;",
                "/* TODO: make the caller's pointer null after freeing it. */",
            )
        ],
    ),
    ex(
        topic="07_pointers",
        slug="07_pointer_to_array",
        title="Pointers to arrays and &array",
        objective="Distinguish a pointer to an array from a pointer to its first element.",
        reference="",
        hint="&a + 1 advances by the whole array, not by one element.",
        code=r"""
#include <stddef.h>

int sum_row(const int (*row)[4])
{
    int sum = 0;
    for (int i = 0; i < 4; ++i) {
        sum += (*row)[i];
    }
    return sum;
}

int pointer_to_array_difference(void)
{
    int values[4] = {0};
    return (int)((char *)(&values + 1) - (char *)(&values));
}
""",
        tests=r"""
const int row[4] = {1, 2, 3, 4};

CLINGS_CHECK_INT(sum_row(&row), 10);
CLINGS_CHECK_INT(pointer_to_array_difference(), (int)(sizeof(int) * 4));
""",
        breaks=[
            (
                "return (int)((char *)(&values + 1) - (char *)(&values));",
                "/* TODO: advance by the whole array, not one element. */\n    return (int)((char *)(values + 1) - (char *)values);",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 07_dynamic_memory
    # ------------------------------------------------------------------
    ex(
        topic="09_dynamic_memory",
        slug="01_malloc_free",
        title="Allocate, initialize, and free",
        objective="Use malloc and free for a dynamically sized array.",
        reference="",
        hint="Write fill into every element, not just the first.",
        code=r"""
#include <stdlib.h>

int *make_array(size_t count, int fill)
{
    int *values = malloc(count * sizeof *values);
    if (values == NULL) {
        return NULL;
    }
    for (size_t i = 0; i < count; ++i) {
        values[i] = fill;
    }
    return values;
}

void destroy_array(int *values)
{
    free(values);
}
""",
        tests=r"""
int *values = make_array(4, 7);

CLINGS_CHECK(values != NULL);
CLINGS_CHECK_INT(values[0], 7);
CLINGS_CHECK_INT(values[1], 7);
CLINGS_CHECK_INT(values[3], 7);
destroy_array(values);
""",
        breaks=[
            (
                "values[i] = fill;",
                "/* TODO: initialize the current element. */\n        values[i] = 0;",
            )
        ],
    ),
    ex(
        topic="09_dynamic_memory",
        slug="02_calloc",
        title="Zero-initialized allocation",
        objective="Use calloc when every byte must start as zero.",
        reference="",
        hint="calloc(count, size) returns zeroed memory.",
        code=r"""
#include <stdlib.h>

int *make_zeroed(size_t count)
{
    return calloc(count, sizeof(int));
}
""",
        tests=r"""
int *values = make_zeroed(5);

CLINGS_CHECK(values != NULL);
for (int i = 0; i < 5; ++i) {
    CLINGS_CHECK_INT(values[i], 0);
}
free(values);
""",
        breaks=[
            (
                "return calloc(count, sizeof(int));",
                "/* TODO: return zero-initialized storage. */\n    int *values = malloc(count * sizeof(int));\n    if (values != NULL) {\n        for (size_t i = 0; i < count; ++i) {\n            values[i] = 1;\n        }\n    }\n    return values;",
            )
        ],
    ),
    ex(
        topic="09_dynamic_memory",
        slug="03_realloc",
        title="Growing an allocation",
        objective="Use realloc safely and initialize only the new elements.",
        reference="",
        hint="Start filling at old_count so the existing elements survive.",
        code=r"""
#include <stdlib.h>

int *grow_array(int *values, size_t old_count, size_t new_count, int fill)
{
    int *grown = realloc(values, new_count * sizeof *grown);
    if (grown == NULL) {
        return NULL;
    }
    for (size_t i = old_count; i < new_count; ++i) {
        grown[i] = fill;
    }
    return grown;
}
""",
        tests=r"""
int *values = malloc(2 * sizeof *values);
values[0] = 10;
values[1] = 20;

values = grow_array(values, 2, 5, 9);
CLINGS_CHECK(values != NULL);
CLINGS_CHECK_INT(values[0], 10);
CLINGS_CHECK_INT(values[1], 20);
CLINGS_CHECK_INT(values[2], 9);
CLINGS_CHECK_INT(values[4], 9);
free(values);
""",
        breaks=[
            (
                "for (size_t i = old_count; i < new_count; ++i) {",
                "/* TODO: preserve the existing elements. */\n    for (size_t i = 0; i < new_count; ++i) {",
            )
        ],
    ),
    ex(
        topic="09_dynamic_memory",
        slug="04_memory_leak",
        title="Detecting a memory leak",
        objective="Pair every allocation with a matching free.",
        reference="",
        hint="The cleanup path must release the tracked allocation.",
        code=r"""
#include <stdlib.h>

static size_t outstanding_allocations = 0;

static void *tracked_malloc(size_t size)
{
    void *pointer = malloc(size);
    if (pointer != NULL) {
        ++outstanding_allocations;
    }
    return pointer;
}

static void tracked_free(void *pointer)
{
    if (pointer != NULL) {
        --outstanding_allocations;
    }
    free(pointer);
}

size_t outstanding(void)
{
    return outstanding_allocations;
}

int sum_and_free(const int *values, int count, int *out)
{
    int *copy = tracked_malloc((size_t)count * sizeof *copy);
    if (copy == NULL) {
        return -1;
    }

    int sum = 0;
    for (int i = 0; i < count; ++i) {
        copy[i] = values[i];
        sum += copy[i];
    }
    *out = sum;

    tracked_free(copy);
    return 0;
}
""",
        tests=r"""
const int values[] = {1, 2, 3};
int out = 0;

CLINGS_CHECK_INT(outstanding(), 0);
CLINGS_CHECK_INT(sum_and_free(values, 3, &out), 0);
CLINGS_CHECK_INT(out, 6);
CLINGS_CHECK_INT(outstanding(), 0);
""",
        breaks=[
            (
                "tracked_free(copy);",
                "/* TODO: release the tracked allocation. */",
            )
        ],
    ),
    ex(
        topic="09_dynamic_memory",
        slug="05_buffer_bounds",
        title="Respecting buffer bounds",
        objective="Copy at most dest_size - 1 bytes and always terminate.",
        reference="",
        hint="Leave room for the terminating NUL.",
        code=r"""
#include <stddef.h>

int bounded_copy(char *destination, size_t destination_size, const char *source)
{
    size_t i = 0;
    for (; i + 1 < destination_size && source[i] != '\0'; ++i) {
        destination[i] = source[i];
    }
    destination[i] = '\0';
    return (int)i;
}
""",
        tests=r"""
char buffer[5];
int copied = 0;

buffer[4] = 'X';
copied = bounded_copy(buffer, 4, "hello");
CLINGS_CHECK_INT(copied, 3);
CLINGS_CHECK_STR(buffer, "hel");
CLINGS_CHECK_INT(buffer[4], 'X');
""",
        breaks=[
            (
                "for (; i + 1 < destination_size && source[i] != '\\0'; ++i) {",
                "/* TODO: leave room for the terminator. */\n    for (; i < destination_size && source[i] != '\\0'; ++i) {",
            )
        ],
    ),
    ex(
        topic="09_dynamic_memory",
        slug="06_flexible_array",
        title="Flexible array members",
        objective="Allocate a struct plus trailing data in one block.",
        reference="",
        hint="The allocation size is sizeof *packet + length bytes.",
        code=r"""
#include <stdlib.h>
#include <string.h>

struct packet {
    size_t length;
    unsigned char data[];
};

struct packet *packet_create(size_t length, const unsigned char *data)
{
    struct packet *packet = malloc(sizeof *packet + length);
    if (packet == NULL) {
        return NULL;
    }
    packet->length = length;
    memcpy(packet->data, data, length);
    return packet;
}

void packet_destroy(struct packet *packet)
{
    free(packet);
}
""",
        tests=r"""
const unsigned char payload[] = {1, 2, 3, 4};
struct packet *packet = packet_create(4, payload);

CLINGS_CHECK(packet != NULL);
CLINGS_CHECK_INT(packet->length, 4);
CLINGS_CHECK_INT(packet->data[0], 1);
CLINGS_CHECK_INT(packet->data[3], 4);
packet_destroy(packet);
""",
        breaks=[
            (
                "packet->length = length;",
                "/* TODO: record the payload length. */\n    packet->length = 0;",
            )
        ],
    ),
    ex(
        topic="09_dynamic_memory",
        slug="07_linked_list",
        title="A singly linked list",
        objective="Build, traverse, and free a linked list.",
        reference="",
        hint="The new node must point at the previous head.",
        code=r"""
#include <stdlib.h>
#include <stddef.h>

struct node {
    int value;
    struct node *next;
};

struct node *list_push(struct node *head, int value)
{
    struct node *node = malloc(sizeof *node);
    if (node == NULL) {
        return head;
    }
    node->value = value;
    node->next = head;
    return node;
}

size_t list_length(const struct node *head)
{
    size_t count = 0;
    for (const struct node *node = head; node != NULL; node = node->next) {
        ++count;
    }
    return count;
}

void list_free(struct node *head)
{
    while (head != NULL) {
        struct node *next = head->next;
        free(head);
        head = next;
    }
}
""",
        tests=r"""
struct node *head = NULL;

head = list_push(head, 1);
head = list_push(head, 2);
head = list_push(head, 3);
CLINGS_CHECK_INT(list_length(head), 3);
CLINGS_CHECK_INT(head->value, 3);
CLINGS_CHECK_INT(head->next->value, 2);
list_free(head);
""",
        breaks=[
            (
                "node->next = head;",
                "/* TODO: link the new node to the old head. */\n    node->next = NULL;",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 08_structs_unions_enums
    # ------------------------------------------------------------------
    ex(
        topic="10_aggregates",
        slug="01_struct_basics",
        title="Defining and using structs",
        objective="Create a struct value and access its members through a pointer.",
        reference="",
        hint="Use the arrow operator when you have a pointer.",
        code=r"""
struct point {
    int x;
    int y;
};

struct point make_point(int x, int y)
{
    struct point point = {x, y};
    return point;
}

int point_sum(const struct point *point)
{
    return point->x + point->y;
}
""",
        tests=r"""
struct point point = make_point(3, 4);

CLINGS_CHECK_INT(point.x, 3);
CLINGS_CHECK_INT(point.y, 4);
CLINGS_CHECK_INT(point_sum(&point), 7);
""",
        breaks=[
            (
                "return point->x + point->y;",
                "/* TODO: return the sum of both coordinates. */\n    return point->x - point->y;",
            )
        ],
    ),
    ex(
        topic="10_aggregates",
        slug="02_nested_structs",
        title="Nested structs",
        objective="Access a nested member through an outer struct pointer.",
        reference="",
        hint="The address lives inside the person struct.",
        code=r"""
#include <stdio.h>

struct address {
    char city[32];
    int zip;
};

struct person {
    char name[32];
    struct address address;
};

void set_city(struct person *person, const char *city)
{
    snprintf(person->address.city, sizeof person->address.city, "%s", city);
}
""",
        tests=r"""
struct person person = {0};

set_city(&person, "Shenzhen");
CLINGS_CHECK_STR(person.address.city, "Shenzhen");
""",
        breaks=[
            (
                "snprintf(person->address.city, sizeof person->address.city, \"%s\", city);",
                "/* TODO: write into the nested city field. */\n    snprintf(person->name, sizeof person->name, \"%s\", city);",
            )
        ],
    ),
    ex(
        topic="10_aggregates",
        slug="03_padding_alignment",
        title="Padding and alignment",
        objective="Observe padding and member offsets with offsetof.",
        reference="",
        hint="offsetof takes the struct type and the member name.",
        code=r"""
#include <stddef.h>

struct padded {
    char first;
    int value;
    char last;
};

int value_offset(void)
{
    return (int)offsetof(struct padded, value);
}

int padded_size(void)
{
    return (int)sizeof(struct padded);
}
""",
        tests=r"""
CLINGS_CHECK(value_offset() >= (int)sizeof(char));
CLINGS_CHECK(padded_size() >= value_offset() + (int)sizeof(int) + 1);
CLINGS_CHECK_INT((int)sizeof(struct padded) % (int)sizeof(int), 0);
""",
        breaks=[
            (
                "return (int)offsetof(struct padded, value);",
                "/* TODO: measure the offset of the value member. */\n    return (int)offsetof(struct padded, first);",
            )
        ],
    ),
    ex(
        topic="10_aggregates",
        slug="04_bitfields",
        title="Bitfields",
        objective="Store several small flags in one struct.",
        reference="",
        hint="The write flag must reflect the enabled argument.",
        code=r"""
struct permissions {
    unsigned int read : 1;
    unsigned int write : 1;
    unsigned int execute : 1;
    unsigned int reserved : 29;
};

int flag_enabled(const struct permissions *permissions, int which)
{
    switch (which) {
    case 0:
        return permissions->read != 0;
    case 1:
        return permissions->write != 0;
    case 2:
        return permissions->execute != 0;
    default:
        return -1;
    }
}

void set_flag(struct permissions *permissions, int which, int enabled)
{
    switch (which) {
    case 0:
        permissions->read = enabled ? 1u : 0u;
        break;
    case 1:
        permissions->write = enabled ? 1u : 0u;
        break;
    case 2:
        permissions->execute = enabled ? 1u : 0u;
        break;
    default:
        break;
    }
}
""",
        tests=r"""
struct permissions permissions = {0, 0, 0, 0};

set_flag(&permissions, 1, 1);
CLINGS_CHECK_INT(flag_enabled(&permissions, 1), 1);
set_flag(&permissions, 1, 0);
CLINGS_CHECK_INT(flag_enabled(&permissions, 1), 0);
CLINGS_CHECK_INT(flag_enabled(&permissions, 9), -1);
""",
        breaks=[
            (
                "permissions->write = enabled ? 1u : 0u;",
                "/* TODO: honor the enabled argument. */\n        permissions->write = 1u;",
            )
        ],
    ),
    ex(
        topic="10_aggregates",
        slug="05_union",
        title="Unions share storage",
        objective="Compare union size with the size of its largest member.",
        reference="",
        hint="Every union member starts at the same address.",
        code=r"""
#include <stddef.h>

union word {
    unsigned char bytes[4];
    unsigned int value;
};

int union_size_is_largest_member(void)
{
    return sizeof(union word) == sizeof(unsigned int);
}

int members_share_address(union word *word)
{
    return (void *)&word->bytes == (void *)&word->value;
}
""",
        tests=r"""
union word word = {0};

CLINGS_CHECK_INT(union_size_is_largest_member(), 1);
CLINGS_CHECK_INT(members_share_address(&word), 1);
""",
        breaks=[
            (
                "return sizeof(union word) == sizeof(unsigned int);",
                "/* TODO: a union is only as large as its largest member. */\n    return sizeof(union word) == sizeof(unsigned int) + sizeof(unsigned char[4]);",
            )
        ],
    ),
    ex(
        topic="10_aggregates",
        slug="06_enum",
        title="Enums",
        objective="Use an enum for a small closed set of values.",
        reference="",
        hint="Each case should return the matching color name.",
        code=r"""
enum color {
    COLOR_RED,
    COLOR_GREEN,
    COLOR_BLUE
};

const char *color_name(enum color color)
{
    switch (color) {
    case COLOR_RED:
        return "red";
    case COLOR_GREEN:
        return "green";
    case COLOR_BLUE:
        return "blue";
    default:
        return "unknown";
    }
}

int color_is_valid(int value)
{
    return value >= COLOR_RED && value <= COLOR_BLUE;
}
""",
        tests=r"""
CLINGS_CHECK_STR(color_name(COLOR_RED), "red");
CLINGS_CHECK_STR(color_name(COLOR_GREEN), "green");
CLINGS_CHECK_STR(color_name(COLOR_BLUE), "blue");
CLINGS_CHECK_INT(color_is_valid(COLOR_BLUE), 1);
CLINGS_CHECK_INT(color_is_valid(99), 0);
""",
        breaks=[
            (
                'case COLOR_BLUE:\n        return "blue";',
                'case COLOR_BLUE:\n        /* TODO: return the blue color name. */\n        return "green";',
            )
        ],
    ),
    ex(
        topic="10_aggregates",
        slug="07_typedef_designated",
        title="typedef and designated initializers",
        objective="Use a typedef and initialize members by name.",
        reference="",
        hint="Designated initializers make the field mapping explicit.",
        code=r"""
typedef struct {
    int x;
    int y;
} point_t;

point_t make_point(int x, int y)
{
    point_t point = {.x = x, .y = y};
    return point;
}
""",
        tests=r"""
point_t point = make_point(3, 4);

CLINGS_CHECK_INT(point.x, 3);
CLINGS_CHECK_INT(point.y, 4);
""",
        breaks=[
            (
                "point_t point = {.x = x, .y = y};",
                "/* TODO: initialize both members by name. */\n    point_t point = {.x = x, .y = 0};",
            )
        ],
    ),
    ex(
        topic="10_aggregates",
        slug="08_container_of",
        title="offsetof and container_of",
        objective="Recover an outer struct from a pointer to one of its members.",
        reference="",
        hint="Subtract the byte offset of the inner member.",
        code=r"""
#include <stddef.h>

struct inner {
    int value;
};

struct outer {
    int id;
    struct inner inner;
};

struct outer *outer_from_inner(struct inner *inner)
{
    return (struct outer *)((char *)inner - offsetof(struct outer, inner));
}
""",
        tests=r"""
struct outer outer = {.id = 42, .inner = {.value = 7}};
struct outer *recovered = outer_from_inner(&outer.inner);

CLINGS_CHECK(recovered == &outer);
CLINGS_CHECK_INT(recovered->id, 42);
CLINGS_CHECK_INT(recovered->inner.value, 7);
""",
        breaks=[
            (
                "return (struct outer *)((char *)inner - offsetof(struct outer, inner));",
                "/* TODO: subtract the offset of the inner member. */\n    return (struct outer *)((char *)inner);",
            )
        ],
    ),
    ex(
        topic="08_arrays_strings",
        slug="18_escaped_strings",
        title="Escaped strings and line continuation",
        objective="Use escape sequences inside a string literal and continue lines explicitly.",
        reference="",
        hint="Escape sequences keep their meaning inside string literals.",
        code=r"""
const char *escaped_text(void)
{
    return "line1\nline2\t\"quoted\"";
}

int continued_sum(void)
{
    int sum = 1 + \
              2 + \
              3;
    return sum;
}

int comment_is_ignored(void)
{
    return 1 /* comment */ + 2;
}
""",
        tests=r"""
CLINGS_CHECK_STR(escaped_text(), "line1\nline2\t\"quoted\"");
CLINGS_CHECK_INT(continued_sum(), 6);
CLINGS_CHECK_INT(comment_is_ignored(), 3);
""",
        breaks=[
            (
                'return "line1\\nline2\\t\\"quoted\\"";',
                '/* TODO: restore the escape sequences. */\n    return "line1 line2 quoted";',
            )
        ],
    ),
]
