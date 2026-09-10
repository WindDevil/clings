/*
 * clings exercise: 20_predefined_macros/02_stdc_version
 * title: __STDC_VERSION__
 * objective: Read the C standard version from __STDC_VERSION__.
 * hint: __STDC_VERSION__ is 201710L for C17; divide by 100 to get the year.
 */

#include "clings/test.h"

int standard_c_year(void)
{
/* TODO: return the C standard year. */
    return 0;
}

int main(void)
{
    CLINGS_CHECK(standard_c_year() >= 2011);
    #if defined(__STDC_VERSION__)
    CLINGS_CHECK_INT(standard_c_year(), (int)(__STDC_VERSION__ / 100L));
    #endif
    return clings_report();
}
