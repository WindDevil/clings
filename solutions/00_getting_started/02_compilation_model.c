/*
 * clings exercise: 00_getting_started/02_compilation_model
 * title: Preprocessing, compiling, and linking
 * objective: See how the preprocessor and the C standard version are exposed.
 * hint: The check requires C11 or newer and compares the result with __STDC_VERSION__.
 */

#include "clings/test.h"

#include <stdio.h>

#if defined(__STDC__) && __STDC__
#define CLINGS_IS_STANDARD_C 1
#else
#define CLINGS_IS_STANDARD_C 0
#endif

int standard_c_year(void)
{
#if defined(__STDC_VERSION__)
    return (int)(__STDC_VERSION__ / 100L);
#else
    return 0;
#endif
}

int main(void)
{
    CLINGS_CHECK_INT(CLINGS_IS_STANDARD_C, 1);
    CLINGS_CHECK(standard_c_year() >= 2011);
    #if defined(__STDC_VERSION__)
    CLINGS_CHECK_INT(standard_c_year(), (int)(__STDC_VERSION__ / 100L));
    #endif
    return clings_report();
}
