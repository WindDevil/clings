/*
 * clings exercise: 09_preprocessor/11_macro_whitespace
 * title: Whitespace in macro definitions
 * objective: Remember that a space can turn a function-like macro into an object-like macro.
 * reference: C 陷阱与缺陷 6.1
 * hint: The ( must immediately follow the macro name.
 */

#include "clings/test.h"

/* TODO: keep the ( immediately after SQUARE. */
#define SQUARE (value) ((value) * (value))

int square_value(int value)
{
    return SQUARE(value);
}

int main(void)
{
    CLINGS_CHECK_INT(square_value(4), 16);
    CLINGS_CHECK_INT(SQUARE(3), 9);
    return clings_report();
}
