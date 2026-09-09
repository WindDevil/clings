/*
 * clings exercise: 11_ub_safety/01_signed_overflow
 * title: Avoid signed integer overflow
 * objective: Detect overflow before performing signed addition.
 * reference: 第一章 1.4 signed、unsigned 关键字；第五章 内存管理
 * hint: Unsigned arithmetic wraps; signed overflow is undefined behavior.
 */

#include "clings/test.h"

#include <limits.h>

int checked_add(int a, int b, int *out)
{
    /* TODO: detect overflow before adding. */
    if (0) {
        return -1;
    }
    *out = a + b;
    return 0;
}

int main(void)
{
    int out = 0;

    CLINGS_CHECK_INT(checked_add(INT_MAX, 1, &out), -1);
    CLINGS_CHECK_INT(checked_add(INT_MIN, -1, &out), -1);
    CLINGS_CHECK_INT(checked_add(20, 22, &out), 0);
    CLINGS_CHECK_INT(out, 42);
    return clings_report();
}
