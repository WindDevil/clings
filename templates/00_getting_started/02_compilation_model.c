/*
 * clings exercise: 00_getting_started/02_compilation_model
 * title: Preprocessing, compiling, and linking
 * objective: See how the preprocessor and the C standard version are exposed.
 * hint: The runner compiles with -std=c17, so __STDC_VERSION__ is 201710L.
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
    /* TODO: return the standard year, not a placeholder. */
    return 0;
#else
    return 0;
#endif
}

int main(void)
{
    CLINGS_CHECK_INT(CLINGS_IS_STANDARD_C, 1);
    CLINGS_CHECK_INT(standard_c_year(), 2017);
    return clings_report();
}
