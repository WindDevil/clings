/*
 * clings exercise: 00_basics/07_include_header
 * title: Include a header
 * objective: Include the standard header that declares toupper.
 * hint: The compiler needs a declaration before use; add the header for character functions.
 */

#include "clings/test.h"

#include <ctype.h>

int uppercase_a(void)
{
    return toupper('a');
}

int main(void)
{
    CLINGS_CHECK_INT(uppercase_a(), 'A');
    return clings_report();
}
