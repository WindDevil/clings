"""Additional exercises that extend existing topics."""

from spec import ex

SPECS = [
    ex(
        topic="03_types_variables",
        slug="09_long_double",
        title="long double",
        objective="Use long double and compare its precision with double.",
        reference="",
        hint="Use the L suffix for long double constants.",
        code=r"""
#include <float.h>

long double long_double_average(long double left, long double right)
{
    return (left + right) / 2.0L;
}

int long_double_has_extra_precision(void)
{
    return LDBL_DIG >= DBL_DIG ? 1 : 0;
}
""",
        tests=r"""
CLINGS_CHECK_INT(long_double_average(1.5L, 2.5L) == 2.0L, 1);
CLINGS_CHECK_INT(long_double_has_extra_precision(), 1);
""",
        breaks=[
            (
                "return (left + right) / 2.0L;",
                "/* TODO: compute the average as a long double. */\n    return left + right;",
            )
        ],
    ),
    ex(
        topic="04_operators",
        slug="07_compound_assignment",
        title="Compound assignment and comma",
        objective="Use +=, -=, *=, /=, %= and the comma operator.",
        reference="",
        hint="The comma operator evaluates left to right and yields the right operand.",
        code=r"""
int compound_demo(int value)
{
    value += 3;
    value *= 2;
    value -= 1;
    value /= 2;
    value %= 5;
    return value;
}

int comma_sum(int left, int right)
{
    int sum = 0;
    sum = (left++, right++, left + right);
    return sum;
}
""",
        tests=r"""
CLINGS_CHECK_INT(compound_demo(1), 3);
CLINGS_CHECK_INT(comma_sum(2, 3), 7);
""",
        breaks=[
            (
                "value *= 2;",
                "/* TODO: multiply value by 2. */\n    value += 2;",
            )
        ],
    ),
    ex(
        topic="05_control_flow",
        slug="07_while_do_while",
        title="while and do-while",
        objective="Distinguish entry-condition and exit-condition loops.",
        reference="",
        hint="A do-while body always executes at least once.",
        code=r"""
int sum_while(int limit)
{
    int sum = 0;
    int value = 1;
    while (value <= limit) {
        sum += value;
        ++value;
    }
    return sum;
}

int count_do_while(int limit)
{
    int count = 0;
    do {
        ++count;
    } while (count < limit);
    return count;
}
""",
        tests=r"""
CLINGS_CHECK_INT(sum_while(0), 0);
CLINGS_CHECK_INT(sum_while(5), 15);
CLINGS_CHECK_INT(count_do_while(0), 1);
CLINGS_CHECK_INT(count_do_while(3), 3);
""",
        breaks=[
            (
                "do {\n        ++count;\n    } while (count < limit);",
                "/* TODO: use an exit-condition loop. */\n    while (count < limit) {\n        ++count;\n    }",
            )
        ],
    ),
    ex(
        topic="06_functions",
        slug="08_tail_recursion",
        title="Tail recursion",
        objective="Rewrite a recursive sum using an accumulator.",
        reference="",
        hint="The recursive call should be the last operation.",
        code=r"""
static int sum_tail(int value, int accumulator)
{
    return value == 0 ? accumulator : sum_tail(value - 1, accumulator + value);
}

int sum_tail_wrapper(int value)
{
    return sum_tail(value, 0);
}
""",
        tests=r"""
CLINGS_CHECK_INT(sum_tail_wrapper(0), 0);
CLINGS_CHECK_INT(sum_tail_wrapper(5), 15);
CLINGS_CHECK_INT(sum_tail_wrapper(10), 55);
""",
        breaks=[
            (
                "sum_tail(value - 1, accumulator + value)",
                "/* TODO: add the current value to the accumulator. */\n        sum_tail(value - 1, accumulator)",
            )
        ],
    ),
    ex(
        topic="08_arrays_strings",
        slug="07_vla",
        title="Variable-length arrays",
        objective="Create an array whose length is a runtime value.",
        reference="",
        hint="A VLA is declared with a runtime expression: int values[n].",
        code=r"""
int sum_vla(int count)
{
    int values[count];
    for (int i = 0; i < count; ++i) {
        values[i] = i + 1;
    }
    int sum = 0;
    for (int i = 0; i < count; ++i) {
        sum += values[i];
    }
    return sum;
}
""",
        tests=r"""
CLINGS_CHECK_INT(sum_vla(1), 1);
CLINGS_CHECK_INT(sum_vla(4), 10);
CLINGS_CHECK_INT(sum_vla(10), 55);
""",
        breaks=[
            (
                "values[i] = i + 1;",
                "/* TODO: initialize the VLA element. */\n        values[i] = 1;",
            )
        ],
    ),
    ex(
        topic="08_arrays_strings",
        slug="08_compound_literals",
        title="Compound literals",
        objective="Create a temporary struct value with a compound literal.",
        reference="",
        hint="The syntax is (struct point){.x = 3, .y = 4}.",
        code=r"""
struct point {
    int x;
    int y;
};

int point_sum(struct point point)
{
    return point.x + point.y;
}

int compound_literal_sum(void)
{
    return point_sum((struct point){.x = 3, .y = 4});
}
""",
        tests=r"""
CLINGS_CHECK_INT(compound_literal_sum(), 7);
CLINGS_CHECK_INT(point_sum((struct point){1, 2}), 3);
""",
        breaks=[
            (
                "point_sum((struct point){.x = 3, .y = 4})",
                "/* TODO: build the compound literal with y = 4. */\n    point_sum((struct point){.x = 3, .y = 0})",
            )
        ],
    ),
    ex(
        topic="08_arrays_strings",
        slug="09_pointer_compatibility",
        title="Pointer compatibility and const",
        objective="Pass a non-const array through a pointer-to-const.",
        reference="",
        hint="A pointer to const may point at non-const data.",
        code=r"""
#include <stddef.h>

int sum_const(const int *values, size_t count)
{
    int sum = 0;
    for (size_t i = 0; i < count; ++i) {
        sum += values[i];
    }
    return sum;
}

int pointer_compatibility(void)
{
    int values[3] = {1, 2, 3};
    const int *pointer = values;
    return sum_const(pointer, 3);
}
""",
        tests=r"""
const int const_values[3] = {4, 5, 6};

CLINGS_CHECK_INT(pointer_compatibility(), 6);
CLINGS_CHECK_INT(sum_const(const_values, 3), 15);
""",
        breaks=[
            (
                "return sum_const(pointer, 3);",
                "/* TODO: pass the full length through the const pointer. */\n    return sum_const(pointer, 2);",
            )
        ],
    ),
    ex(
        topic="10_aggregates",
        slug="09_struct_array",
        title="Arrays of structs",
        objective="Traverse an array of structs and find the best element.",
        reference="",
        hint="Use students[i].score for each element.",
        code=r"""
#include <stddef.h>

struct student {
    char name[16];
    int score;
};

int total_score(const struct student *students, size_t count)
{
    int total = 0;
    for (size_t i = 0; i < count; ++i) {
        total += students[i].score;
    }
    return total;
}

const struct student *best_student(const struct student *students, size_t count)
{
    const struct student *best = &students[0];
    for (size_t i = 1; i < count; ++i) {
        if (students[i].score > best->score) {
            best = &students[i];
        }
    }
    return best;
}
""",
        tests=r"""
const struct student students[3] = {
    {"Ada", 91},
    {"Linus", 88},
    {"Grace", 95},
};

CLINGS_CHECK_INT(total_score(students, 3), 274);
CLINGS_CHECK_STR(best_student(students, 3)->name, "Grace");
""",
        breaks=[
            (
                "total += students[i].score;",
                "/* TODO: add the current student's score. */\n        total += students[0].score;",
            )
        ],
    ),
    ex(
        topic="10_aggregates",
        slug="10_struct_pass",
        title="Passing structs by value and by pointer",
        objective="Compare struct value parameters with struct pointer parameters.",
        reference="",
        hint="A struct pointer can modify the caller's struct.",
        code=r"""
struct point {
    int x;
    int y;
};

int point_sum_by_value(struct point point)
{
    return point.x + point.y;
}

void point_shift_by_pointer(struct point *point, int dx, int dy)
{
    point->x += dx;
    point->y += dy;
}
""",
        tests=r"""
struct point point = {3, 4};

CLINGS_CHECK_INT(point_sum_by_value(point), 7);
point_shift_by_pointer(&point, 10, -2);
CLINGS_CHECK_INT(point.x, 13);
CLINGS_CHECK_INT(point.y, 2);
""",
        breaks=[
            (
                "point->x += dx;",
                "/* TODO: shift the x coordinate by dx. */\n    point->x += 0;",
            )
        ],
    ),
    ex(
        topic="10_aggregates",
        slug="11_struct_file",
        title="Writing and reading structs",
        objective="Store a struct with fwrite and read it back with fread.",
        reference="",
        hint="Use binary mode and compare the number of complete items written.",
        code=r"""
#include <stdio.h>

struct record {
    int id;
    double value;
};

int write_record(const char *path, const struct record *record)
{
    FILE *file = fopen(path, "wb");
    if (file == NULL) {
        return -1;
    }
    size_t written = fwrite(record, sizeof *record, 1, file);
    if (fclose(file) != 0) {
        return -1;
    }
    return written == 1 ? 0 : -1;
}

int read_record(const char *path, struct record *record)
{
    FILE *file = fopen(path, "rb");
    if (file == NULL) {
        return -1;
    }
    size_t read_count = fread(record, sizeof *record, 1, file);
    fclose(file);
    return read_count == 1 ? 0 : -1;
}
""",
        tests=r"""
const char *path = "/tmp/clings_struct_file_test.bin";
struct record written = {.id = 7, .value = 3.5};
struct record read_back = {0};

CLINGS_CHECK_INT(write_record(path, &written), 0);
CLINGS_CHECK_INT(read_record(path, &read_back), 0);
CLINGS_CHECK_INT(read_back.id, 7);
CLINGS_CHECK_INT(read_back.value == 3.5, 1);
remove(path);
""",
        breaks=[
            (
                "size_t written = fwrite(record, sizeof *record, 1, file);",
                "/* TODO: write one complete record. */\n    size_t written = fwrite(record, 1, sizeof *record, file);",
            )
        ],
    ),
    ex(
        topic="10_aggregates",
        slug="12_complex_declarations",
        title="Complex declarations and function-pointer tables",
        objective="Read and use a typedef for a function pointer and an array of function pointers.",
        reference="",
        hint="binary_operation is a typedef for int (*)(int, int).",
        code=r"""
typedef int (*binary_operation)(int, int);

static int add(int left, int right)
{
    return left + right;
}

static int subtract(int left, int right)
{
    return left - right;
}

int apply_operation(binary_operation operation, int left, int right)
{
    return operation(left, right);
}

int use_operation_table(void)
{
    binary_operation table[2] = {add, subtract};
    return apply_operation(table[1], 10, 3);
}
""",
        tests=r"""
CLINGS_CHECK_INT(apply_operation(add, 2, 3), 5);
CLINGS_CHECK_INT(use_operation_table(), 7);
""",
        breaks=[
            (
                "return operation(left, right);",
                "/* TODO: call the selected operation. */\n    return add(left, right);",
            )
        ],
    ),
    ex(
        topic="01_preprocessor",
        slug="06_undef_defined",
        title="#undef and defined",
        objective="Undefine a macro and test it with defined().",
        reference="",
        hint="#undef removes the macro before the second #if.",
        code=r"""
#define CLINGS_FEATURE 1

#if defined(CLINGS_FEATURE)
#define CLINGS_FEATURE_STATE 1
#else
#define CLINGS_FEATURE_STATE 0
#endif

#undef CLINGS_FEATURE

#ifdef CLINGS_FEATURE
#define CLINGS_AFTER_UNDEF 1
#else
#define CLINGS_AFTER_UNDEF 0
#endif

int feature_state(void)
{
    return CLINGS_FEATURE_STATE;
}

int after_undef(void)
{
    return CLINGS_AFTER_UNDEF;
}
""",
        tests=r"""
CLINGS_CHECK_INT(feature_state(), 1);
CLINGS_CHECK_INT(after_undef(), 0);
""",
        breaks=[
            (
                "#undef CLINGS_FEATURE",
                "/* TODO: remove CLINGS_FEATURE before the second test. */",
            )
        ],
    ),
    ex(
        topic="12_standard_library",
        slug="12_printf_advanced",
        title="Advanced printf formatting",
        objective="Use width, zero padding, precision, and the * width argument.",
        reference="",
        hint="%08d zero-pads to width 8; %.3f uses three fractional digits.",
        code=r"""
#include <stdio.h>

int format_width(char *buffer, size_t size, int value)
{
    return snprintf(buffer, size, "%08d", value);
}

int format_precision(char *buffer, size_t size, double value)
{
    return snprintf(buffer, size, "%.3f", value);
}

int format_star(char *buffer, size_t size, int width, int value)
{
    return snprintf(buffer, size, "%*d", width, value);
}
""",
        tests=r"""
char buffer[32];

CLINGS_CHECK_INT(format_width(buffer, sizeof buffer, 42), 8);
CLINGS_CHECK_STR(buffer, "00000042");
CLINGS_CHECK_INT(format_precision(buffer, sizeof buffer, 3.14159), 5);
CLINGS_CHECK_STR(buffer, "3.142");
CLINGS_CHECK_INT(format_star(buffer, sizeof buffer, 5, 42), 5);
CLINGS_CHECK_STR(buffer, "   42");
""",
        breaks=[
            (
                'return snprintf(buffer, size, "%08d", value);',
                '/* TODO: zero-pad the value to width 8. */\n    return snprintf(buffer, size, "%d", value);',
            )
        ],
    ),
    ex(
        topic="12_standard_library",
        slug="13_scanf_advanced",
        title="Advanced scanf input",
        objective="Use field width and a scanset in sscanf.",
        reference="",
        hint="%3d reads at most three digits; %[abc] reads only a, b, and c.",
        code=r"""
#include <stdio.h>

int parse_field(const char *input, int *out)
{
    return sscanf(input, "%3d", out) == 1 ? 0 : -1;
}

int parse_set(const char *input, char *out, size_t size)
{
    if (size == 0) {
        return -1;
    }
    out[0] = '\0';
    return sscanf(input, "%[abc]", out) == 1 ? 0 : -1;
}
""",
        tests=r"""
int value = 0;
char buffer[16];

CLINGS_CHECK_INT(parse_field("12345", &value), 0);
CLINGS_CHECK_INT(value, 123);
CLINGS_CHECK_INT(parse_set("abcxyz", buffer, sizeof buffer), 0);
CLINGS_CHECK_STR(buffer, "abc");
CLINGS_CHECK_INT(parse_set("xyz", buffer, sizeof buffer), -1);
""",
        breaks=[
            (
                'return sscanf(input, "%3d", out) == 1 ? 0 : -1;',
                '/* TODO: read at most three digits. */\n    return sscanf(input, "%d", out) == 1 ? 0 : -1;',
            )
        ],
    ),
    ex(
        topic="12_standard_library",
        slug="14_ctype_full",
        title="ctype.h classification and conversion",
        objective="Use isalnum and toupper with unsigned char casts.",
        reference="",
        hint="Pass (unsigned char) to ctype functions to avoid negative arguments.",
        code=r"""
#include <ctype.h>

int count_alnum(const char *text)
{
    int count = 0;
    for (const char *pointer = text; *pointer != '\0'; ++pointer) {
        if (isalnum((unsigned char)*pointer)) {
            ++count;
        }
    }
    return count;
}

char upper_char(char character)
{
    return (char)toupper((unsigned char)character);
}
""",
        tests=r"""
CLINGS_CHECK_INT(count_alnum("a1 B2!"), 4);
CLINGS_CHECK_INT(upper_char('q'), 'Q');
CLINGS_CHECK_INT(upper_char('Z'), 'Z');
""",
        breaks=[
            (
                "if (isalnum((unsigned char)*pointer)) {",
                "/* TODO: classify letters and digits. */\n        if (isalpha((unsigned char)*pointer)) {",
            )
        ],
    ),
]
