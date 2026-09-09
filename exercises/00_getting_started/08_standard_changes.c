/*
 * clings exercise: 00_getting_started/08_standard_changes
 * title: C standard changes
 * objective: Detect the C standard version at compile time.
 * reference: C 陷阱与缺陷 7.1
 * hint: __STDC_VERSION__ is 201112L for C11 and 201710L for C17.
 */

#include "clings/test.h"

int c_standard_year(void)
{
    return (int)(__STDC_VERSION__ / 100L);
}

int has_c11(void)
{
#if defined(__STDC_VERSION__) && /* TODO: test for C11 or newer. */
__STDC_VERSION__ >= 999999L
    return 1;
#else
    return 0;
#endif
}

int main(void)
{
    CLINGS_CHECK(c_standard_year() >= 2011);
    CLINGS_CHECK_INT(has_c11(), 1);
    return clings_report();
}
