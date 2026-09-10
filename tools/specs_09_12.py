"""Exercise specifications for topics 09 through 12."""

from spec import ex

SPECS = [
    # ------------------------------------------------------------------
    # 09_preprocessor
    # ------------------------------------------------------------------
    ex(
        topic="09_preprocessor",
        slug="01_object_macro",
        title="Object-like macros",
        objective="Use a named compile-time constant.",
        reference="",
        hint="Object-like macros are simple text substitutions.",
        code=r"""
#define CLINGS_BUFFER_SIZE 16
#define CLINGS_VERSION 2

int buffer_size(void)
{
    return CLINGS_BUFFER_SIZE;
}

int version(void)
{
    return CLINGS_VERSION;
}
""",
        tests=r"""
CLINGS_CHECK_INT(buffer_size(), 16);
CLINGS_CHECK_INT(version(), 2);
""",
        breaks=[
            (
                "#define CLINGS_BUFFER_SIZE 16",
                "/* TODO: define a 16-byte buffer size. */\n#define CLINGS_BUFFER_SIZE 8",
            )
        ],
    ),
    ex(
        topic="09_preprocessor",
        slug="02_function_macro",
        title="Function-like macros",
        objective="Protect macro arguments and the whole expansion with parentheses.",
        reference="",
        hint="Parenthesize both the parameters and the entire replacement expression.",
        code=r"""
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int min_value(int a, int b)
{
    return MIN(a, b);
}

int max_value(int a, int b)
{
    return MAX(a, b);
}
""",
        tests=r"""
CLINGS_CHECK_INT(min_value(3, 4), 3);
CLINGS_CHECK_INT(max_value(3, 4), 4);
CLINGS_CHECK_INT(MIN(2, 3) * 2, 4);
""",
        breaks=[
            (
                "#define MIN(a, b) ((a) < (b) ? (a) : (b))",
                "/* TODO: parenthesize the whole macro expansion. */\n#define MIN(a, b) (a) < (b) ? (a) : (b)",
            )
        ],
    ),
    ex(
        topic="09_preprocessor",
        slug="03_stringize_paste",
        title="Stringizing and token pasting",
        objective="Use # to stringize and ## to paste tokens.",
        reference="",
        hint="A second helper macro is needed to expand a macro before stringizing it.",
        code=r"""
#define CLINGS_VALUE 123

#define STRINGIFY_IMPL(x) #x
#define STRINGIFY(x) STRINGIFY_IMPL(x)

#define CONCAT_IMPL(a, b) a##b
#define CONCAT(a, b) CONCAT_IMPL(a, b)

const char *stringized_value(void)
{
    return STRINGIFY(CLINGS_VALUE);
}

int concatenated_value(void)
{
    int CONCAT(foo, bar) = 42;
    return foobar;
}
""",
        tests=r"""
CLINGS_CHECK_STR(stringized_value(), "123");
CLINGS_CHECK_INT(concatenated_value(), 42);
""",
        breaks=[
            (
                "#define STRINGIFY(x) STRINGIFY_IMPL(x)",
                "/* TODO: expand x before stringizing it. */\n#define STRINGIFY(x) #x",
            )
        ],
    ),
    ex(
        topic="09_preprocessor",
        slug="04_conditional_compilation",
        title="Conditional compilation",
        objective="Select code at preprocessing time based on the language version.",
        reference="",
        hint="C11 introduced __STDC_VERSION__ value 201112L.",
        code=r"""
#if defined(__STDC_VERSION__) && __STDC_VERSION__ >= 201112L
#define CLINGS_HAS_C11 1
#else
#define CLINGS_HAS_C11 0
#endif

int has_c11(void)
{
    return CLINGS_HAS_C11;
}
""",
        tests=r"""
CLINGS_CHECK_INT(has_c11(), 1);
""",
        breaks=[
            (
                "__STDC_VERSION__ >= 201112L",
                "/* TODO: test for C11 or newer. */\n__STDC_VERSION__ >= 999999L",
            )
        ],
    ),
    ex(
        topic="09_preprocessor",
        slug="05_include_guards",
        title="Include guards",
        objective="Prevent multiple inclusion with a preprocessor guard.",
        reference="",
        hint="Define the guard macro before the guarded declarations.",
        code=r"""
#ifndef CLINGS_GUARD_H
#define CLINGS_GUARD_H

int guarded_value(void);

#endif

int guarded_value(void)
{
    return 42;
}

int guard_is_defined(void)
{
#ifdef CLINGS_GUARD_H
    return 1;
#else
    return 0;
#endif
}
""",
        tests=r"""
CLINGS_CHECK_INT(guard_is_defined(), 1);
CLINGS_CHECK_INT(guarded_value(), 42);
""",
        breaks=[
            (
                "#define CLINGS_GUARD_H",
                "/* TODO: define the include guard macro. */",
            )
        ],
    ),
    ex(
        topic="09_preprocessor",
        slug="06_variadic_macros",
        title="Variadic macros",
        objective="Forward a variable argument list to a variadic function.",
        reference="",
        hint="SUM(...) should pass every argument, including the count.",
        code=r"""
#include <stdarg.h>

int sum_variadic(int count, ...)
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

#define SUM(...) sum_variadic(__VA_ARGS__)
""",
        tests=r"""
CLINGS_CHECK_INT(SUM(3, 1, 2, 3), 6);
CLINGS_CHECK_INT(SUM(0), 0);
""",
        breaks=[
            (
                "#define SUM(...) sum_variadic(__VA_ARGS__)",
                "/* TODO: forward all arguments, including the count. */\n#define SUM(...) sum_variadic(0, __VA_ARGS__)",
            )
        ],
    ),
    ex(
        topic="09_preprocessor",
        slug="07_x_macros",
        title="X-macros",
        objective="Generate an enum and a string table from one list.",
        reference="",
        hint="The string table uses #name, not a fixed string.",
        code=r"""
#define COLOR_LIST(X) X(RED) X(GREEN) X(BLUE)

enum color {
#define X(name) COLOR_##name,
    COLOR_LIST(X)
#undef X
};

static const char *const color_names[] = {
#define X(name) #name,
    COLOR_LIST(X)
#undef X
};
""",
        tests=r"""
CLINGS_CHECK_STR(color_names[COLOR_RED], "RED");
CLINGS_CHECK_STR(color_names[COLOR_GREEN], "GREEN");
CLINGS_CHECK_STR(color_names[COLOR_BLUE], "BLUE");
""",
        breaks=[
            (
                "#define X(name) #name,",
                "/* TODO: stringize each name. */\n#define X(name) \"unknown\",",
            )
        ],
    ),
    ex(
        topic="09_preprocessor",
        slug="08_pragma_error_line",
        title="#error, #line, and #pragma pack",
        objective="Use diagnostics, line control, and packing pragmas.",
        reference="",
        hint="#pragma pack(push, 1) removes padding between the two members.",
        code=r"""
#include <stddef.h>

#if 0
#error "this branch is disabled"
#endif

#pragma pack(push, 1)
struct packed {
    char first;
    int second;
};
#pragma pack(pop)

int packed_size(void)
{
    return (int)sizeof(struct packed);
}

int line_number(void)
{
#line 1000
    return __LINE__;
}
""",
        tests=r"""
CLINGS_CHECK_INT(packed_size(), (int)(sizeof(char) + sizeof(int)));
CLINGS_CHECK_INT(line_number(), 1000);
""",
        breaks=[
            (
                "#pragma pack(push, 1)",
                "/* TODO: pack the struct without padding. */\n#pragma pack(push, 4)",
            )
        ],
    ),
    # ------------------------------------------------------------------
    # 10_stdlib_io
    # ------------------------------------------------------------------
    ex(
        topic="10_stdlib_io",
        slug="01_printf_formats",
        title="printf format specifiers",
        objective="Match each conversion specifier to its argument type.",
        reference="",
        hint="long values use %ld; doubles use %f or %.2f.",
        code=r"""
#include <stdio.h>

int format_all(char *buffer, size_t size, long value, double real,
               const char *text)
{
    return snprintf(buffer, size, "%ld %.2f %s", value, real, text);
}
""",
        tests=r"""
char buffer[64];

CLINGS_CHECK_INT(format_all(buffer, sizeof buffer, 42L, 3.5, "ok"), 10);
CLINGS_CHECK_STR(buffer, "42 3.50 ok");
""",
        breaks=[
            (
                'return snprintf(buffer, size, "%ld %.2f %s", value, real, text);',
                '/* TODO: use the correct specifier for a long value. */\n    return snprintf(buffer, size, "%d %.2f %s", value, real, text);',
            )
        ],
        compile_fail=True,
    ),
    ex(
        topic="10_stdlib_io",
        slug="02_scanf_parse",
        title="Parsing with scanf",
        objective="Parse a comma-separated pair with sscanf.",
        reference="",
        hint="The literal comma in the format must match the input.",
        code=r"""
#include <stdio.h>

int parse_pair(const char *input, int *first, int *second)
{
    return sscanf(input, "%d,%d", first, second) == 2 ? 0 : -1;
}
""",
        tests=r"""
int first = 0;
int second = 0;

CLINGS_CHECK_INT(parse_pair("3,4", &first, &second), 0);
CLINGS_CHECK_INT(first, 3);
CLINGS_CHECK_INT(second, 4);
CLINGS_CHECK_INT(parse_pair("3 4", &first, &second), -1);
""",
        breaks=[
            (
                'return sscanf(input, "%d,%d", first, second) == 2 ? 0 : -1;',
                '/* TODO: parse the comma separator. */\n    return sscanf(input, "%d %d", first, second) == 2 ? 0 : -1;',
            )
        ],
    ),
    ex(
        topic="10_stdlib_io",
        slug="03_strtol_errno",
        title="Robust integer parsing",
        objective="Use strtol, errno, and the end pointer to validate input.",
        reference="",
        hint="Reject empty input, trailing characters, ERANGE, and out-of-range values.",
        code=r"""
#include <errno.h>
#include <limits.h>
#include <stdlib.h>

int parse_int(const char *text, int *out)
{
    char *end = NULL;
    errno = 0;
    long value = strtol(text, &end, 10);

    if (errno == ERANGE || end == text || *end != '\0' ||
        value < INT_MIN || value > INT_MAX) {
        return -1;
    }

    *out = (int)value;
    return 0;
}
""",
        tests=r"""
int out = 0;

CLINGS_CHECK_INT(parse_int("123", &out), 0);
CLINGS_CHECK_INT(out, 123);
CLINGS_CHECK_INT(parse_int("-7", &out), 0);
CLINGS_CHECK_INT(out, -7);
CLINGS_CHECK_INT(parse_int("12x", &out), -1);
CLINGS_CHECK_INT(parse_int("", &out), -1);
CLINGS_CHECK_INT(parse_int("99999999999999999999", &out), -1);
""",
        breaks=[
            (
                "if (errno == ERANGE || end == text || *end != '\\0' ||\n        value < INT_MIN || value > INT_MAX) {",
                "/* TODO: validate every part of the conversion. */\n    if (0) {",
            )
        ],
    ),
    ex(
        topic="10_stdlib_io",
        slug="04_qsort_bsearch",
        title="qsort and bsearch",
        objective="Use comparison callbacks for sorting and searching.",
        reference="",
        hint="The comparator returns negative, zero, or positive.",
        code=r"""
#include <stdlib.h>

static int compare_ints(const void *left, const void *right)
{
    int a = *(const int *)left;
    int b = *(const int *)right;
    return (a > b) - (a < b);
}

void sort_ints(int *values, size_t count)
{
    qsort(values, count, sizeof *values, compare_ints);
}

int *find_int(int *values, size_t count, int needle)
{
    return bsearch(&needle, values, count, sizeof *values, compare_ints);
}
""",
        tests=r"""
int values[] = {4, 1, 3, 2};
int needle = 3;

sort_ints(values, 4);
CLINGS_CHECK_INT(values[0], 1);
CLINGS_CHECK_INT(values[1], 2);
CLINGS_CHECK_INT(values[2], 3);
CLINGS_CHECK_INT(values[3], 4);
CLINGS_CHECK(find_int(values, 4, needle) != NULL);
CLINGS_CHECK(find_int(values, 4, 99) == NULL);
""",
        breaks=[
            (
                "return (a > b) - (a < b);",
                "/* TODO: return ascending order. */\n    return (a < b) - (a > b);",
            )
        ],
    ),
    ex(
        topic="10_stdlib_io",
        slug="05_math_functions",
        title="The math library",
        objective="Use hypot and other functions from math.h.",
        reference="",
        hint="hypot(x, y) computes sqrt(x*x + y*y) without avoidable overflow.",
        code=r"""
#include <math.h>

double distance(double x1, double y1, double x2, double y2)
{
    return hypot(x2 - x1, y2 - y1);
}
""",
        tests=r"""
CLINGS_CHECK_INT(distance(0.0, 0.0, 3.0, 4.0) == 5.0, 1);
CLINGS_CHECK_INT(distance(1.0, 1.0, 1.0, 1.0) == 0.0, 1);
""",
        breaks=[
            (
                "return hypot(x2 - x1, y2 - y1);",
                "/* TODO: compute the Euclidean distance. */\n    return fabs(x2 - x1) + fabs(y2 - y1);",
            )
        ],
    ),
    ex(
        topic="10_stdlib_io",
        slug="06_time_functions",
        title="Time arithmetic",
        objective="Use time_t and difftime.",
        reference="",
        hint="difftime(end, start) returns end - start seconds.",
        code=r"""
#include <time.h>

long seconds_between(time_t start, time_t end)
{
    return (long)difftime(end, start);
}
""",
        tests=r"""
CLINGS_CHECK_INT(seconds_between(100, 250), 150);
CLINGS_CHECK_INT(seconds_between(250, 100), -150);
""",
        breaks=[
            (
                "return (long)difftime(end, start);",
                "/* TODO: subtract start from end. */\n    return (long)difftime(start, end);",
            )
        ],
    ),
    ex(
        topic="10_stdlib_io",
        slug="07_random",
        title="Pseudo-random numbers",
        objective="Seed the generator and bound its output.",
        reference="",
        hint="rand() % upper produces values from 0 to upper - 1.",
        code=r"""
#include <stdlib.h>

void seed_random(unsigned int seed)
{
    srand(seed);
}

int random_bounded(int upper)
{
    return upper > 0 ? rand() % upper : 0;
}
""",
        tests=r"""
seed_random(42u);
int first = random_bounded(10);
seed_random(42u);
int second = random_bounded(10);

CLINGS_CHECK_INT(first, second);
CLINGS_CHECK(first >= 0 && first < 10);
CLINGS_CHECK_INT(random_bounded(0), 0);
""",
        breaks=[
            (
                "return upper > 0 ? rand() % upper : 0;",
                "/* TODO: keep the result below upper. */\n    return upper > 0 ? upper : 0;",
            )
        ],
    ),
    ex(
        topic="10_stdlib_io",
        slug="08_file_io",
        title="Text file I/O",
        objective="Write and read a text file with fopen, fputs, and fread.",
        reference="",
        hint="Use mode \"w\" for writing and mode \"r\" for reading.",
        code=r"""
#include <stdio.h>

int write_text_file(const char *path, const char *text)
{
    FILE *file = fopen(path, "w");
    if (file == NULL) {
        return -1;
    }
    int ok = fputs(text, file) >= 0;
    if (fclose(file) != 0) {
        ok = 0;
    }
    return ok ? 0 : -1;
}

int read_text_file(const char *path, char *buffer, size_t size)
{
    FILE *file = fopen(path, "r");
    if (file == NULL) {
        return -1;
    }
    size_t count = fread(buffer, 1, size - 1, file);
    buffer[count] = '\0';
    fclose(file);
    return (int)count;
}
""",
        tests=r"""
const char *path = "/tmp/clings_file_io_test.txt";
char buffer[32];

CLINGS_CHECK_INT(write_text_file(path, "hello"), 0);
CLINGS_CHECK_INT(read_text_file(path, buffer, sizeof buffer), 5);
CLINGS_CHECK_STR(buffer, "hello");
remove(path);
""",
        breaks=[
            (
                'FILE *file = fopen(path, "w");',
                '/* TODO: open the file for writing. */\n    FILE *file = fopen(path, "r");',
            )
        ],
    ),
    ex(
        topic="10_stdlib_io",
        slug="09_memory_functions",
        title="memcpy, memmove, memset, and memcmp",
        objective="Use the byte-oriented memory functions correctly.",
        reference="",
        hint="memcpy requires non-overlapping regions; memmove handles overlap.",
        code=r"""
#include <string.h>

void copy_ints(int *destination, const int *source, size_t count)
{
    memcpy(destination, source, count * sizeof *destination);
}

void move_overlapping(char *buffer, size_t size)
{
    memmove(buffer + 1, buffer, size - 1);
}

void clear_ints(int *values, size_t count)
{
    memset(values, 0, count * sizeof *values);
}

int ints_equal(const int *left, const int *right, size_t count)
{
    return memcmp(left, right, count * sizeof *left) == 0;
}
""",
        tests=r"""
const int source[3] = {1, 2, 3};
int destination[3] = {0, 0, 0};
char buffer[6] = "abcde";

copy_ints(destination, source, 3);
CLINGS_CHECK_INT(ints_equal(destination, source, 3), 1);
clear_ints(destination, 3);
CLINGS_CHECK_INT(destination[0], 0);
CLINGS_CHECK_INT(destination[2], 0);
move_overlapping(buffer, 5);
CLINGS_CHECK_STR(buffer, "aabcd");
""",
        breaks=[
            (
                "memcpy(destination, source, count * sizeof *destination);",
                "/* TODO: copy the whole array, not count bytes. */\n    memcpy(destination, source, count);",
            )
        ],
    ),
    ex(
        topic="10_stdlib_io",
        slug="10_string_search",
        title="Searching strings",
        objective="Use strchr, strrchr, and strstr.",
        reference="",
        hint="strstr finds a substring, not just a single character.",
        code=r"""
#include <string.h>

const char *find_first(const char *text, char character)
{
    return strchr(text, character);
}

const char *find_last(const char *text, char character)
{
    return strrchr(text, character);
}

const char *find_substring(const char *text, const char *needle)
{
    return strstr(text, needle);
}
""",
        tests=r"""
const char *text = "hello world";

CLINGS_CHECK(find_first(text, 'l') == text + 2);
CLINGS_CHECK(find_last(text, 'l') == text + 9);
CLINGS_CHECK(find_substring(text, "or") == text + 7);
CLINGS_CHECK(find_substring(text, "xyz") == NULL);
""",
        breaks=[
            (
                "return strstr(text, needle);",
                "/* TODO: search for the whole substring. */\n    return strchr(text, needle[0]);",
            )
        ],
    ),
    ex(
        topic="10_stdlib_io",
        slug="11_stdint_inttypes",
        title="Fixed-width integers and format macros",
        objective="Use uint64_t and PRIu64 from stdint.h and inttypes.h.",
        reference="",
        hint="PRIu64 is the portable printf specifier for uint64_t.",
        code=r"""
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>

int format_u64(char *buffer, size_t size, uint64_t value)
{
    return snprintf(buffer, size, "%" PRIu64, value);
}

uint32_t low_32_bits(uint64_t value)
{
    return (uint32_t)value;
}
""",
        tests=r"""
char buffer[32];

CLINGS_CHECK_INT(
    format_u64(buffer, sizeof buffer, UINT64_C(1234567890123)), 13);
CLINGS_CHECK_STR(buffer, "1234567890123");
CLINGS_CHECK_INT(low_32_bits(UINT64_C(0x1122334455667788)), 0x55667788u);
""",
        breaks=[
            (
                'return snprintf(buffer, size, "%" PRIu64, value);',
                '/* TODO: use the format macro for uint64_t. */\n    return snprintf(buffer, size, "%" PRIu32, value);',
            )
        ],
        compile_fail=True,
    ),
    ex(
        topic="10_stdlib_io",
        slug="12_environment",
        title="Environment variables",
        objective="Read and write environment variables with getenv and setenv.",
        reference="",
        hint="setenv must succeed before getenv can find the new value.",
        code=r"""
#include <stdio.h>
#include <stdlib.h>

int set_and_get(const char *name, const char *value, char *out, size_t size)
{
    if (setenv(name, value, 1) != 0) {
        return -1;
    }
    const char *found = getenv(name);
    if (found == NULL) {
        return -1;
    }
    snprintf(out, size, "%s", found);
    return 0;
}
""",
        tests=r"""
char buffer[32];
const char *name = "CLINGS_TEST_ENV_VARIABLE";

CLINGS_CHECK_INT(
    set_and_get(name, "hello", buffer, sizeof buffer), 0);
CLINGS_CHECK_STR(buffer, "hello");
unsetenv(name);
""",
        breaks=[
            (
                "const char *found = getenv(name);",
                "/* TODO: read the environment variable back. */\n    const char *found = NULL;",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 11_ub_safety
    # ------------------------------------------------------------------
    ex(
        topic="11_ub_safety",
        slug="01_signed_overflow",
        title="Avoid signed integer overflow",
        objective="Detect overflow before performing signed addition.",
        reference="",
        hint="Unsigned arithmetic wraps; signed overflow is undefined behavior.",
        code=r"""
#include <limits.h>

int checked_add(int a, int b, int *out)
{
    if ((b > 0 && a > INT_MAX - b) || (b < 0 && a < INT_MIN - b)) {
        return -1;
    }
    *out = a + b;
    return 0;
}
""",
        tests=r"""
int out = 0;

CLINGS_CHECK_INT(checked_add(INT_MAX, 1, &out), -1);
CLINGS_CHECK_INT(checked_add(INT_MIN, -1, &out), -1);
CLINGS_CHECK_INT(checked_add(20, 22, &out), 0);
CLINGS_CHECK_INT(out, 42);
""",
        breaks=[
            (
                "if ((b > 0 && a > INT_MAX - b) || (b < 0 && a < INT_MIN - b)) {",
                "/* TODO: detect overflow before adding. */\n    if (0) {",
            )
        ],
    ),
    ex(
        topic="11_ub_safety",
        slug="02_uninitialized",
        title="Initialize before use",
        objective="Give every local variable a defined initial value.",
        reference="",
        hint="Start result at -1 so the fallback path is well-defined.",
        code=r"""
int initialized_or_default(int value)
{
    int result = -1;
    if (value > 0) {
        result = value;
    }
    return result;
}
""",
        tests=r"""
CLINGS_CHECK_INT(initialized_or_default(0), -1);
CLINGS_CHECK_INT(initialized_or_default(-5), -1);
CLINGS_CHECK_INT(initialized_or_default(7), 7);
""",
        breaks=[
            (
                "int result = -1;",
                "/* TODO: initialize the fallback value. */\n    int result = 12345;",
            )
        ],
    ),
    ex(
        topic="11_ub_safety",
        slug="03_out_of_bounds",
        title="Bounds checking",
        objective="Reject indices outside the logical array length.",
        reference="",
        hint="An index is invalid when it is less than zero or greater than or equal to count.",
        code=r"""
int get_or_default(const int *values, int count, int index, int fallback)
{
    if (index < 0 || index >= count) {
        return fallback;
    }
    return values[index];
}
""",
        tests=r"""
const int values[] = {10, 20, 30, 999};

CLINGS_CHECK_INT(get_or_default(values, 3, 0, 123), 10);
CLINGS_CHECK_INT(get_or_default(values, 3, 2, 123), 30);
CLINGS_CHECK_INT(get_or_default(values, 3, 3, 123), 123);
CLINGS_CHECK_INT(get_or_default(values, 3, -1, 123), 123);
""",
        breaks=[
            (
                "if (index < 0 || index >= count) {",
                "/* TODO: reject indices that are out of range. */\n    if (index < 0 || index > count) {",
            )
        ],
    ),
    ex(
        topic="11_ub_safety",
        slug="04_use_after_free",
        title="Use-after-free",
        objective="Clear a pointer after freeing its target.",
        reference="",
        hint="Write NULL through the pointer-to-pointer after free.",
        code=r"""
#include <stdlib.h>

void free_and_clear(int **pointer)
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
*value = 7;
free_and_clear(&value);
CLINGS_CHECK_INT(is_null(value), 1);
""",
        breaks=[
            (
                "*pointer = NULL;",
                "/* TODO: clear the caller's pointer. */",
            )
        ],
    ),
    ex(
        topic="11_ub_safety",
        slug="05_sequence_points",
        title="Sequence points",
        objective="Avoid unsequenced reads and writes of the same object.",
        reference="",
        hint="Read the old value, update the object, then return the old value.",
        code=r"""
int next_value(int *value)
{
    int current = *value;
    *value = current + 1;
    return current;
}
""",
        tests=r"""
int value = 5;

CLINGS_CHECK_INT(next_value(&value), 5);
CLINGS_CHECK_INT(value, 6);
CLINGS_CHECK_INT(next_value(&value), 6);
CLINGS_CHECK_INT(value, 7);
""",
        breaks=[
            (
                "int current = *value;\n    *value = current + 1;\n    return current;",
                "/* TODO: do not read and modify the same object without a sequence point. */\n    return (*value)++ + *value;",
            )
        ],
        compile_fail=True,
    ),
    ex(
        topic="11_ub_safety",
        slug="06_strict_aliasing",
        title="Type punning without strict-aliasing violations",
        objective="Reinterpret object representation with memcpy.",
        reference="",
        hint="memcpy preserves the bit pattern; a cast to float converts the numeric value.",
        code=r"""
#include <string.h>

float bits_to_float(unsigned int bits)
{
    float value;
    memcpy(&value, &bits, sizeof value);
    return value;
}
""",
        tests=r"""
CLINGS_CHECK_INT(bits_to_float(0x3f800000u) == 1.0f, 1);
CLINGS_CHECK_INT(bits_to_float(0x00000000u) == 0.0f, 1);
""",
        breaks=[
            (
                "memcpy(&value, &bits, sizeof value);",
                "/* TODO: reinterpret the bit pattern instead of converting the number. */\n    value = (float)bits;",
            )
        ],
    ),
    ex(
        topic="11_ub_safety",
        slug="07_alignment",
        title="Alignment requirements",
        objective="Query alignment with alignof and keep members aligned.",
        reference="",
        hint="alignof reports the strictest alignment the type requires.",
        code=r"""
#include <stdalign.h>
#include <stddef.h>

struct aligned {
    char first;
    max_align_t second;
};

int align_of_int(void)
{
    return (int)alignof(int);
}

int second_member_is_aligned(void)
{
    return (offsetof(struct aligned, second) % alignof(max_align_t)) == 0;
}
""",
        tests=r"""
CLINGS_CHECK(align_of_int() >= (int)alignof(short));
CLINGS_CHECK_INT(second_member_is_aligned(), 1);
""",
        breaks=[
            (
                "return (int)alignof(int);",
                "/* TODO: report the actual alignment of int. */\n    return 1;",
            )
        ],
    ),
    ex(
        topic="11_ub_safety",
        slug="08_null_pointer",
        title="Null pointer checks",
        objective="Never dereference a null pointer.",
        reference="",
        hint="Use a conditional expression to provide a fallback.",
        code=r"""
int dereference_or_default(const int *pointer, int fallback)
{
    return pointer != NULL ? *pointer : fallback;
}
""",
        tests=r"""
int value = 42;

CLINGS_CHECK_INT(dereference_or_default(&value, -1), 42);
CLINGS_CHECK_INT(dereference_or_default(NULL, -1), -1);
""",
        breaks=[
            (
                "return pointer != NULL ? *pointer : fallback;",
                "/* TODO: return the pointed-to value only when the pointer is not null. */\n    return fallback;",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 12_advanced_c
    # ------------------------------------------------------------------
    ex(
        topic="12_advanced_c",
        slug="01_variadic",
        title="Variadic functions",
        objective="Read a variable number of int arguments with va_list.",
        reference="",
        hint="The loop must consume exactly count arguments.",
        code=r"""
#include <stdarg.h>

long sum_variadic(int count, ...)
{
    va_list arguments;
    va_start(arguments, count);

    long sum = 0;
    for (int i = 0; i < count; ++i) {
        sum += va_arg(arguments, int);
    }

    va_end(arguments);
    return sum;
}
""",
        tests=r"""
CLINGS_CHECK_INT(sum_variadic(0), 0);
CLINGS_CHECK_INT(sum_variadic(3, 1, 2, 3), 6);
CLINGS_CHECK_INT(sum_variadic(5, 10, 20, 30, 40, 50), 150);
""",
        breaks=[
            (
                "for (int i = 0; i < count; ++i) {",
                "/* TODO: consume every variadic argument. */\n    for (int i = 0; i < count - 1; ++i) {",
            )
        ],
    ),
    ex(
        topic="12_advanced_c",
        slug="02_setjmp_longjmp",
        title="setjmp and longjmp",
        objective="Use non-local jumps for a simple error path.",
        reference="",
        hint="longjmp returns control to the matching setjmp call.",
        code=r"""
#include <setjmp.h>

static jmp_buf jump_buffer;

static int checked_positive(int value)
{
    if (value < 0) {
        longjmp(jump_buffer, 1);
    }
    return value;
}

int run_checked(int value, int *out)
{
    if (setjmp(jump_buffer) != 0) {
        return -1;
    }
    *out = checked_positive(value);
    return 0;
}
""",
        tests=r"""
int out = 0;

CLINGS_CHECK_INT(run_checked(5, &out), 0);
CLINGS_CHECK_INT(out, 5);
CLINGS_CHECK_INT(run_checked(-1, &out), -1);
""",
        breaks=[
            (
                "longjmp(jump_buffer, 1);",
                "/* TODO: jump back to the setjmp call. */\n        return -1;",
            )
        ],
    ),
    ex(
        topic="12_advanced_c",
        slug="03_pthreads",
        title="POSIX threads and a mutex",
        objective="Create threads and protect shared state with a mutex.",
        reference="",
        hint="Each worker increments the shared counter 1000 times.",
        code=r"""
#include <pthread.h>

struct counter {
    long value;
};

static pthread_mutex_t counter_mutex = PTHREAD_MUTEX_INITIALIZER;

static void *worker(void *argument)
{
    struct counter *counter = argument;
    for (int i = 0; i < 1000; ++i) {
        pthread_mutex_lock(&counter_mutex);
        counter->value += 1;
        pthread_mutex_unlock(&counter_mutex);
    }
    return NULL;
}

int run_threads(void)
{
    struct counter counter = {0};
    pthread_t first;
    pthread_t second;

    if (pthread_create(&first, NULL, worker, &counter) != 0) {
        return -1;
    }
    if (pthread_create(&second, NULL, worker, &counter) != 0) {
        pthread_join(first, NULL);
        return -1;
    }

    pthread_join(first, NULL);
    pthread_join(second, NULL);
    return (int)counter.value;
}
""",
        tests=r"""
CLINGS_CHECK_INT(run_threads(), 2000);
""",
        breaks=[
            (
                "counter->value += 1;",
                "/* TODO: increment the shared counter. */\n        counter->value += 0;",
            )
        ],
    ),
    ex(
        topic="12_advanced_c",
        slug="04_atomics",
        title="C11 atomics",
        objective="Use atomic_int for lock-free counter updates.",
        reference="",
        hint="atomic_fetch_add adds to the current value and returns the old value.",
        code=r"""
#include <stdatomic.h>

struct atomic_counter {
    atomic_int value;
};

void atomic_counter_init(struct atomic_counter *counter)
{
    atomic_init(&counter->value, 0);
}

void atomic_counter_add(struct atomic_counter *counter, int amount)
{
    atomic_fetch_add(&counter->value, amount);
}

int atomic_counter_get(const struct atomic_counter *counter)
{
    return atomic_load(&counter->value);
}
""",
        tests=r"""
struct atomic_counter counter;

atomic_counter_init(&counter);
atomic_counter_add(&counter, 5);
CLINGS_CHECK_INT(atomic_counter_get(&counter), 5);
atomic_counter_add(&counter, 3);
CLINGS_CHECK_INT(atomic_counter_get(&counter), 8);
""",
        breaks=[
            (
                "atomic_fetch_add(&counter->value, amount);",
                "/* TODO: add amount to the existing value. */\n    atomic_store(&counter->value, amount);",
            )
        ],
    ),
    ex(
        topic="12_advanced_c",
        slug="05_generic",
        title="_Generic selection",
        objective="Choose an expression based on the type of a value.",
        reference="",
        hint="The controlling expression is not evaluated; only its type is used.",
        code=r"""
#define type_name(value)                                                     \
    _Generic((value), int: "int", double: "double", char *: "char *",        \
             default: "other")
""",
        tests=r"""
CLINGS_CHECK_STR(type_name(1), "int");
CLINGS_CHECK_STR(type_name(1.0), "double");
CLINGS_CHECK_STR(type_name("text"), "char *");
CLINGS_CHECK_STR(type_name(1L), "other");
""",
        breaks=[
            (
                'int: "int"',
                '/* TODO: return "int" for the int case. */ int: "integer"',
            )
        ],
    ),
    ex(
        topic="12_advanced_c",
        slug="06_static_assert",
        title="Compile-time assertions",
        objective="Use _Static_assert to enforce assumptions at compile time.",
        reference="",
        hint="A failed static assertion must make the build fail.",
        code=r"""
#include <limits.h>

_Static_assert(sizeof(int) >= 2, "int must be at least 16 bits");
_Static_assert(CHAR_BIT == 8, "this course assumes 8-bit bytes");

int static_asserts_passed(void)
{
    return 1;
}
""",
        tests=r"""
CLINGS_CHECK_INT(static_asserts_passed(), 1);
""",
        breaks=[
            (
                '_Static_assert(sizeof(int) >= 2, "int must be at least 16 bits");',
                '/* TODO: restore the correct compile-time assumption. */\n_Static_assert(sizeof(int) >= 100, "int must be at least 16 bits");',
            )
        ],
        compile_fail=True,
    ),
    ex(
        topic="12_advanced_c",
        slug="07_align",
        title="alignof and alignas",
        objective="Query and request alignment.",
        reference="",
        hint="Double usually requires more alignment than int.",
        code=r"""
#include <stdalign.h>

int align_of_int(void)
{
    return (int)alignof(int);
}

int align_of_double(void)
{
    return (int)alignof(double);
}
""",
        tests=r"""
CLINGS_CHECK(align_of_int() >= (int)alignof(short));
CLINGS_CHECK(align_of_double() >= align_of_int());
""",
        breaks=[
            (
                "return (int)alignof(double);",
                "/* TODO: report the alignment of double. */\n    return 1;",
            )
        ],
    ),
    ex(
        topic="12_advanced_c",
        slug="08_anonymous_union",
        title="Anonymous structs and unions",
        objective="Access anonymous union members directly through the outer struct.",
        reference="",
        hint="An anonymous union member is promoted into the enclosing struct scope.",
        code=r"""
struct variant {
    int kind;
    union {
        int integer;
        double real;
    };
};

int variant_integer(const struct variant *value)
{
    return value->integer;
}

double variant_real(const struct variant *value)
{
    return value->real;
}
""",
        tests=r"""
struct variant integer_value = {0};
struct variant real_value = {0};

integer_value.kind = 1;
integer_value.integer = 42;
CLINGS_CHECK_INT(variant_integer(&integer_value), 42);
real_value.real = 3.5;
CLINGS_CHECK_INT(variant_real(&real_value) == 3.5, 1);
""",
        breaks=[
            (
                "return value->integer;",
                "/* TODO: read the anonymous union member. */\n    return value->kind;",
            )
        ],
    ),
    ex(
        topic="12_advanced_c",
        slug="09_thread_local",
        title="Thread-local storage",
        objective="Use _Thread_local to give each thread its own object.",
        reference="",
        hint="The worker thread modifies its own copy of thread_value.",
        code=r"""
#include <pthread.h>

static _Thread_local int thread_value = 0;

static void *worker(void *argument)
{
    (void)argument;
    thread_value = 42;
    return NULL;
}

int thread_local_demo(void)
{
    pthread_t thread;
    thread_value = 7;
    if (pthread_create(&thread, NULL, worker, NULL) != 0) {
        return -1;
    }
    pthread_join(thread, NULL);
    return thread_value;
}
""",
        tests=r"""
CLINGS_CHECK_INT(thread_local_demo(), 7);
""",
        breaks=[
            (
                "static _Thread_local int thread_value = 0;",
                "/* TODO: make thread_value thread-local. */\nstatic int thread_value = 0;",
            )
        ],
    ),
    ex(
        topic="12_advanced_c",
        slug="10_complex",
        title="Complex numbers",
        objective="Use double complex, I, conj, creal, and cimag.",
        reference="",
        hint="conj changes the sign of the imaginary part.",
        code=r"""
#include <complex.h>

double complex make_complex(double real, double imaginary)
{
    return real + imaginary * I;
}

double complex conjugate_value(double complex value)
{
    return conj(value);
}

double real_part(double complex value)
{
    return creal(value);
}

double imaginary_part(double complex value)
{
    return cimag(value);
}
""",
        tests=r"""
double complex value = make_complex(3.0, 4.0);
double complex conjugated = conjugate_value(value);

CLINGS_CHECK_INT(real_part(value) == 3.0, 1);
CLINGS_CHECK_INT(imaginary_part(value) == 4.0, 1);
CLINGS_CHECK_INT(imaginary_part(conjugated) == -4.0, 1);
""",
        breaks=[
            (
                "return conj(value);",
                "/* TODO: return the complex conjugate. */\n    return value;",
            )
        ],
    ),
    ex(
        topic="12_advanced_c",
        slug="11_signal",
        title="Signals and sig_atomic_t",
        objective="Install a signal handler and use a sig_atomic_t flag.",
        reference="",
        hint="raise(SIGINT) invokes the installed handler synchronously.",
        code=r"""
#include <signal.h>

static volatile sig_atomic_t caught = 0;

static void handle_signal(int signal_number)
{
    (void)signal_number;
    caught = 1;
}

int raise_and_catch(void)
{
    caught = 0;
    if (signal(SIGINT, handle_signal) == SIG_ERR) {
        return -1;
    }
    if (raise(SIGINT) != 0) {
        return -1;
    }
    return caught ? 0 : -1;
}
""",
        tests=r"""
CLINGS_CHECK_INT(raise_and_catch(), 0);
""",
        breaks=[
            (
                "caught = 1;",
                "/* TODO: record that the signal was caught. */\n    caught = 0;",
            )
        ],
    ),
]
