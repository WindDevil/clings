/*
 * clings exercise: 12_advanced_c/07_align
 * title: alignof and alignas
 * objective: Query and request alignment.
 * reference: C11 标准 alignof/alignas 资料
 * hint: Double usually requires more alignment than int.
 */

#include "clings/test.h"

#include <stdalign.h>

int align_of_int(void)
{
    return (int)alignof(int);
}

int align_of_double(void)
{
    /* TODO: report the alignment of double. */
    return 1;
}

int main(void)
{
    CLINGS_CHECK(align_of_int() >= (int)alignof(short));
    CLINGS_CHECK(align_of_double() >= align_of_int());
    return clings_report();
}
