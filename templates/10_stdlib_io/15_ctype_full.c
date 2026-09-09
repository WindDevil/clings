/*
 * clings exercise: 10_stdlib_io/15_ctype_full
 * title: ctype.h classification and conversion
 * objective: Use isalnum and toupper with unsigned char casts.
 * reference: C Primer Plus 第7章 7.2.2、第11章 11.7
 * hint: Pass (unsigned char) to ctype functions to avoid negative arguments.
 */

#include "clings/test.h"

#include <ctype.h>

int count_alnum(const char *text)
{
    int count = 0;
    for (const char *pointer = text; *pointer != '\0'; ++pointer) {
        /* TODO: classify letters and digits. */
        if (isalpha((unsigned char)*pointer)) {
            ++count;
        }
    }
    return count;
}

char upper_char(char character)
{
    return (char)toupper((unsigned char)character);
}

int main(void)
{
    CLINGS_CHECK_INT(count_alnum("a1 B2!"), 4);
    CLINGS_CHECK_INT(upper_char('q'), 'Q');
    CLINGS_CHECK_INT(upper_char('Z'), 'Z');
    return clings_report();
}
