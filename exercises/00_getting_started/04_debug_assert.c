/*
 * clings exercise: 00_getting_started/04_debug_assert
 * title: Assertions and defensive programming
 * objective: Use assert for programmer errors and return values for user errors.
 * reference: 第五章 内存管理；调试与测试资料
 * hint: A zero denominator is a normal error, so return -1 instead of dividing.
 */

#include "clings/test.h"

#include <assert.h>

int checked_divide(int numerator, int denominator, int *out)
{
    assert(out != NULL);
    if (denominator == 0) {
        /* TODO: report the error. */
        return 0;
    }
    *out = numerator / denominator;
    return 0;
}

int main(void)
{
    int out = 0;

    CLINGS_CHECK_INT(checked_divide(10, 2, &out), 0);
    CLINGS_CHECK_INT(out, 5);
    CLINGS_CHECK_INT(checked_divide(10, 0, &out), -1);
    return clings_report();
}
