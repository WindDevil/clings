/*
 * clings exercise: 10_stdlib_io/16_rand_max
 * title: RAND_MAX portability
 * objective: Do not assume rand() returns a value below a fixed small bound.
 * reference: C 陷阱与缺陷 7.8
 * hint: The C standard only guarantees RAND_MAX >= 32767.
 */

#include "clings/test.h"

#include <stdlib.h>

int rand_max_is_at_least_32767(void)
{
    /* TODO: use the standard minimum guarantee. */
    return RAND_MAX == 32767;
}

int bounded_rand(int upper)
{
    return upper > 0 ? rand() % upper : 0;
}

int main(void)
{
    CLINGS_CHECK_INT(rand_max_is_at_least_32767(), 1);
    srand(42u);
    int value = bounded_rand(10);
    CLINGS_CHECK(value >= 0 && value < 10);
    return clings_report();
}
