/*
 * clings exercise: 20_predefined_macros/03_stdc_hosted
 * title: __STDC_HOSTED__
 * objective: Distinguish hosted and freestanding implementations.
 * hint: __STDC_HOSTED__ is 1 for a hosted implementation and 0 for freestanding.
 */

#include "clings/test.h"

int is_hosted_implementation(void)
{
/* TODO: return the hosted/freestanding indicator. */
    return 0;
}

int main(void)
{
    CLINGS_CHECK_INT(is_hosted_implementation(), 1);
    return clings_report();
}
