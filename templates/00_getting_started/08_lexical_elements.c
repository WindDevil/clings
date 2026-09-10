/*
 * clings exercise: 00_getting_started/08_lexical_elements
 * title: Comments, line continuation, and escapes
 * objective: Recognize comments, backslash-newline continuation, and escape sequences.
 * hint: The escaped text contains a real newline, a tab, and quotation marks.
 */

#include "clings/test.h"

#include <string.h>

const char *escaped_text(void)
{
    /* TODO: restore the escape sequences. */
    return "line1 line2 quoted";
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

int main(void)
{
    CLINGS_CHECK_STR(escaped_text(), "line1\nline2\t\"quoted\"");
    CLINGS_CHECK_INT(continued_sum(), 6);
    CLINGS_CHECK_INT(comment_is_ignored(), 3);
    return clings_report();
}
