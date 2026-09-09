"""Additional exercises covering common C pitfalls."""

from spec import ex, project

SPECS = [
    ex(
        topic="02_operators",
        slug="08_assignment_vs_equality",
        title="Assignment versus equality",
        objective="Use == for comparison and recognize the = versus == trap.",
        reference="",
        hint="A single = assigns; a double == compares.",
        code=r"""
int is_equal(int left, int right)
{
    return left == right;
}

int compare_with_zero(int value)
{
    if (value == 0) {
        return 1;
    }
    return 0;
}
""",
        tests=r"""
CLINGS_CHECK_INT(is_equal(1, 1), 1);
CLINGS_CHECK_INT(is_equal(1, 2), 0);
CLINGS_CHECK_INT(compare_with_zero(0), 1);
CLINGS_CHECK_INT(compare_with_zero(5), 0);
""",
        breaks=[
            (
                "return left == right;",
                "/* TODO: compare instead of assign. */\n    return left = right;",
            )
        ],
    ),
    ex(
        topic="02_operators",
        slug="09_maximal_munch",
        title="Lexical maximal munch",
        objective="Understand how the lexer greedily forms the longest token.",
        reference="",
        hint="a+++b is tokenized as (a++) + b.",
        code=r"""
int greedy_expression(int left, int right)
{
    return left+++right;
}

int comment_expression(void)
{
    return 1 /* comment */ + 2;
}
""",
        tests=r"""
CLINGS_CHECK_INT(greedy_expression(1, 2), 3);
CLINGS_CHECK_INT(comment_expression(), 3);
""",
        breaks=[
            (
                "return left+++right;",
                "/* TODO: preserve the maximal-munch tokenization. */\n    return left + ++right;",
            )
        ],
    ),
    ex(
        topic="01_types_variables",
        slug="10_octal_constants",
        title="Octal integer constants",
        objective="Recognize that a leading zero means base 8.",
        reference="",
        hint="010 is 8, not 10; 0195 is not a valid C integer constant.",
        code=r"""
#include <stdlib.h>

int octal_constant(void)
{
    return 010;
}

int parse_c_integer(const char *text, int *out)
{
    char *end = NULL;
    long value = strtol(text, &end, 0);
    if (end == text || *end != '\0') {
        return -1;
    }
    *out = (int)value;
    return 0;
}
""",
        tests=r"""
int value = 0;

CLINGS_CHECK_INT(octal_constant(), 8);
CLINGS_CHECK_INT(parse_c_integer("010", &value), 0);
CLINGS_CHECK_INT(value, 8);
CLINGS_CHECK_INT(parse_c_integer("10", &value), 0);
CLINGS_CHECK_INT(value, 10);
CLINGS_CHECK_INT(parse_c_integer("0195", &value), -1);
""",
        breaks=[
            (
                "return 010;",
                "/* TODO: return the octal constant 010. */\n    return 10;",
            )
        ],
    ),
    ex(
        topic="03_control_flow",
        slug="08_semicolon_pitfalls",
        title="Semicolon and empty-statement traps",
        objective="Avoid accidentally ending an if or loop with a semicolon.",
        reference="",
        hint="A semicolon after if creates an empty body.",
        code=r"""
int count_nonzero(const int *values, int count)
{
    int nonzero = 0;
    for (int i = 0; i < count; ++i) {
        if (values[i] != 0) {
            ++nonzero;
        }
    }
    return nonzero;
}
""",
        tests=r"""
const int values[] = {0, 1, 2};
const int zeros[] = {0, 0, 0};

CLINGS_CHECK_INT(count_nonzero(values, 3), 2);
CLINGS_CHECK_INT(count_nonzero(zeros, 3), 0);
""",
        breaks=[
            (
                "if (values[i] != 0) {\n            ++nonzero;\n        }",
                "if (values[i] != 0);\n        {\n            ++nonzero;\n        }",
            )
        ],
    ),
    ex(
        topic="03_control_flow",
        slug="09_dangling_else",
        title="Dangling else",
        objective="Use braces to make else bind to the intended if.",
        reference="",
        hint="Without braces, else binds to the nearest unmatched if.",
        code=r"""
int classify(int x, int y)
{
    if (x > 0) {
        if (y > 0) {
            return 1;
        }
    } else {
        return 2;
    }
    return 0;
}
""",
        tests=r"""
CLINGS_CHECK_INT(classify(1, 1), 1);
CLINGS_CHECK_INT(classify(1, -1), 0);
CLINGS_CHECK_INT(classify(-1, 1), 2);
""",
        breaks=[
            (
                "if (x > 0) {\n        if (y > 0) {\n            return 1;\n        }\n    } else {\n        return 2;\n    }",
                "if (x > 0)\n        if (y > 0)\n            return 1;\n    else\n        return 2;",
            )
        ],
    ),
    ex(
        topic="06_pointers",
        slug="08_null_empty_string",
        title="NULL, empty string, and NUL",
        objective="Distinguish a null pointer, an empty string, and the NUL character.",
        reference="",
        hint="NULL is a null pointer; \"\" is a valid empty string; '\\0' is NUL.",
        code=r"""
#include <stddef.h>
#include <string.h>

int length_or_zero(const char *text)
{
    return text == NULL ? 0 : (int)strlen(text);
}

int is_empty_string(const char *text)
{
    return text != NULL && text[0] == '\0';
}
""",
        tests=r"""
CLINGS_CHECK_INT(length_or_zero(NULL), 0);
CLINGS_CHECK_INT(length_or_zero(""), 0);
CLINGS_CHECK_INT(is_empty_string(""), 1);
CLINGS_CHECK_INT(is_empty_string(NULL), 0);
""",
        breaks=[
            (
                "return text == NULL ? 0 : (int)strlen(text);",
                "/* TODO: treat NULL as an empty input. */\n    return text == NULL ? -1 : (int)strlen(text);",
            )
        ],
    ),
    ex(
        topic="05_arrays_strings",
        slug="11_asymmetric_bounds",
        title="Asymmetric bounds",
        objective="Use the half-open interval [low, high).",
        reference="",
        hint="The upper bound is exclusive: value < high.",
        code=r"""
int in_range(int value, int low, int high)
{
    return value >= low && value < high;
}

int range_length(int low, int high)
{
    return high - low;
}

int loop_count(int low, int high)
{
    int count = 0;
    for (int value = low; value < high; ++value) {
        ++count;
    }
    return count;
}
""",
        tests=r"""
CLINGS_CHECK_INT(in_range(4, 0, 5), 1);
CLINGS_CHECK_INT(in_range(5, 0, 5), 0);
CLINGS_CHECK_INT(range_length(0, 5), 5);
CLINGS_CHECK_INT(loop_count(0, 5), 5);
""",
        breaks=[
            (
                "return value >= low && value < high;",
                "/* TODO: make the upper bound exclusive. */\n    return value >= low && value <= high;",
            )
        ],
    ),
    ex(
        topic="00_getting_started",
        slug="07_main_return_value",
        title="main return values",
        objective="Return a defined success or failure status from a program.",
        reference="",
        hint="EXIT_SUCCESS is 0 on hosted implementations; EXIT_FAILURE is nonzero.",
        code=r"""
#include <stdlib.h>

int exit_code_for(int success)
{
    return success ? EXIT_SUCCESS : EXIT_FAILURE;
}
""",
        tests=r"""
CLINGS_CHECK_INT(exit_code_for(1), EXIT_SUCCESS);
CLINGS_CHECK_INT(exit_code_for(0), EXIT_FAILURE);
""",
        breaks=[
            (
                "return success ? EXIT_SUCCESS : EXIT_FAILURE;",
                "/* TODO: return success for success and failure otherwise. */\n    return success ? EXIT_FAILURE : EXIT_SUCCESS;",
            )
        ],
    ),
    project(
        topic="13_translation_units",
        slug="04_external_type_check",
        title="External type checking",
        objective="Keep declarations and definitions consistent across translation units.",
        reference="",
        hint="The linker does not compare the types of extern declarations.",
        files={
            "value.h": r"""
#ifndef VALUE_H
#define VALUE_H

extern double shared_value;

#endif
""",
            "value.c": r"""
#include "value.h"

double shared_value = 3.5;
""",
            "main.c": r"""
#include "clings/test.h"
#include "value.h"

int main(void)
{
    CLINGS_CHECK_INT(shared_value == 3.5, 1);
    return clings_report();
}
""",
        },
        file_breaks=[
            (
                "value.h",
                "extern double shared_value;",
                "/* TODO: match the type in value.c. */\nextern int shared_value;",
            )
        ],
    ),
    ex(
        topic="09_preprocessor",
        slug="11_macro_whitespace",
        title="Whitespace in macro definitions",
        objective="Remember that a space can turn a function-like macro into an object-like macro.",
        reference="",
        hint="The ( must immediately follow the macro name.",
        code=r"""
#define SQUARE(value) ((value) * (value))

int square_value(int value)
{
    return SQUARE(value);
}
""",
        tests=r"""
CLINGS_CHECK_INT(square_value(4), 16);
CLINGS_CHECK_INT(SQUARE(3), 9);
""",
        breaks=[
            (
                "#define SQUARE(value) ((value) * (value))",
                "/* TODO: keep the ( immediately after SQUARE. */\n#define SQUARE (value) ((value) * (value))",
            )
        ],
        compile_fail=True,
    ),
    ex(
        topic="09_preprocessor",
        slug="12_macro_statement",
        title="Macros are not statements",
        objective="Use do { ... } while (0) for a statement-like macro.",
        reference="",
        hint="A bare block macro breaks if/else syntax.",
        code=r"""
#define SET_ZERO(pointer) do { *(pointer) = 0; } while (0)

void set_if_positive(int *pointer, int condition)
{
    if (condition)
        SET_ZERO(pointer);
    else
        *pointer = 1;
}
""",
        tests=r"""
int value = 5;

set_if_positive(&value, 1);
CLINGS_CHECK_INT(value, 0);
value = 5;
set_if_positive(&value, 0);
CLINGS_CHECK_INT(value, 1);
""",
        breaks=[
            (
                "#define SET_ZERO(pointer) do { *(pointer) = 0; } while (0)",
                "/* TODO: make the macro behave like a single statement. */\n#define SET_ZERO(pointer) { *(pointer) = 0; }",
            )
        ],
        compile_fail=True,
    ),
    ex(
        topic="09_preprocessor",
        slug="13_macro_not_typedef",
        title="Macros are not type definitions",
        objective="Use typedef instead of an object-like macro for pointer types.",
        reference="",
        hint="INT_POINTER a, b declares b as int, not int *.",
        code=r"""
#include <stddef.h>

typedef int *int_pointer;
#define INT_POINTER int *

int_pointer first = NULL;
int_pointer second = NULL;
""",
        tests=r"""
CLINGS_CHECK_INT((int)sizeof first, (int)sizeof(int *));
CLINGS_CHECK_INT((int)sizeof second, (int)sizeof(int *));
""",
        breaks=[
            (
                "int_pointer first = NULL;\nint_pointer second = NULL;",
                "/* TODO: use the typedef for both declarations. */\nINT_POINTER first = NULL, second = NULL;",
            )
        ],
    ),
    ex(
        topic="01_types_variables",
        slug="11_char_signedness",
        title="char signedness",
        objective="Use signed char and unsigned char explicitly when the sign matters.",
        reference="",
        hint="Plain char may be signed or unsigned; signed char and unsigned char are explicit.",
        code=r"""
int signed_char_value(signed char value)
{
    return value;
}

int unsigned_char_value(unsigned char value)
{
    return value;
}
""",
        tests=r"""
CLINGS_CHECK_INT(signed_char_value((signed char)0xFF), -1);
CLINGS_CHECK_INT(unsigned_char_value((unsigned char)0xFF), 255);
""",
        breaks=[
            (
                "int signed_char_value(signed char value)\n{\n    return value;\n}",
                "int signed_char_value(signed char value)\n{\n    /* TODO: preserve the signed value. */\n    return (int)(unsigned char)value;\n}",
            )
        ],
    ),
    ex(
        topic="06_pointers",
        slug="09_memory_location_zero",
        title="Memory location zero",
        objective="Treat address zero as a null pointer, not as a valid object address.",
        reference="",
        hint="NULL is the portable null pointer constant.",
        code=r"""
#include <stddef.h>

int pointer_is_null(const void *pointer)
{
    return pointer == NULL;
}

int null_is_zero(void)
{
    return NULL == 0;
}
""",
        tests=r"""
int value = 1;

CLINGS_CHECK_INT(pointer_is_null(NULL), 1);
CLINGS_CHECK_INT(pointer_is_null(&value), 0);
CLINGS_CHECK_INT(null_is_zero(), 1);
""",
        breaks=[
            (
                "return pointer == NULL;",
                "/* TODO: compare against the null pointer. */\n    return pointer == (void *)0x1;",
            )
        ],
    ),
    ex(
        topic="06_pointers",
        slug="10_one_past_pointer",
        title="One-past pointer arithmetic",
        objective="Do not treat a pointer to a single object as an array.",
        reference="",
        hint="For a single object, only the one-past pointer is valid; do not dereference it.",
        code=r"""
int one_past_offset(void)
{
    int value = 42;
    int *pointer = &value;
    int *one_past = pointer + 1;
    return (int)(one_past - pointer);
}

int single_object_value(void)
{
    int value = 42;
    int *pointer = &value;
    return *pointer;
}
""",
        tests=r"""
CLINGS_CHECK_INT(one_past_offset(), 1);
CLINGS_CHECK_INT(single_object_value(), 42);
""",
        breaks=[
            (
                "return (int)(one_past - pointer);",
                "/* TODO: only one-past is valid for a single object. */\n    return (int)(one_past - pointer + 1);",
            )
        ],
    ),
    ex(
        topic="10_stdlib_io",
        slug="16_rand_max",
        title="RAND_MAX portability",
        objective="Do not assume rand() returns a value below a fixed small bound.",
        reference="",
        hint="The C standard only guarantees RAND_MAX >= 32767.",
        code=r"""
#include <stdlib.h>

int rand_max_is_at_least_32767(void)
{
    return RAND_MAX >= 32767;
}

int bounded_rand(int upper)
{
    return upper > 0 ? rand() % upper : 0;
}
""",
        tests=r"""
CLINGS_CHECK_INT(rand_max_is_at_least_32767(), 1);
srand(42u);
int value = bounded_rand(10);
CLINGS_CHECK(value >= 0 && value < 10);
""",
        breaks=[
            (
                "return RAND_MAX >= 32767;",
                "/* TODO: use the standard minimum guarantee. */\n    return RAND_MAX == 32767;",
            )
        ],
    ),
    ex(
        topic="07_dynamic_memory",
        slug="08_free_then_realloc",
        title="Free then realloc",
        objective="Use realloc directly instead of freeing before growing an allocation.",
        reference="",
        hint="free(values) followed by realloc(values, ...) uses a dangling pointer.",
        code=r"""
#include <stdlib.h>
#include <string.h>

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
                "int *grown = realloc(values, new_count * sizeof *grown);",
                "/* TODO: grow without freeing the original block first. */\n    free(values);\n    int *grown = malloc(new_count * sizeof *grown);\n    if (grown != NULL) {\n        memset(grown, 0, new_count * sizeof *grown);\n    }",
            )
        ],
    ),
    ex(
        topic="00_getting_started",
        slug="08_standard_changes",
        title="C standard changes",
        objective="Detect the C standard version at compile time.",
        reference="",
        hint="__STDC_VERSION__ is 201112L for C11 and 201710L for C17.",
        code=r"""
int c_standard_year(void)
{
    return (int)(__STDC_VERSION__ / 100L);
}

int has_c11(void)
{
#if defined(__STDC_VERSION__) && __STDC_VERSION__ >= 201112L
    return 1;
#else
    return 0;
#endif
}
""",
        tests=r"""
CLINGS_CHECK(c_standard_year() >= 2011);
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
        topic="00_getting_started",
        slug="09_identifier_length",
        title="Identifier length",
        objective="Use long internal identifiers and rely on the standard minimum.",
        reference="",
        hint="Modern C guarantees at least 31 significant external and 63 internal identifier characters.",
        code=r"""
static int this_is_a_very_long_internal_identifier_name_for_c_traps(void)
{
    return 42;
}

int long_identifier_value(void)
{
    return this_is_a_very_long_internal_identifier_name_for_c_traps();
}
""",
        tests=r"""
CLINGS_CHECK_INT(long_identifier_value(), 42);
""",
        breaks=[
            (
                "return 42;",
                "/* TODO: return the long-identifier value. */\n    return 0;",
            )
        ],
    ),
    ex(
        topic="14_character_io",
        slug="05_getchar_putchar",
        title="getchar and putchar",
        objective="Use the standard input/output character macros directly.",
        reference="",
        hint="ungetc can push a character back onto stdin for a test.",
        code=r"""
#include <stdio.h>

int read_one_character(void)
{
    return getchar();
}

int write_one_character(int character)
{
    return putchar(character);
}
""",
        tests=r"""
CLINGS_CHECK_INT(ungetc('x', stdin), 'x');
CLINGS_CHECK_INT(read_one_character(), 'x');
CLINGS_CHECK_INT(write_one_character('y'), 'y');
""",
        breaks=[
            (
                "return getchar();",
                "/* TODO: read one character from stdin. */\n    return 'z';",
            )
        ],
    ),
    ex(
        topic="18_file_io_advanced",
        slug="07_buffered_output_memory",
        title="Buffered output and memory allocation",
        objective="Combine malloc, setvbuf, output, fclose, and free.",
        reference="",
        hint="The buffer passed to setvbuf must remain valid until the stream is closed.",
        code=r"""
#include <stdio.h>
#include <stdlib.h>

int write_with_buffer(const char *path, const char *text, size_t size)
{
    FILE *file = fopen(path, "w");
    if (file == NULL) {
        return -1;
    }
    char *buffer = malloc(size);
    if (buffer == NULL) {
        fclose(file);
        return -1;
    }
    if (setvbuf(file, buffer, _IOFBF, size) != 0) {
        free(buffer);
        fclose(file);
        return -1;
    }
    int ok = fputs(text, file) >= 0;
    if (fclose(file) != 0) {
        ok = 0;
    }
    free(buffer);
    return ok ? 0 : -1;
}
""",
        tests=r"""
const char *path = "/tmp/clings_buffered_output.txt";
char buffer[32];

CLINGS_CHECK_INT(write_with_buffer(path, "buffered", 128), 0);
FILE *file = fopen(path, "r");
CLINGS_CHECK(file != NULL);
CLINGS_CHECK(fgets(buffer, sizeof buffer, file) != NULL);
CLINGS_CHECK_STR(buffer, "buffered");
fclose(file);
remove(path);
""",
        breaks=[
            (
                "int ok = fputs(text, file) >= 0;",
                '/* TODO: write the supplied text. */\n    int ok = fputs("wrong", file) >= 0;',
            )
        ],
    ),
]
