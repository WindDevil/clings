/*
 * clings exercise: 20_predefined_macros/08_optional_features
 * title: Optional-feature macros
 * objective: Detect unavailable optional C features with __STDC_NO_* macros.
 * hint: If __STDC_NO_ATOMICS__ is not defined, atomics are available.
 */

#include "clings/test.h"

int has_atomics(void)
{
#if defined(__STDC_NO_ATOMICS__)
    return 0;
#else
    return 1;
#endif
}

int has_threads(void)
{
#if defined(__STDC_NO_THREADS__)
    return 0;
#else
    return 1;
#endif
}

int has_iec_559(void)
{
#if defined(__STDC_IEC_559__) && __STDC_IEC_559__
    return 1;
#else
    return 0;
#endif
}

int main(void)
{
    CLINGS_CHECK_INT(has_atomics(), 1);
    CLINGS_CHECK_INT(has_threads(), 1);
    CLINGS_CHECK_INT(has_iec_559(), 1);
    return clings_report();
}
