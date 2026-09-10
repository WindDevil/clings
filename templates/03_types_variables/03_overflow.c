/*
 * clings exercise: 03_types_variables/03_overflow
 * title: Unsigned wrap and checked signed addition
 * objective: Understand modulo wrap and avoid signed integer overflow.
 * hint: Check INT_MAX - b before adding b to a.
 */

#include "clings/test.h"

#include <limits.h>

unsigned wrap_add(unsigned a, unsigned b)
{
    return a + b;
}

int safe_add_int(int a, int b, int *out)
{
    /* TODO: detect overflow before doing the addition. */
    if (0) {
        return -1;
    }
    *out = a + b;
    return 0;
}

int main(void)
{
    int out = 0;

    CLINGS_CHECK_INT(wrap_add(UINT_MAX, 1u), 0);
    CLINGS_CHECK_INT(safe_add_int(INT_MAX, 1, &out), -1);
    CLINGS_CHECK_INT(safe_add_int(INT_MIN, -1, &out), -1);
    CLINGS_CHECK_INT(safe_add_int(2, 3, &out), 0);
    CLINGS_CHECK_INT(out, 5);
    return clings_report();
}
