/*
 * clings exercise: 00_getting_started/02_compilation_model
 * title: Headers and declarations
 * objective: Include the standard header that declares INT_MAX.
 * hint: The compiler needs a declaration before use; add the header for integer limits.
 */

#include "clings/test.h"

/* TODO: include the header that declares INT_MAX. */
int largest_int(void)
{
    return INT_MAX;
}

int main(void)
{
    CLINGS_CHECK_INT(largest_int(), INT_MAX);
    return clings_report();
}
