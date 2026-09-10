/*
 * clings exercise: 20_predefined_macros/01_stdc
 * title: __STDC__
 * objective: Use __STDC__ to detect a conforming C implementation.
 * hint: defined(__STDC__) checks that the macro exists; __STDC__ is 1 for a conforming implementation.
 */

#include "clings/test.h"

int is_standard_c(void)
{
#if defined(__STDC__) && __STDC__
    return 1;
#else
    return 0;
#endif
}

int main(void)
{
    CLINGS_CHECK_INT(is_standard_c(), 1);
    return clings_report();
}
