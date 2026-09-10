"""Exercise specifications for topics 00 through 04."""

from spec import ex

SPECS = [
    # ------------------------------------------------------------------
    # 00_getting_started
    # ------------------------------------------------------------------
    ex(
        topic="00_basics",
        slug="01_printf",
        title="Print with printf",
        objective="Use printf to print a line of text.",
        reference="",
        hint="printf returns the number of characters printed, including the newline.",
        code=r"""
#include <stdio.h>

int print_greeting(void)
{
    return printf("Hello, C!\n");
}
""",
        tests=r"""
CLINGS_CHECK_INT(print_greeting(), 10);
""",
        breaks=[
            (
                'return printf("Hello, C!\\n");',
                '/* TODO: print Hello, C! followed by a newline. */\n    return printf("Hello, world!\\n");',
            )
        ],
    ),
    ex(
        topic="00_basics",
        slug="02_printf_values",
        title="Print a value",
        objective="Use printf with %d to print an integer value.",
        reference="",
        hint="Use %d for an int argument and include the newline in the format string.",
        code=r"""
#include <stdio.h>

int print_value(int value)
{
    return printf("%d\n", value);
}
""",
        tests=r"""
CLINGS_CHECK_INT(print_value(42), 3);
""",
        breaks=[
            (
                'return printf("%d\\n", value);',
                '/* TODO: print the integer value. */\n    return printf("value\\n");',
            )
        ],
    ),
    ex(
        topic="00_basics",
        slug="03_scanf",
        title="Read with scanf",
        objective="Read an integer from stdin with scanf.",
        reference="",
        hint="scanf needs the address of the variable: &value.",
        code=r"""
#include <stdio.h>

int read_number(void)
{
    int value = 0;
    if (scanf("%d", &value) != 1) {
        return -1;
    }
    return value;
}
""",
        tests=r"""
const char *valid_path = "/tmp/clings_scanf_valid.txt";
const char *invalid_path = "/tmp/clings_scanf_invalid.txt";

FILE *file = fopen(valid_path, "w");
CLINGS_CHECK(file != NULL);
fputs("42", file);
fclose(file);
CLINGS_CHECK(freopen(valid_path, "r", stdin) != NULL);
CLINGS_CHECK_INT(read_number(), 42);

file = fopen(invalid_path, "w");
CLINGS_CHECK(file != NULL);
fputs("abc", file);
fclose(file);
CLINGS_CHECK(freopen(invalid_path, "r", stdin) != NULL);
CLINGS_CHECK_INT(read_number(), -1);

remove(valid_path);
remove(invalid_path);
""",
        breaks=[
            (
                'if (scanf("%d", &value) != 1) {',
                '/* TODO: scanf needs the address of value. */\n    if (scanf("%d", value) != 1) {',
            )
        ],
        compile_fail=True,
    ),
    ex(
        topic="00_basics",
        slug="04_char_array",
        title="Character arrays",
        objective="Store text in a char array and access its characters.",
        reference="",
        hint="Array indexes start at 0; sizeof(\"hello\") includes the terminating NUL.",
        code=r"""
char text[] = "hello";

char first_character(void)
{
    return text[0];
}

char last_character(void)
{
    return text[4];
}
""",
        tests=r"""
CLINGS_CHECK_INT(first_character(), 'h');
CLINGS_CHECK_INT(last_character(), 'o');
""",
        breaks=[
            (
                "return text[4];",
                "/* TODO: return the last visible character, not the NUL terminator. */\n    return text[5];",
            )
        ],
    ),
    ex(
        topic="00_basics",
        slug="05_snprintf",
        title="Safe formatting with snprintf",
        objective="Write formatted text into a fixed-size buffer.",
        reference="",
        hint="snprintf takes the buffer size and returns the number of characters it would write.",
        code=r"""
#include <stdio.h>

char buffer[32];

int format_greeting(void)
{
    return snprintf(buffer, 32, "Hello, %s", "C");
}
""",
        tests=r"""
CLINGS_CHECK_INT(format_greeting(), 8);
CLINGS_CHECK_STR(buffer, "Hello, C");
""",
        breaks=[
            (
                'return snprintf(buffer, 32, "Hello, %s", "C");',
                '/* TODO: format the greeting with the name C. */\n    return snprintf(buffer, 32, "Hello, %s", "world");',
            )
        ],
    ),
    ex(
        topic="00_basics",
        slug="06_sscanf",
        title="Safe parsing with sscanf",
        objective="Parse values from a string with sscanf.",
        reference="",
        hint="The literal comma in the format must match the input string.",
        code=r"""
#include <stdio.h>

int first;
int second;

int parse_pair(void)
{
    return sscanf("3,4", "%d,%d", &first, &second) == 2 ? 0 : -1;
}

int parse_invalid(void)
{
    return sscanf("3 4", "%d,%d", &first, &second) == 2 ? 0 : -1;
}
""",
        tests=r"""
CLINGS_CHECK_INT(parse_pair(), 0);
CLINGS_CHECK_INT(first, 3);
CLINGS_CHECK_INT(second, 4);
CLINGS_CHECK_INT(parse_invalid(), -1);
""",
        breaks=[
            (
                'sscanf("3,4", "%d,%d", &first, &second)',
                '/* TODO: match the comma in the input. */\n    sscanf("3 4", "%d,%d", &first, &second)',
            )
        ],
    ),
    ex(
        topic="00_basics",
        slug="07_include_header",
        title="Include a header",
        objective="Include the standard header that declares toupper.",
        reference="",
        hint="The compiler needs a declaration before use; add the header for character functions.",
        code=r"""
#include <ctype.h>

int uppercase_a(void)
{
    return toupper('a');
}
""",
        tests=r"""
CLINGS_CHECK_INT(uppercase_a(), 'A');
""",
        breaks=[
            (
                "#include <ctype.h>\n\n",
                "/* TODO: include the header that declares toupper. */\n",
            )
        ],
    ),
    ex(
        topic="08_arrays_strings",
        slug="16_main_args",
        title="argc, argv, and the program environment",
        objective="Work with the arguments passed to main.",
        reference="",
        hint="argv[0] is the program name; user arguments start at argv[1].",
        code=r"""
#include <string.h>

int count_user_args(int argc, char **argv)
{
    (void)argv;
    return argc > 0 ? argc - 1 : 0;
}

int find_arg(int argc, char **argv, const char *needle)
{
    for (int i = 1; i < argc; ++i) {
        if (strcmp(argv[i], needle) == 0) {
            return i;
        }
    }
    return -1;
}
""",
        tests=r"""
char *argv[] = {"program", "--verbose", "file.txt", NULL};

CLINGS_CHECK_INT(count_user_args(3, argv), 2);
CLINGS_CHECK_INT(find_arg(3, argv, "--verbose"), 1);
CLINGS_CHECK_INT(find_arg(3, argv, "file.txt"), 2);
CLINGS_CHECK_INT(find_arg(3, argv, "missing"), -1);
""",
        breaks=[
            (
                "for (int i = 1; i < argc; ++i) {",
                "/* TODO: search all user arguments. */\n    for (int i = 1; i < argc - 1; ++i) {",
            )
        ],
    ),
    ex(
        topic="02_macros",
        slug="10_assert_macro",
        title="Assertions and defensive programming",
        objective="Use assert for programmer errors and return values for user errors.",
        reference="",
        hint="A zero denominator is a normal error, so return -1 instead of dividing.",
        code=r"""
#include <assert.h>

int checked_divide(int numerator, int denominator, int *out)
{
    assert(out != NULL);
    if (denominator == 0) {
        return -1;
    }
    *out = numerator / denominator;
    return 0;
}
""",
        tests=r"""
int out = 0;

CLINGS_CHECK_INT(checked_divide(10, 2, &out), 0);
CLINGS_CHECK_INT(out, 5);
CLINGS_CHECK_INT(checked_divide(10, 0, &out), -1);
""",
        breaks=[
            (
                "if (denominator == 0) {\n        return -1;\n    }",
                "if (denominator == 0) {\n        /* TODO: report the error. */\n        return 0;\n    }",
            )
        ],
    ),
    ex(
        topic="00_basics",
        slug="09_compiler_diagnostics",
        title="Read compiler diagnostics",
        objective="Fix a format-string warning that the compiler reports.",
        reference="",
        hint="Use %d to print an int; %s expects a string.",
        code=r"""
#include <stdio.h>

int print_number(int value)
{
    return printf("%d\n", value);
}
""",
        tests=r"""
CLINGS_CHECK_INT(print_number(42), 3);
""",
        breaks=[
            (
                'return printf("%d\\n", value);',
                '/* TODO: use the conversion specifier for an int. */\n    return printf("%s\\n", value);',
            )
        ],
        compile_fail=True,
    ),
    ex(
        topic="00_basics",
        slug="08_lexical_elements",
        title="Comments, line continuation, and escapes",
        objective="Recognize comments, backslash-newline continuation, and escape sequences.",
        reference="",
        hint="The escaped text contains a real newline, a tab, and quotation marks.",
        code=r"""
#include <string.h>

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

    # ------------------------------------------------------------------
    # 01_types_variables
    # ------------------------------------------------------------------
    ex(
        topic="03_types_variables",
        slug="01_integer_types",
        title="Integer types and ranges",
        objective="Use sizeof, CHAR_BIT, INT_MIN, and INT_MAX correctly.",
        reference="",
        hint="The number of bits in an int is sizeof(int) * CHAR_BIT.",
        code=r"""
#include <limits.h>

int int_bits(void)
{
    return (int)(sizeof(int) * CHAR_BIT);
}

int long_can_hold_int(long value)
{
    return value >= INT_MIN && value <= INT_MAX;
}
""",
        tests=r"""
CLINGS_CHECK(int_bits() >= 16);
CLINGS_CHECK_INT(long_can_hold_int(0), 1);
CLINGS_CHECK_INT(long_can_hold_int((long)INT_MAX), 1);
CLINGS_CHECK_INT(long_can_hold_int((long)INT_MAX + 1L), 0);
""",
        breaks=[
            (
                "return (int)(sizeof(int) * CHAR_BIT);",
                "/* TODO: measure the width of int, not char. */\n    return (int)(sizeof(char) * CHAR_BIT);",
            )
        ],
    ),
    ex(
        topic="03_types_variables",
        slug="02_signed_unsigned",
        title="Signed and unsigned conversions",
        objective="Avoid the usual arithmetic conversion trap when comparing.",
        reference="",
        hint="A negative int converted to unsigned becomes a very large value.",
        code=r"""
int compare_int_unsigned(int a, unsigned b)
{
    if (a < 0) {
        return -1;
    }
    if ((unsigned)a < b) {
        return -1;
    }
    if ((unsigned)a > b) {
        return 1;
    }
    return 0;
}
""",
        tests=r"""
CLINGS_CHECK_INT(compare_int_unsigned(-1, 0u), -1);
CLINGS_CHECK_INT(compare_int_unsigned(5, 3u), 1);
CLINGS_CHECK_INT(compare_int_unsigned(3, 3u), 0);
CLINGS_CHECK_INT(compare_int_unsigned(2, 9u), -1);
""",
        breaks=[
            (
                "if (a < 0) {\n        return -1;\n    }",
                "if (a < 0) {\n        /* TODO: negative values are smaller than any unsigned. */\n        return 1;\n    }",
            )
        ],
    ),
    ex(
        topic="03_types_variables",
        slug="03_overflow",
        title="Unsigned wrap and checked signed addition",
        objective="Understand modulo wrap and avoid signed integer overflow.",
        reference="",
        hint="Check INT_MAX - b before adding b to a.",
        code=r"""
#include <limits.h>

unsigned wrap_add(unsigned a, unsigned b)
{
    return a + b;
}

int safe_add_int(int a, int b, int *out)
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

CLINGS_CHECK_INT(wrap_add(UINT_MAX, 1u), 0);
CLINGS_CHECK_INT(safe_add_int(INT_MAX, 1, &out), -1);
CLINGS_CHECK_INT(safe_add_int(INT_MIN, -1, &out), -1);
CLINGS_CHECK_INT(safe_add_int(2, 3, &out), 0);
CLINGS_CHECK_INT(out, 5);
""",
        breaks=[
            (
                "if ((b > 0 && a > INT_MAX - b) || (b < 0 && a < INT_MIN - b)) {",
                "/* TODO: detect overflow before doing the addition. */\n    if (0) {",
            )
        ],
    ),
    ex(
        topic="03_types_variables",
        slug="04_floating_point",
        title="Floating-point comparison",
        objective="Compare floating-point values with an epsilon.",
        reference="",
        hint="Exact equality is usually the wrong comparison for computed doubles.",
        code=r"""
#include <math.h>

int nearly_equal(double a, double b, double epsilon)
{
    return fabs(a - b) <= epsilon;
}
""",
        tests=r"""
CLINGS_CHECK_INT(nearly_equal(0.1 + 0.2, 0.3, 1e-9), 1);
CLINGS_CHECK_INT(nearly_equal(1.0, 1.1, 1e-9), 0);
CLINGS_CHECK_INT(nearly_equal(-1.0, -1.0, 0.0), 1);
""",
        breaks=[
            (
                "return fabs(a - b) <= epsilon;",
                "/* TODO: use an epsilon comparison. */\n    return a == b;",
            )
        ],
    ),
    ex(
        topic="03_types_variables",
        slug="05_char_ascii",
        title="Characters and ASCII",
        objective="Work with char values and the ctype classification functions.",
        reference="",
        hint="Lowercase letters live in a contiguous range only for the execution character set.",
        code=r"""
#include <ctype.h>

int is_ascii_digit(char c)
{
    return c >= '0' && c <= '9';
}

char to_upper_ascii(char c)
{
    return (c >= 'a' && c <= 'z') ? (char)(c - 'a' + 'A') : c;
}
""",
        tests=r"""
CLINGS_CHECK_INT(is_ascii_digit('7'), 1);
CLINGS_CHECK_INT(is_ascii_digit('x'), 0);
CLINGS_CHECK_INT(to_upper_ascii('q'), 'Q');
CLINGS_CHECK_INT(to_upper_ascii('Z'), 'Z');
CLINGS_CHECK_INT(to_upper_ascii('!'), '!');
""",
        breaks=[
            (
                "return (c >= 'a' && c <= 'z') ? (char)(c - 'a' + 'A') : c;",
                "/* TODO: convert lowercase letters to uppercase. */\n    return (c >= 'A' && c <= 'Z') ? (char)(c - 'A' + 'a') : c;",
            )
        ],
    ),
    ex(
        topic="03_types_variables",
        slug="06_storage_scope",
        title="Storage classes and scope",
        objective="Observe the lifetime of a static variable and block scope.",
        reference="",
        hint="++counter increments first; counter++ returns the old value.",
        code=r"""
static int counter = 0;

int next_counter(void)
{
    return ++counter;
}

int local_shadow(int value)
{
    int local_counter = value;
    return local_counter;
}
""",
        tests=r"""
CLINGS_CHECK_INT(next_counter(), 1);
CLINGS_CHECK_INT(next_counter(), 2);
CLINGS_CHECK_INT(local_shadow(99), 99);
CLINGS_CHECK_INT(next_counter(), 3);
""",
        breaks=[
            (
                "return ++counter;",
                "/* TODO: pre-increment the static counter. */\n    return counter++;",
            )
        ],
    ),
    ex(
        topic="03_types_variables",
        slug="07_qualifiers",
        title="Type qualifiers and storage-class specifiers",
        objective="Use const, volatile, restrict, extern, auto, and register.",
        reference="",
        hint="restrict promises that the two pointer parameters do not alias.",
        code=r"""
extern int shared_value;
int shared_value = 42;

int read_const(const int *value)
{
    return *value;
}

int read_volatile(volatile int *value)
{
    return *value;
}

int sum_restrict(const int *restrict left, const int *restrict right)
{
    return *left + *right;
}

int register_sum(void)
{
    register int sum = 0;
    for (register int i = 0; i < 3; ++i) {
        sum += i;
    }
    return sum;
}

int auto_value(void)
{
    auto int value = 5;
    return value;
}
""",
        tests=r"""
int left = 5;
int right = 7;
volatile int volatile_value = 9;

CLINGS_CHECK_INT(shared_value, 42);
CLINGS_CHECK_INT(read_const(&left), 5);
CLINGS_CHECK_INT(read_volatile(&volatile_value), 9);
CLINGS_CHECK_INT(sum_restrict(&left, &right), 12);
CLINGS_CHECK_INT(register_sum(), 3);
CLINGS_CHECK_INT(auto_value(), 5);
""",
        breaks=[
            (
                "return *left + *right;",
                "/* TODO: read both restricted pointers. */\n    return *left;",
            )
        ],
    ),
    ex(
        topic="03_types_variables",
        slug="08_stdbool_stddef",
        title="stdbool.h and stddef.h",
        objective="Use bool and size_t from the standard headers.",
        reference="",
        hint="bool is defined in <stdbool.h>; size_t is defined in <stddef.h>.",
        code=r"""
#include <stdbool.h>
#include <stddef.h>

bool is_even(int value)
{
    return value % 2 == 0;
}

size_t size_of_int(void)
{
    return sizeof(int);
}
""",
        tests=r"""
CLINGS_CHECK_INT(is_even(4), 1);
CLINGS_CHECK_INT(is_even(3), 0);
CLINGS_CHECK_INT(size_of_int(), sizeof(int));
""",
        breaks=[
            (
                "return value % 2 == 0;",
                "/* TODO: return a bool result, not an integer remainder. */\n    return value % 2;",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 02_operators
    # ------------------------------------------------------------------
    ex(
        topic="04_operators",
        slug="01_arithmetic",
        title="Integer arithmetic",
        objective="Practice integer division, modulo, and truncation.",
        reference="",
        hint="Integer division truncates toward zero.",
        code=r"""
int quotient(int a, int b)
{
    return a / b;
}

int int_remainder(int a, int b)
{
    return a % b;
}

int average_floor(int a, int b)
{
    return (a + b) / 2;
}
""",
        tests=r"""
CLINGS_CHECK_INT(quotient(7, 3), 2);
CLINGS_CHECK_INT(quotient(-7, 3), -2);
CLINGS_CHECK_INT(int_remainder(7, 3), 1);
CLINGS_CHECK_INT(average_floor(2, 3), 2);
""",
        breaks=[
            (
                "return a % b;",
                "/* TODO: return the remainder, not the quotient. */\n    return a / b;",
            )
        ],
    ),
    ex(
        topic="04_operators",
        slug="02_precedence",
        title="Precedence and parentheses",
        objective="Use parentheses to express intent clearly.",
        reference="",
        hint="Multiplication binds more tightly than addition.",
        code=r"""
int precedence_demo(int a, int b, int c)
{
    return a + b * c;
}

int parenthesized(int a, int b, int c)
{
    return (a + b) * c;
}
""",
        tests=r"""
CLINGS_CHECK_INT(precedence_demo(2, 3, 4), 14);
CLINGS_CHECK_INT(parenthesized(2, 3, 4), 20);
CLINGS_CHECK_INT(parenthesized(1, 1, 0), 0);
""",
        breaks=[
            (
                "return (a + b) * c;",
                "/* TODO: add parentheses so the sum is multiplied by c. */\n    return a + b * c;",
            )
        ],
    ),
    ex(
        topic="04_operators",
        slug="03_short_circuit",
        title="Short-circuit evaluation",
        objective="Observe that && and || may not evaluate their right operand.",
        reference="",
        hint="The right side of && is only evaluated when the left side is true.",
        code=r"""
static int side_effect_count = 0;

static int touch(void)
{
    ++side_effect_count;
    return 1;
}

int short_circuit_and(int left)
{
    return left && touch();
}

int short_circuit_or(int left)
{
    return left || touch();
}

int touch_count(void)
{
    return side_effect_count;
}
""",
        tests=r"""
CLINGS_CHECK_INT(short_circuit_and(0), 0);
CLINGS_CHECK_INT(touch_count(), 0);
CLINGS_CHECK_INT(short_circuit_or(1), 1);
CLINGS_CHECK_INT(touch_count(), 0);
CLINGS_CHECK_INT(short_circuit_and(1), 1);
CLINGS_CHECK_INT(touch_count(), 1);
""",
        breaks=[
            (
                "return left && touch();",
                "/* TODO: use the logical AND operator, not bitwise AND. */\n    return left & touch();",
            )
        ],
    ),
    ex(
        topic="04_operators",
        slug="04_bitwise",
        title="Bitwise set, clear, toggle, and test",
        objective="Use masks and bitwise operators safely.",
        reference="",
        hint="Clearing a bit uses value & ~(1u << bit).",
        code=r"""
unsigned set_bit(unsigned value, unsigned bit)
{
    return value | (1u << bit);
}

unsigned clear_bit(unsigned value, unsigned bit)
{
    return value & ~(1u << bit);
}

unsigned toggle_bit(unsigned value, unsigned bit)
{
    return value ^ (1u << bit);
}

int test_bit(unsigned value, unsigned bit)
{
    return (value & (1u << bit)) != 0;
}
""",
        tests=r"""
CLINGS_CHECK_INT(set_bit(0u, 3u), 8u);
CLINGS_CHECK_INT(clear_bit(0xFu, 2u), 0xBu);
CLINGS_CHECK_INT(toggle_bit(0xFu, 0u), 0xEu);
CLINGS_CHECK_INT(test_bit(0x8u, 3u), 1);
CLINGS_CHECK_INT(test_bit(0x8u, 2u), 0);
""",
        breaks=[
            (
                "return value & ~(1u << bit);",
                "/* TODO: clear the selected bit. */\n    return value & (1u << bit);",
            )
        ],
    ),
    ex(
        topic="04_operators",
        slug="05_shifts",
        title="Shift operators and masks",
        objective="Build masks and avoid shifting by the width of the type.",
        reference="",
        hint="A mask of width w has w low bits set: (1u << w) - 1u.",
        code=r"""
unsigned low_bits_mask(unsigned width)
{
    return (width == 0u) ? 0u : ((1u << width) - 1u);
}

unsigned shift_left_safe(unsigned value, unsigned count)
{
    return (count >= 32u) ? 0u : value << count;
}
""",
        tests=r"""
CLINGS_CHECK_INT(low_bits_mask(0u), 0u);
CLINGS_CHECK_INT(low_bits_mask(4u), 0xFu);
CLINGS_CHECK_INT(shift_left_safe(1u, 4u), 16u);
CLINGS_CHECK_INT(shift_left_safe(1u, 32u), 0u);
""",
        breaks=[
            (
                "return (width == 0u) ? 0u : ((1u << width) - 1u);",
                "/* TODO: subtract one to build the mask. */\n    return (width == 0u) ? 0u : (1u << width);",
            )
        ],
    ),
    ex(
        topic="04_operators",
        slug="06_sizeof_incdec",
        title="sizeof and increment operators",
        objective="Distinguish sizeof expressions from increment side effects.",
        reference="",
        hint="Post-increment returns the old value; pre-increment returns the new value.",
        code=r"""
int size_of_char(void)
{
    return (int)sizeof(char);
}

int post_increment(int *value)
{
    return (*value)++;
}

int pre_increment(int *value)
{
    return ++(*value);
}
""",
        tests=r"""
int value = 5;

CLINGS_CHECK_INT(size_of_char(), 1);
CLINGS_CHECK_INT(post_increment(&value), 5);
CLINGS_CHECK_INT(value, 6);
CLINGS_CHECK_INT(pre_increment(&value), 7);
CLINGS_CHECK_INT(value, 7);
""",
        breaks=[
            (
                "return (*value)++;",
                "/* TODO: use post-increment here. */\n    return ++(*value);",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 03_control_flow
    # ------------------------------------------------------------------
    ex(
        topic="05_control_flow",
        slug="01_if_else",
        title="if and else",
        objective="Write clear conditional branches.",
        reference="",
        hint="Check for positive, then negative, then the remaining zero case.",
        code=r"""
int sign_of(int value)
{
    if (value > 0) {
        return 1;
    }
    if (value < 0) {
        return -1;
    }
    return 0;
}

int max_of(int a, int b)
{
    return (a > b) ? a : b;
}
""",
        tests=r"""
CLINGS_CHECK_INT(sign_of(42), 1);
CLINGS_CHECK_INT(sign_of(-7), -1);
CLINGS_CHECK_INT(sign_of(0), 0);
CLINGS_CHECK_INT(max_of(3, 9), 9);
CLINGS_CHECK_INT(max_of(-1, -2), -1);
""",
        breaks=[
            (
                "if (value < 0) {\n        return -1;\n    }",
                "if (value < 0) {\n        /* TODO: negative numbers have sign -1. */\n        return 1;\n    }",
            )
        ],
    ),
    ex(
        topic="05_control_flow",
        slug="02_switch_case",
        title="switch and fallthrough",
        objective="Use intentional fallthrough and a default case.",
        reference="",
        hint="February has 29 days when leap is true.",
        code=r"""
int days_in_month(int month, int leap)
{
    switch (month) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        return 31;
    case 4:
    case 6:
    case 9:
    case 11:
        return 30;
    case 2:
        return leap ? 29 : 28;
    default:
        return -1;
    }
}
""",
        tests=r"""
CLINGS_CHECK_INT(days_in_month(1, 0), 31);
CLINGS_CHECK_INT(days_in_month(4, 0), 30);
CLINGS_CHECK_INT(days_in_month(2, 0), 28);
CLINGS_CHECK_INT(days_in_month(2, 1), 29);
CLINGS_CHECK_INT(days_in_month(13, 0), -1);
""",
        breaks=[
            (
                "return leap ? 29 : 28;",
                "/* TODO: account for leap years. */\n        return 28;",
            )
        ],
    ),
    ex(
        topic="05_control_flow",
        slug="03_loops",
        title="for and while loops",
        objective="Get loop bounds and accumulators right.",
        reference="",
        hint="sum_to(n) includes n; factorial multiplies 2 through n.",
        code=r"""
long sum_to(int n)
{
    long sum = 0;
    for (int i = 1; i <= n; ++i) {
        sum += i;
    }
    return sum;
}

long factorial(int n)
{
    long result = 1;
    for (int i = 2; i <= n; ++i) {
        result *= i;
    }
    return result;
}
""",
        tests=r"""
CLINGS_CHECK_INT(sum_to(0), 0);
CLINGS_CHECK_INT(sum_to(5), 15);
CLINGS_CHECK_INT(factorial(0), 1);
CLINGS_CHECK_INT(factorial(5), 120);
""",
        breaks=[
            (
                "for (int i = 1; i <= n; ++i) {\n        sum += i;\n    }",
                "/* TODO: include n in the sum. */\n    for (int i = 1; i < n; ++i) {\n        sum += i;\n    }",
            )
        ],
    ),
    ex(
        topic="05_control_flow",
        slug="04_break_continue",
        title="break and continue",
        objective="Use break to stop early and continue to skip one iteration.",
        reference="",
        hint="continue skips the rest of the current iteration; break exits the loop.",
        code=r"""
int first_even(const int *values, int count)
{
    for (int i = 0; i < count; ++i) {
        if (values[i] % 2 == 0) {
            return values[i];
        }
    }
    return -1;
}

int sum_positive(const int *values, int count)
{
    int sum = 0;
    for (int i = 0; i < count; ++i) {
        if (values[i] <= 0) {
            continue;
        }
        sum += values[i];
    }
    return sum;
}
""",
        tests=r"""
const int values[] = {1, -3, 4, 5, -6};

CLINGS_CHECK_INT(first_even(values, 5), 4);
CLINGS_CHECK_INT(sum_positive(values, 5), 10);
CLINGS_CHECK_INT(sum_positive((const int[]){-1, -2}, 2), 0);
""",
        breaks=[
            (
                "if (values[i] <= 0) {\n            continue;\n        }",
                "if (values[i] <= 0) {\n            /* TODO: skip this value, do not stop the loop. */\n            break;\n        }",
            )
        ],
    ),
    ex(
        topic="05_control_flow",
        slug="05_goto_cleanup",
        title="goto for single-exit cleanup",
        objective="Use goto for a clear cleanup path in C.",
        reference="",
        hint="Set *out only after the copy has been allocated and filled.",
        code=r"""
#include <stdlib.h>

int parse_and_sum(const int *values, int count, int *out)
{
    int *copy = NULL;
    int result = -1;

    if (values == NULL || out == NULL || count < 0) {
        goto cleanup;
    }

    copy = malloc((size_t)count * sizeof *copy);
    if (copy == NULL) {
        goto cleanup;
    }

    for (int i = 0; i < count; ++i) {
        copy[i] = values[i];
    }

    int sum = 0;
    for (int i = 0; i < count; ++i) {
        sum += copy[i];
    }
    *out = sum;
    result = 0;

cleanup:
    free(copy);
    return result;
}
""",
        tests=r"""
const int values[] = {1, 2, 3, 4};
int out = 0;

CLINGS_CHECK_INT(parse_and_sum(values, 4, &out), 0);
CLINGS_CHECK_INT(out, 10);
CLINGS_CHECK_INT(parse_and_sum(NULL, 4, &out), -1);
CLINGS_CHECK_INT(parse_and_sum(values, 4, NULL), -1);
""",
        breaks=[
            (
                "*out = sum;",
                "/* TODO: return the computed sum to the caller. */\n    *out = 0;",
            )
        ],
    ),
    ex(
        topic="05_control_flow",
        slug="06_state_machine",
        title="A small state machine",
        objective="Track state while scanning a string.",
        reference="",
        hint="A word starts when the previous character was whitespace.",
        code=r"""
int count_words(const char *text)
{
    int in_word = 0;
    int words = 0;

    for (const char *p = text; *p != '\0'; ++p) {
        if (*p == ' ' || *p == '\t' || *p == '\n') {
            in_word = 0;
        } else if (!in_word) {
            in_word = 1;
            ++words;
        }
    }
    return words;
}
""",
        tests=r"""
CLINGS_CHECK_INT(count_words(""), 0);
CLINGS_CHECK_INT(count_words("hello world"), 2);
CLINGS_CHECK_INT(count_words("  a\tb\n c  "), 3);
""",
        breaks=[
            (
                "} else if (!in_word) {",
                "} else if (in_word) {\n            /* TODO: a word starts when we were not in one. */",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 04_functions
    # ------------------------------------------------------------------
    ex(
        topic="06_functions",
        slug="01_declaration_definition",
        title="Declarations and definitions",
        objective="Use a forward declaration and an internal helper.",
        reference="",
        hint="The declaration promises the signature; the definition supplies the body.",
        code=r"""
static int square(int value);

int square_then_add(int value, int addend)
{
    return square(value) + addend;
}

static int square(int value)
{
    return value * value;
}
""",
        tests=r"""
CLINGS_CHECK_INT(square_then_add(3, 4), 13);
CLINGS_CHECK_INT(square_then_add(-2, 1), 5);
""",
        breaks=[
            (
                "return value * value;",
                "/* TODO: return the square of value. */\n    return value + value;",
            )
        ],
    ),
    ex(
        topic="06_functions",
        slug="02_parameters_return",
        title="Parameters and return values",
        objective="Return values through parameters and clamp a range.",
        reference="",
        hint="When count is zero, leave the outputs unchanged.",
        code=r"""
int clamp(int value, int low, int high)
{
    if (value < low) {
        return low;
    }
    if (value > high) {
        return high;
    }
    return value;
}

void min_max(const int *values, int count, int *min_out, int *max_out)
{
    if (count <= 0 || values == NULL || min_out == NULL || max_out == NULL) {
        return;
    }

    int minimum = values[0];
    int maximum = values[0];
    for (int i = 1; i < count; ++i) {
        if (values[i] < minimum) {
            minimum = values[i];
        }
        if (values[i] > maximum) {
            maximum = values[i];
        }
    }
    *min_out = minimum;
    *max_out = maximum;
}
""",
        tests=r"""
const int values[] = {4, -2, 9, 1};
int minimum = 0;
int maximum = 0;

CLINGS_CHECK_INT(clamp(5, 1, 10), 5);
CLINGS_CHECK_INT(clamp(0, 1, 10), 1);
CLINGS_CHECK_INT(clamp(11, 1, 10), 10);
min_max(values, 4, &minimum, &maximum);
CLINGS_CHECK_INT(minimum, -2);
CLINGS_CHECK_INT(maximum, 9);
""",
        breaks=[
            (
                "if (value < low) {\n        return low;\n    }",
                "if (value < low) {\n        /* TODO: clamp to the lower bound. */\n        return high;\n    }",
            )
        ],
    ),
    ex(
        topic="06_functions",
        slug="03_pass_by_pointer",
        title="Pass by value and pass by pointer",
        objective="Modify caller-owned data through pointers.",
        reference="",
        hint="Save *a before overwriting it.",
        code=r"""
void swap_int(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void increment_all(int *values, int count)
{
    for (int i = 0; i < count; ++i) {
        ++values[i];
    }
}
""",
        tests=r"""
int a = 1;
int b = 2;
int values[] = {1, 2, 3};

swap_int(&a, &b);
CLINGS_CHECK_INT(a, 2);
CLINGS_CHECK_INT(b, 1);
increment_all(values, 3);
CLINGS_CHECK_INT(values[0], 2);
CLINGS_CHECK_INT(values[1], 3);
CLINGS_CHECK_INT(values[2], 4);
""",
        breaks=[
            (
                "int temp = *a;\n    *a = *b;\n    *b = temp;",
                "/* TODO: swap the two integers without losing either value. */\n    *a = *b;\n    *b = *a;",
            )
        ],
    ),
    ex(
        topic="06_functions",
        slug="04_recursion",
        title="Recursion and base cases",
        objective="Write recursive functions with correct base cases.",
        reference="",
        hint="factorial(n) = n * factorial(n - 1).",
        code=r"""
long factorial_recursive(int n)
{
    return n <= 1 ? 1 : n * factorial_recursive(n - 1);
}

int fibonacci(int n)
{
    return n <= 1 ? n : fibonacci(n - 1) + fibonacci(n - 2);
}
""",
        tests=r"""
CLINGS_CHECK_INT(factorial_recursive(0), 1);
CLINGS_CHECK_INT(factorial_recursive(5), 120);
CLINGS_CHECK_INT(fibonacci(0), 0);
CLINGS_CHECK_INT(fibonacci(1), 1);
CLINGS_CHECK_INT(fibonacci(8), 21);
""",
        breaks=[
            (
                "return n <= 1 ? 1 : n * factorial_recursive(n - 1);",
                "/* TODO: multiply by the recursive result. */\n    return n <= 1 ? 1 : n + factorial_recursive(n - 1);",
            )
        ],
    ),
    ex(
        topic="06_functions",
        slug="05_static_inline",
        title="Internal linkage and inline helpers",
        objective="Use static functions and file-scope state.",
        reference="",
        hint="Update call_count before returning the incremented value.",
        code=r"""
static int call_count = 0;

static int add_one(int value)
{
    ++call_count;
    return value + 1;
}

int call_add_one(int value)
{
    return add_one(value);
}

int add_one_calls(void)
{
    return call_count;
}
""",
        tests=r"""
CLINGS_CHECK_INT(add_one_calls(), 0);
CLINGS_CHECK_INT(call_add_one(1), 2);
CLINGS_CHECK_INT(call_add_one(2), 3);
CLINGS_CHECK_INT(add_one_calls(), 2);
""",
        breaks=[
            (
                "++call_count;",
                "/* TODO: count every call. */",
            )
        ],
    ),
    ex(
        topic="06_functions",
        slug="06_function_pointers",
        title="Function pointers and dispatch",
        objective="Store functions in variables and choose one at runtime.",
        reference="",
        hint="Return the function that matches the operator character.",
        code=r"""
typedef int (*operation_fn)(int, int);

static int add(int a, int b)
{
    return a + b;
}

static int multiply(int a, int b)
{
    return a * b;
}

int apply_operation(operation_fn op, int a, int b)
{
    return op(a, b);
}

operation_fn choose_operation(char op)
{
    return op == '+' ? add : multiply;
}
""",
        tests=r"""
CLINGS_CHECK_INT(apply_operation(add, 2, 3), 5);
CLINGS_CHECK_INT(apply_operation(multiply, 2, 3), 6);
CLINGS_CHECK_INT(choose_operation('+')(4, 5), 9);
CLINGS_CHECK_INT(choose_operation('*')(4, 5), 20);
""",
        breaks=[
            (
                "return op == '+' ? add : multiply;",
                "/* TODO: choose multiply for any non-plus operator. */\n    return add;",
            )
        ],
    ),
    ex(
        topic="06_functions",
        slug="07_void_and_return",
        title="void functions and return statements",
        objective="Return early from a void function and return values from int functions.",
        reference="",
        hint="A void function uses a bare return; an int function must return a value.",
        code=r"""
#include <stddef.h>

void set_zero(int *value)
{
    if (value == NULL) {
        return;
    }
    *value = 0;
}

int early_return(int value)
{
    if (value < 0) {
        return -1;
    }
    return value * 2;
}
""",
        tests=r"""
int value = 5;

set_zero(&value);
CLINGS_CHECK_INT(value, 0);
set_zero(NULL);
CLINGS_CHECK_INT(value, 0);
CLINGS_CHECK_INT(early_return(-3), -1);
CLINGS_CHECK_INT(early_return(4), 8);
""",
        breaks=[
            (
                "return value * 2;",
                "/* TODO: double the non-negative value. */\n    return value;",
            )
        ],
    ),
]
