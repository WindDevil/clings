/*
 * clings exercise: 20_predefined_macros/05_line
 * title: __LINE__
 * objective: Use __LINE__ to obtain the current source line number.
 * hint: __LINE__ expands to an integer constant for the current line.
 */

#include "clings/test.h"

int first_line(void)
{
    /* TODO: return the current line number. */
    return 0;
}

int second_line(void)
{
    return __LINE__;
}

int line_numbers_differ(void)
{
    return first_line() != second_line();
}

int main(void)
{
    CLINGS_CHECK(first_line() > 0);
    CLINGS_CHECK_INT(line_numbers_differ(), 1);
    return clings_report();
}
