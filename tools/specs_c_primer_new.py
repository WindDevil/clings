"""C Primer Plus gap exercises that form new topics."""

from spec import ex, project

SPECS = [
    # ------------------------------------------------------------------
    # 13_translation_units
    # ------------------------------------------------------------------
    project(
        topic="13_translation_units",
        slug="01_header_source_split",
        title="Header and source split",
        objective="Compile a program from a main file, a header, and an implementation file.",
        reference="C Primer Plus 第9章 9.4、第16章 16.5",
        hint="Declare add in the header and define it in math_utils.c.",
        files={
            "math_utils.h": r"""
#ifndef MATH_UTILS_H
#define MATH_UTILS_H

int add(int left, int right);

#endif
""",
            "math_utils.c": r"""
#include "math_utils.h"

int add(int left, int right)
{
    return left + right;
}
""",
            "main.c": r"""
#include "clings/test.h"
#include "math_utils.h"

int main(void)
{
    CLINGS_CHECK_INT(add(2, 3), 5);
    CLINGS_CHECK_INT(add(-4, 4), 0);
    return clings_report();
}
""",
        },
        file_breaks=[
            (
                "math_utils.c",
                "return left + right;",
                "/* TODO: add the two values. */\n    return left - right;",
            )
        ],
    ),
    project(
        topic="13_translation_units",
        slug="02_extern_linkage",
        title="External linkage across files",
        objective="Declare a global variable in a header and define it in another file.",
        reference="C Primer Plus 第12章 12.1.7、12.1.9",
        hint="The extern declaration promises a definition in config.c.",
        files={
            "config.h": r"""
#ifndef CONFIG_H
#define CONFIG_H

extern int config_value;

#endif
""",
            "config.c": r"""
#include "config.h"

int config_value = 42;
""",
            "main.c": r"""
#include "clings/test.h"
#include "config.h"

int main(void)
{
    CLINGS_CHECK_INT(config_value, 42);
    return clings_report();
}
""",
        },
        file_breaks=[
            (
                "config.c",
                "int config_value = 42;",
                "/* TODO: define config_value. */",
            )
        ],
    ),
    project(
        topic="13_translation_units",
        slug="03_static_internal_linkage",
        title="Internal linkage and file-scope state",
        objective="Keep a counter private to one translation unit with static.",
        reference="C Primer Plus 第12章 12.1.8-12.1.9",
        hint="static file-scope objects are visible only in their own .c file.",
        files={
            "counter.h": r"""
#ifndef COUNTER_H
#define COUNTER_H

int next_count(void);
int count_calls(void);

#endif
""",
            "counter.c": r"""
#include "counter.h"

static int count = 0;

int next_count(void)
{
    return ++count;
}

int count_calls(void)
{
    return count;
}
""",
            "main.c": r"""
#include "clings/test.h"
#include "counter.h"

int main(void)
{
    CLINGS_CHECK_INT(next_count(), 1);
    CLINGS_CHECK_INT(next_count(), 2);
    CLINGS_CHECK_INT(count_calls(), 2);
    return clings_report();
}
""",
        },
        file_breaks=[
            (
                "counter.c",
                "return ++count;",
                "/* TODO: pre-increment the private counter. */\n    return count++;",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 14_character_io
    # ------------------------------------------------------------------
    ex(
        topic="14_character_io",
        slug="01_getc_putc",
        title="getc and putc",
        objective="Copy a stream one character at a time with getc and putc.",
        reference="C Primer Plus 第8章 8.1、第13章 13.2.3",
        hint="getc returns EOF when there are no more characters.",
        code=r"""
#include <stdio.h>

int copy_stream(FILE *input, FILE *output)
{
    int character;
    int count = 0;
    while ((character = getc(input)) != EOF) {
        putc(character, output);
        ++count;
    }
    return count;
}
""",
        tests=r"""
FILE *input = tmpfile();
FILE *output = tmpfile();
char buffer[16];

CLINGS_CHECK(input != NULL && output != NULL);
fputs("hello", input);
rewind(input);
CLINGS_CHECK_INT(copy_stream(input, output), 5);
rewind(output);
CLINGS_CHECK(fgets(buffer, sizeof buffer, output) != NULL);
CLINGS_CHECK_STR(buffer, "hello");
fclose(input);
fclose(output);
""",
        breaks=[
            (
                "putc(character, output);",
                "/* TODO: write the current character. */\n        putc('x', output);",
            )
        ],
    ),
    ex(
        topic="14_character_io",
        slug="02_eof_ferror",
        title="EOF, feof, and ferror",
        objective="Read until EOF and distinguish end-of-file from an error.",
        reference="C Primer Plus 第8章 8.3、第13章 13.7.7",
        hint="feof is true only after a read attempts to pass the end of the file.",
        code=r"""
#include <stdio.h>

int read_all(FILE *file, char *buffer, size_t size)
{
    size_t index = 0;
    int character;
    while (index + 1 < size && (character = fgetc(file)) != EOF) {
        buffer[index] = (char)character;
        ++index;
    }
    buffer[index] = '\0';
    if (ferror(file)) {
        return -1;
    }
    return (int)index;
}
""",
        tests=r"""
FILE *file = tmpfile();
char buffer[16];

CLINGS_CHECK(file != NULL);
fputs("abc", file);
rewind(file);
CLINGS_CHECK_INT(read_all(file, buffer, sizeof buffer), 3);
CLINGS_CHECK_STR(buffer, "abc");
CLINGS_CHECK_INT(feof(file), 1);
fclose(file);
""",
        breaks=[
            (
                "return (int)index;",
                "/* TODO: return the number of characters read. */\n    return -1;",
            )
        ],
    ),
    ex(
        topic="14_character_io",
        slug="03_input_validation",
        title="Input validation",
        objective="Reject input with trailing characters or out-of-range values.",
        reference="C Primer Plus 第8章 8.6",
        hint="Use %c after %d to detect trailing non-whitespace input.",
        code=r"""
#include <stdio.h>

int read_choice(const char *input, int *choice)
{
    int value = 0;
    char extra = '\0';
    if (sscanf(input, "%d %c", &value, &extra) != 1) {
        return -1;
    }
    if (value < 1 || value > 3) {
        return -1;
    }
    *choice = value;
    return 0;
}
""",
        tests=r"""
int choice = 0;

CLINGS_CHECK_INT(read_choice("2", &choice), 0);
CLINGS_CHECK_INT(choice, 2);
CLINGS_CHECK_INT(read_choice("2x", &choice), -1);
CLINGS_CHECK_INT(read_choice("9", &choice), -1);
CLINGS_CHECK_INT(read_choice("abc", &choice), -1);
""",
        breaks=[
            (
                'if (sscanf(input, "%d %c", &value, &extra) != 1) {',
                '/* TODO: reject trailing characters. */\n    if (sscanf(input, "%d", &value) != 1) {',
            )
        ],
    ),
    ex(
        topic="14_character_io",
        slug="04_iso646",
        title="iso646.h alternative spellings",
        objective="Use and/or/not from iso646.h.",
        reference="C Primer Plus 第7章 7.3.1",
        hint="iso646.h defines and as && and or as ||.",
        code=r"""
#include <iso646.h>

int is_yes(const char *text)
{
    return (text[0] == 'y' or text[0] == 'Y') and text[1] == '\0';
}
""",
        tests=r"""
CLINGS_CHECK_INT(is_yes("y"), 1);
CLINGS_CHECK_INT(is_yes("Y"), 1);
CLINGS_CHECK_INT(is_yes("yes"), 0);
CLINGS_CHECK_INT(is_yes("n"), 0);
""",
        breaks=[
            (
                "(text[0] == 'y' or text[0] == 'Y') and text[1] == '\\0'",
                "/* TODO: accept either y or Y. */\n    (text[0] == 'y' and text[0] == 'Y') and text[1] == '\\0'",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 15_string_functions
    # ------------------------------------------------------------------
    ex(
        topic="15_string_functions",
        slug="01_strcat_strncat",
        title="strcat and strncat",
        objective="Append a string while respecting the destination size.",
        reference="C Primer Plus 第11章 11.5.2-11.5.3",
        hint="strncat appends at most n characters and always terminates.",
        code=r"""
#include <stddef.h>
#include <string.h>

int append_bounded(char *destination, size_t size, const char *source)
{
    size_t used = strlen(destination);
    if (used >= size) {
        return -1;
    }
    strncat(destination, source, size - used - 1);
    return 0;
}
""",
        tests=r"""
char buffer[16] = "Hello";
char small[8] = "Hello";

CLINGS_CHECK_INT(append_bounded(buffer, sizeof buffer, " C"), 0);
CLINGS_CHECK_STR(buffer, "Hello C");
CLINGS_CHECK_INT(append_bounded(small, sizeof small, " world"), 0);
CLINGS_CHECK_STR(small, "Hello w");
""",
        breaks=[
            (
                "return 0;",
                "/* TODO: report success after a bounded append. */\n    return -1;",
            )
        ],
    ),
    ex(
        topic="15_string_functions",
        slug="02_strncpy_bounded",
        title="Bounded copying with strncpy",
        objective="Copy a string safely and always terminate the destination.",
        reference="C Primer Plus 第11章 11.5.5",
        hint="strncpy does not guarantee a terminating NUL when the source is too long.",
        code=r"""
#include <stddef.h>
#include <string.h>

int copy_bounded(char *destination, size_t size, const char *source)
{
    if (size == 0) {
        return -1;
    }
    strncpy(destination, source, size - 1);
    destination[size - 1] = '\0';
    return 0;
}
""",
        tests=r"""
char buffer[8];
char small[4];

CLINGS_CHECK_INT(copy_bounded(buffer, sizeof buffer, "hello"), 0);
CLINGS_CHECK_STR(buffer, "hello");
CLINGS_CHECK_INT(copy_bounded(small, sizeof small, "hello"), 0);
CLINGS_CHECK_STR(small, "hel");
CLINGS_CHECK_INT(copy_bounded(buffer, 0, "x"), -1);
""",
        breaks=[
            (
                "destination[size - 1] = '\\0';",
                "/* TODO: terminate the copied string. */\n    destination[size - 1] = 'x';",
            )
        ],
    ),
    ex(
        topic="15_string_functions",
        slug="03_sprintf_snprintf",
        title="sprintf and snprintf",
        objective="Format text with snprintf and understand truncation.",
        reference="C Primer Plus 第11章 11.5.6",
        hint="snprintf returns the number of characters that would have been written.",
        code=r"""
#include <stdio.h>

int format_record(char *buffer, size_t size, const char *name, int age)
{
    return snprintf(buffer, size, "%s:%d", name, age);
}
""",
        tests=r"""
char buffer[32];
char small[6];

CLINGS_CHECK_INT(format_record(buffer, sizeof buffer, "Ada", 36), 6);
CLINGS_CHECK_STR(buffer, "Ada:36");
CLINGS_CHECK_INT(format_record(small, sizeof small, "Ada", 36), 6);
CLINGS_CHECK_STR(small, "Ada:3");
""",
        breaks=[
            (
                'return snprintf(buffer, size, "%s:%d", name, age);',
                '/* TODO: format name followed by age. */\n    return snprintf(buffer, size, "%d:%s", age, name);',
            )
        ],
    ),
    ex(
        topic="15_string_functions",
        slug="04_fgets_fputs_sort",
        title="fgets, fputs, and sorting strings",
        objective="Read a line with fgets and sort an array of strings.",
        reference="C Primer Plus 第11章 11.2.3、11.6",
        hint="qsort receives an array of pointers, so cast to const char *const *.",
        code=r"""
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int compare_strings(const void *left, const void *right)
{
    return strcmp(*(const char *const *)left, *(const char *const *)right);
}

void sort_strings(const char **values, size_t count)
{
    qsort(values, count, sizeof *values, compare_strings);
}

int read_line(FILE *file, char *buffer, size_t size)
{
    return fgets(buffer, (int)size, file) != NULL ? 0 : -1;
}
""",
        tests=r"""
FILE *file = tmpfile();
char buffer[16];
const char *values[3] = {"pear", "apple", "banana"};

CLINGS_CHECK(file != NULL);
fputs("hello\n", file);
rewind(file);
CLINGS_CHECK_INT(read_line(file, buffer, sizeof buffer), 0);
CLINGS_CHECK_STR(buffer, "hello\n");
fclose(file);
sort_strings(values, 3);
CLINGS_CHECK_STR(values[0], "apple");
CLINGS_CHECK_STR(values[1], "banana");
CLINGS_CHECK_STR(values[2], "pear");
""",
        breaks=[
            (
                "return strcmp(*(const char *const *)left, *(const char *const *)right);",
                "/* TODO: sort in ascending order. */\n    return strcmp(*(const char *const *)right, *(const char *const *)left);",
            )
        ],
    ),
    ex(
        topic="15_string_functions",
        slug="05_strtod",
        title="Converting strings to double",
        objective="Parse a double with strtod and reject trailing input.",
        reference="C Primer Plus 第11章 11.9",
        hint="Check errno, endptr, and the character after the number.",
        code=r"""
#include <errno.h>
#include <stdlib.h>

int parse_double(const char *text, double *out)
{
    char *end = NULL;
    errno = 0;
    double value = strtod(text, &end);
    if (errno == ERANGE || end == text || *end != '\0') {
        return -1;
    }
    *out = value;
    return 0;
}
""",
        tests=r"""
double value = 0.0;

CLINGS_CHECK_INT(parse_double("3.14", &value), 0);
CLINGS_CHECK_INT(value == 3.14, 1);
CLINGS_CHECK_INT(parse_double("3.14x", &value), -1);
CLINGS_CHECK_INT(parse_double("", &value), -1);
""",
        breaks=[
            (
                "if (errno == ERANGE || end == text || *end != '\\0') {",
                "/* TODO: reject trailing characters. */\n    if (errno == ERANGE || end == text) {",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 16_data_representation
    # ------------------------------------------------------------------
    ex(
        topic="16_data_representation",
        slug="01_base_conversion",
        title="Binary, octal, and hexadecimal input",
        objective="Parse a hexadecimal string with strtoul.",
        reference="C Primer Plus 第15章 15.2",
        hint="Base 16 accepts an optional 0x prefix.",
        code=r"""
#include <stdlib.h>

int parse_hex(const char *text, unsigned int *out)
{
    char *end = NULL;
    unsigned int value = (unsigned int)strtoul(text, &end, 16);
    if (end == text || *end != '\0') {
        return -1;
    }
    *out = value;
    return 0;
}
""",
        tests=r"""
unsigned int value = 0;

CLINGS_CHECK_INT(parse_hex("0x2A", &value), 0);
CLINGS_CHECK_INT(value, 42);
CLINGS_CHECK_INT(parse_hex("2A", &value), 0);
CLINGS_CHECK_INT(value, 42);
CLINGS_CHECK_INT(parse_hex("xyz", &value), -1);
""",
        breaks=[
            (
                "unsigned int value = (unsigned int)strtoul(text, &end, 16);",
                "/* TODO: parse base 16. */\n    unsigned int value = (unsigned int)strtoul(text, &end, 10);",
            )
        ],
    ),
    ex(
        topic="16_data_representation",
        slug="02_integer_binary_representation",
        title="Integer bit patterns",
        objective="Count set bits and convert sign-magnitude to two's complement.",
        reference="C Primer Plus 第15章 15.1",
        hint="value &= value - 1 clears the lowest set bit.",
        code=r"""
int count_set_bits(unsigned int value)
{
    int count = 0;
    while (value != 0) {
        value &= value - 1;
        ++count;
    }
    return count;
}

unsigned int sign_magnitude_to_twos_complement(unsigned int sign_magnitude)
{
    unsigned int sign = sign_magnitude & 0x80000000u;
    unsigned int magnitude = sign_magnitude & 0x7fffffffu;
    return sign ? (~magnitude + 1u) : magnitude;
}
""",
        tests=r"""
CLINGS_CHECK_INT(count_set_bits(0u), 0);
CLINGS_CHECK_INT(count_set_bits(0xF0F0u), 8);
CLINGS_CHECK_INT(sign_magnitude_to_twos_complement(0x80000001u), 0xFFFFFFFFu);
""",
        breaks=[
            (
                "value &= value - 1;",
                "/* TODO: clear the lowest set bit. */\n        value >>= 1;",
            )
        ],
    ),
    ex(
        topic="16_data_representation",
        slug="03_float_binary_representation",
        title="Floating-point bit patterns",
        objective="Inspect and reconstruct an IEEE-754 float with memcpy.",
        reference="C Primer Plus 第15章 15.1.3",
        hint="Use memcpy instead of pointer casts to avoid strict-aliasing violations.",
        code=r"""
#include <stdint.h>
#include <string.h>

uint32_t float_bits(float value)
{
    uint32_t bits = 0;
    memcpy(&bits, &value, sizeof bits);
    return bits;
}

float bits_to_float(uint32_t bits)
{
    float value = 0.0f;
    memcpy(&value, &bits, sizeof value);
    return value;
}
""",
        tests=r"""
CLINGS_CHECK_INT(float_bits(1.0f), 0x3f800000u);
CLINGS_CHECK_INT(bits_to_float(0x3f800000u) == 1.0f, 1);
""",
        breaks=[
            (
                "memcpy(&bits, &value, sizeof bits);",
                "/* TODO: copy the object representation. */\n    bits = (uint32_t)value;",
            )
        ],
    ),
    ex(
        topic="16_data_representation",
        slug="04_bitfield_portability",
        title="Bitfields and explicit masks",
        objective="Pack fields with bitfields and compare them with an explicit mask.",
        reference="C Primer Plus 第15章 15.4",
        hint="Bitfield layout is implementation-defined; masks make the encoding explicit.",
        code=r"""
struct flags {
    unsigned int first : 1;
    unsigned int second : 1;
    unsigned int value : 4;
};

int pack_flags(int first, int second, int value)
{
    struct flags flags = {0};
    flags.first = first ? 1u : 0u;
    flags.second = second ? 1u : 0u;
    flags.value = (unsigned int)(value & 0x0f);
    return (int)flags.first | ((int)flags.second << 1) | ((int)flags.value << 2);
}
""",
        tests=r"""
CLINGS_CHECK_INT(pack_flags(1, 0, 5), 21);
CLINGS_CHECK_INT(pack_flags(0, 1, 15), 62);
""",
        breaks=[
            (
                "flags.value = (unsigned int)(value & 0x0f);",
                "/* TODO: mask the four-bit value field. */\n    flags.value = 0;",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 17_data_structures
    # ------------------------------------------------------------------
    ex(
        topic="17_data_structures",
        slug="01_queue_adt",
        title="Queue ADT",
        objective="Implement a fixed-capacity circular queue.",
        reference="C Primer Plus 第17章 17.4",
        hint="The tail index wraps with modulo capacity.",
        code=r"""
#include <stddef.h>

#define QUEUE_CAPACITY 8

struct queue {
    int values[QUEUE_CAPACITY];
    size_t head;
    size_t tail;
    size_t count;
};

void queue_init(struct queue *queue)
{
    queue->head = 0;
    queue->tail = 0;
    queue->count = 0;
}

int queue_push(struct queue *queue, int value)
{
    if (queue->count == QUEUE_CAPACITY) {
        return -1;
    }
    queue->values[queue->tail] = value;
    queue->tail = (queue->tail + 1) % QUEUE_CAPACITY;
    ++queue->count;
    return 0;
}

int queue_pop(struct queue *queue, int *out)
{
    if (queue->count == 0) {
        return -1;
    }
    *out = queue->values[queue->head];
    queue->head = (queue->head + 1) % QUEUE_CAPACITY;
    --queue->count;
    return 0;
}

size_t queue_size(const struct queue *queue)
{
    return queue->count;
}
""",
        tests=r"""
struct queue queue;
int value = 0;

queue_init(&queue);
CLINGS_CHECK_INT(queue_size(&queue), 0);
CLINGS_CHECK_INT(queue_push(&queue, 1), 0);
CLINGS_CHECK_INT(queue_push(&queue, 2), 0);
CLINGS_CHECK_INT(queue_push(&queue, 3), 0);
CLINGS_CHECK_INT(queue_size(&queue), 3);
CLINGS_CHECK_INT(queue_pop(&queue, &value), 0);
CLINGS_CHECK_INT(value, 1);
CLINGS_CHECK_INT(queue_pop(&queue, &value), 0);
CLINGS_CHECK_INT(value, 2);
""",
        breaks=[
            (
                "queue->values[queue->tail] = value;",
                "/* TODO: store the new value. */\n    queue->values[queue->tail] = 0;",
            )
        ],
    ),
    ex(
        topic="17_data_structures",
        slug="02_binary_search_tree",
        title="Binary search tree",
        objective="Insert into and search a binary search tree.",
        reference="C Primer Plus 第17章 17.7",
        hint="Smaller values go left; larger values go right.",
        code=r"""
#include <stddef.h>
#include <stdlib.h>

struct node {
    int value;
    struct node *left;
    struct node *right;
};

struct node *insert(struct node *root, int value)
{
    if (root == NULL) {
        struct node *node = malloc(sizeof *node);
        if (node == NULL) {
            return NULL;
        }
        node->value = value;
        node->left = NULL;
        node->right = NULL;
        return node;
    }
    if (value < root->value) {
        root->left = insert(root->left, value);
    } else if (value > root->value) {
        root->right = insert(root->right, value);
    }
    return root;
}

int contains(const struct node *root, int value)
{
    if (root == NULL) {
        return 0;
    }
    if (value < root->value) {
        return contains(root->left, value);
    }
    if (value > root->value) {
        return contains(root->right, value);
    }
    return 1;
}

void free_tree(struct node *root)
{
    if (root == NULL) {
        return;
    }
    free_tree(root->left);
    free_tree(root->right);
    free(root);
}
""",
        tests=r"""
struct node *root = NULL;

root = insert(root, 5);
root = insert(root, 3);
root = insert(root, 7);
CLINGS_CHECK_INT(contains(root, 5), 1);
CLINGS_CHECK_INT(contains(root, 3), 1);
CLINGS_CHECK_INT(contains(root, 7), 1);
CLINGS_CHECK_INT(contains(root, 4), 0);
free_tree(root);
""",
        breaks=[
            (
                "root->right = insert(root->right, value);",
                "/* TODO: larger values go to the right subtree. */\n        root->left = insert(root->left, value);",
            )
        ],
    ),
    ex(
        topic="17_data_structures",
        slug="03_dynamic_vector",
        title="Dynamic array/vector",
        objective="Grow a dynamic array and preserve existing elements.",
        reference="C Primer Plus 第17章 17.2、17.6",
        hint="Double the capacity when the array is full.",
        code=r"""
#include <stddef.h>
#include <stdlib.h>

struct vector {
    int *values;
    size_t size;
    size_t capacity;
};

int vector_push(struct vector *vector, int value)
{
    if (vector->size == vector->capacity) {
        size_t new_capacity = vector->capacity == 0 ? 2 : vector->capacity * 2;
        int *grown = realloc(vector->values, new_capacity * sizeof *grown);
        if (grown == NULL) {
            return -1;
        }
        vector->values = grown;
        vector->capacity = new_capacity;
    }
    vector->values[vector->size++] = value;
    return 0;
}

void vector_free(struct vector *vector)
{
    free(vector->values);
    vector->values = NULL;
    vector->size = 0;
    vector->capacity = 0;
}
""",
        tests=r"""
struct vector vector = {0};

for (int value = 1; value <= 5; ++value) {
    CLINGS_CHECK_INT(vector_push(&vector, value), 0);
}
CLINGS_CHECK_INT(vector.size, 5);
CLINGS_CHECK_INT(vector.values[0], 1);
CLINGS_CHECK_INT(vector.values[4], 5);
vector_free(&vector);
""",
        breaks=[
            (
                "vector->values[vector->size++] = value;",
                "/* TODO: append the value and increase size. */\n    vector->values[vector->size] = value;",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 18_file_io_advanced
    # ------------------------------------------------------------------
    ex(
        topic="18_file_io_advanced",
        slug="01_fprintf_fscanf",
        title="fprintf and fscanf",
        objective="Write formatted data to a file and read it back.",
        reference="C Primer Plus 第13章 13.4.1",
        hint="The format strings used for writing and reading must agree.",
        code=r"""
#include <stdio.h>

int write_person(const char *path, const char *name, int age)
{
    FILE *file = fopen(path, "w");
    if (file == NULL) {
        return -1;
    }
    int ok = fprintf(file, "%s %d\n", name, age) > 0;
    if (fclose(file) != 0) {
        ok = 0;
    }
    return ok ? 0 : -1;
}

int read_person(const char *path, char *name, int *age)
{
    FILE *file = fopen(path, "r");
    if (file == NULL) {
        return -1;
    }
    int ok = fscanf(file, "%31s %d", name, age) == 2;
    fclose(file);
    return ok ? 0 : -1;
}
""",
        tests=r"""
const char *path = "/tmp/clings_fprintf_test.txt";
char name[32];
int age = 0;

CLINGS_CHECK_INT(write_person(path, "Ada", 36), 0);
CLINGS_CHECK_INT(read_person(path, name, &age), 0);
CLINGS_CHECK_STR(name, "Ada");
CLINGS_CHECK_INT(age, 36);
remove(path);
""",
        breaks=[
            (
                'int ok = fprintf(file, "%s %d\\n", name, age) > 0;',
                '/* TODO: write name followed by age. */\n    int ok = fprintf(file, "%d %s\\n", age, name) > 0;',
            )
        ],
    ),
    ex(
        topic="18_file_io_advanced",
        slug="02_fgets_fputs",
        title="fgets and fputs",
        objective="Copy a text file line by line.",
        reference="C Primer Plus 第13章 13.4.2",
        hint="fgets includes the newline when the buffer is large enough.",
        code=r"""
#include <stdio.h>

int copy_lines(FILE *input, FILE *output)
{
    char buffer[64];
    int count = 0;
    while (fgets(buffer, sizeof buffer, input) != NULL) {
        if (fputs(buffer, output) == EOF) {
            return -1;
        }
        ++count;
    }
    return count;
}
""",
        tests=r"""
FILE *input = tmpfile();
FILE *output = tmpfile();
char buffer[64];

CLINGS_CHECK(input != NULL && output != NULL);
fputs("first\nsecond\n", input);
rewind(input);
CLINGS_CHECK_INT(copy_lines(input, output), 2);
rewind(output);
CLINGS_CHECK(fgets(buffer, sizeof buffer, output) != NULL);
CLINGS_CHECK_STR(buffer, "first\n");
CLINGS_CHECK(fgets(buffer, sizeof buffer, output) != NULL);
CLINGS_CHECK_STR(buffer, "second\n");
fclose(input);
fclose(output);
""",
        breaks=[
            (
                "if (fputs(buffer, output) == EOF) {",
                '/* TODO: copy the line that was read. */\n        if (fputs("line\\n", output) == EOF) {',
            )
        ],
    ),
    ex(
        topic="18_file_io_advanced",
        slug="03_getc_putc_ungetc",
        title="getc, putc, and ungetc",
        objective="Peek at a character and put it back into the stream.",
        reference="C Primer Plus 第13章 13.2.3、13.7.1",
        hint="ungetc pushes one character back onto the input stream.",
        code=r"""
#include <stdio.h>

int peek_character(FILE *file)
{
    int character = getc(file);
    if (character != EOF) {
        ungetc(character, file);
    }
    return character;
}
""",
        tests=r"""
FILE *file = tmpfile();

CLINGS_CHECK(file != NULL);
fputs("abc", file);
rewind(file);
CLINGS_CHECK_INT(peek_character(file), 'a');
CLINGS_CHECK_INT(peek_character(file), 'a');
CLINGS_CHECK_INT(getc(file), 'a');
fclose(file);
""",
        breaks=[
            (
                "ungetc(character, file);",
                "/* TODO: put the character back into the stream. */",
            )
        ],
    ),
    ex(
        topic="18_file_io_advanced",
        slug="04_fseek_ftell",
        title="Random access with fseek and ftell",
        objective="Seek to a byte offset and report the resulting position.",
        reference="C Primer Plus 第13章 13.5",
        hint="fseek with SEEK_SET positions the stream at an absolute offset.",
        code=r"""
#include <stdio.h>

int read_at(FILE *file, long offset, char *buffer, size_t size)
{
    if (fseek(file, offset, SEEK_SET) != 0) {
        return -1;
    }
    if (fgets(buffer, (int)size, file) == NULL) {
        return -1;
    }
    return (int)ftell(file);
}
""",
        tests=r"""
FILE *file = tmpfile();
char buffer[8];

CLINGS_CHECK(file != NULL);
fputs("abcdef", file);
rewind(file);
CLINGS_CHECK_INT(read_at(file, 2, buffer, sizeof buffer), 6);
CLINGS_CHECK_STR(buffer, "cdef");
fclose(file);
""",
        breaks=[
            (
                "if (fseek(file, offset, SEEK_SET) != 0) {",
                "/* TODO: seek relative to the beginning of the file. */\n    if (fseek(file, offset, SEEK_END) != 0) {",
            )
        ],
    ),
    ex(
        topic="18_file_io_advanced",
        slug="05_fflush_setvbuf",
        title="Stream buffering",
        objective="Configure full buffering and flush a stream.",
        reference="C Primer Plus 第13章 13.7.2-13.7.3",
        hint="setvbuf must be called before other I/O on the stream.",
        code=r"""
#include <stdio.h>

int configure_buffer(FILE *file, char *buffer, size_t size)
{
    return setvbuf(file, buffer, _IOFBF, size) == 0 ? 0 : -1;
}

int flush_output(FILE *file)
{
    return fflush(file) == 0 ? 0 : -1;
}
""",
        tests=r"""
FILE *file = tmpfile();
char buffer[128];

CLINGS_CHECK(file != NULL);
CLINGS_CHECK_INT(configure_buffer(file, buffer, sizeof buffer), 0);
CLINGS_CHECK_INT(fputs("buffered", file) >= 0, 1);
CLINGS_CHECK_INT(flush_output(file), 0);
fclose(file);
""",
        breaks=[
            (
                "return fflush(file) == 0 ? 0 : -1;",
                "/* TODO: flush the stream. */\n    return -1;",
            )
        ],
    ),
    ex(
        topic="18_file_io_advanced",
        slug="06_binary_random_access",
        title="Binary random access",
        objective="Read a specific struct record from a binary file.",
        reference="C Primer Plus 第13章 13.7.9",
        hint="Seek by index * sizeof(record).",
        code=r"""
#include <stddef.h>
#include <stdio.h>

struct record {
    int id;
    char name[16];
};

int write_records(const char *path, const struct record *records, size_t count)
{
    FILE *file = fopen(path, "wb");
    if (file == NULL) {
        return -1;
    }
    size_t written = fwrite(records, sizeof *records, count, file);
    fclose(file);
    return written == count ? 0 : -1;
}

int read_record_at(const char *path, size_t index, struct record *out)
{
    FILE *file = fopen(path, "rb");
    if (file == NULL) {
        return -1;
    }
    if (fseek(file, (long)(index * sizeof *out), SEEK_SET) != 0) {
        fclose(file);
        return -1;
    }
    size_t read_count = fread(out, sizeof *out, 1, file);
    fclose(file);
    return read_count == 1 ? 0 : -1;
}
""",
        tests=r"""
const char *path = "/tmp/clings_binary_records.bin";
const struct record records[3] = {
    {1, "one"},
    {2, "two"},
    {3, "three"},
};
struct record record = {0};

CLINGS_CHECK_INT(write_records(path, records, 3), 0);
CLINGS_CHECK_INT(read_record_at(path, 1, &record), 0);
CLINGS_CHECK_INT(record.id, 2);
CLINGS_CHECK_STR(record.name, "two");
remove(path);
""",
        breaks=[
            (
                "if (fseek(file, (long)(index * sizeof *out), SEEK_SET) != 0) {",
                "/* TODO: seek to the selected record. */\n    if (fseek(file, (long)index, SEEK_SET) != 0) {",
            )
        ],
    ),

    # ------------------------------------------------------------------
    # 19_modern_c_library
    # ------------------------------------------------------------------
    ex(
        topic="19_modern_c_library",
        slug="01_noreturn",
        title="_Noreturn functions",
        objective="Declare a function that never returns and observe its exit status.",
        reference="C Primer Plus 第16章 16.8",
        hint="The child process calls terminate_now and exits with status 7.",
        code=r"""
#include <stdnoreturn.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

_Noreturn void terminate_now(void)
{
    exit(7);
}

int run_noreturn(void)
{
    pid_t child = fork();
    if (child == 0) {
        terminate_now();
    }
    if (child < 0) {
        return 0;
    }
    int status = 0;
    if (waitpid(child, &status, 0) < 0) {
        return 0;
    }
    return WIFEXITED(status) && WEXITSTATUS(status) == 7;
}
""",
        tests=r"""
CLINGS_CHECK_INT(run_noreturn(), 1);
""",
        breaks=[
            (
                "exit(7);",
                "/* TODO: terminate with status 7. */\n    _Exit(0);",
            )
        ],
    ),
    ex(
        topic="19_modern_c_library",
        slug="02_tgmath",
        title="Type-generic math with tgmath.h",
        objective="Use sqrt with both double and float arguments through tgmath.h.",
        reference="C Primer Plus 第16章 16.10.3",
        hint="tgmath.h selects the correct real function from the argument type.",
        code=r"""
#include <tgmath.h>

double generic_sqrt(double value)
{
    return sqrt(value);
}

float generic_sqrtf(float value)
{
    return sqrt(value);
}
""",
        tests=r"""
CLINGS_CHECK_INT(generic_sqrt(9.0) == 3.0, 1);
CLINGS_CHECK_INT(generic_sqrtf(16.0f) == 4.0f, 1);
""",
        breaks=[
            (
                "float generic_sqrtf(float value)\n{\n    return sqrt(value);\n}",
                "float generic_sqrtf(float value)\n{\n    /* TODO: use type-generic sqrt. */\n    return value;\n}",
            )
        ],
    ),
    ex(
        topic="19_modern_c_library",
        slug="03_atexit",
        title="Registering atexit handlers",
        objective="Register a cleanup function with atexit.",
        reference="C Primer Plus 第16章 16.11.1",
        hint="atexit returns 0 on success and nonzero on failure.",
        code=r"""
#include <stdlib.h>

static void cleanup(void)
{
}

int register_cleanup(void)
{
    return atexit(cleanup) == 0 ? 0 : -1;
}
""",
        tests=r"""
CLINGS_CHECK_INT(register_cleanup(), 0);
""",
        breaks=[
            (
                "return atexit(cleanup) == 0 ? 0 : -1;",
                "/* TODO: register the cleanup function. */\n    return -1;",
            )
        ],
    ),
    ex(
        topic="19_modern_c_library",
        slug="04_atomic_flag",
        title="atomic_flag spin lock",
        objective="Use atomic_flag as a simple test-and-set lock.",
        reference="C Primer Plus 第12章 12.5.4；C11 stdatomic.h",
        hint="atomic_flag_test_and_set returns the previous state.",
        code=r"""
#include <stdatomic.h>

static atomic_flag lock = ATOMIC_FLAG_INIT;

int try_lock_flag(void)
{
    return !atomic_flag_test_and_set(&lock);
}

void unlock_flag(void)
{
    atomic_flag_clear(&lock);
}
""",
        tests=r"""
CLINGS_CHECK_INT(try_lock_flag(), 1);
CLINGS_CHECK_INT(try_lock_flag(), 0);
unlock_flag();
CLINGS_CHECK_INT(try_lock_flag(), 1);
unlock_flag();
""",
        breaks=[
            (
                "atomic_flag_clear(&lock);",
                "/* TODO: release the lock. */",
            )
        ],
    ),
]
