/*
 * clings exercise: 01_types_variables/03_overflow
 * title: Unsigned wrap and checked signed addition
 * objective: Understand modulo wrap and avoid signed integer overflow.
 * reference: 第一章 1.4 基本数据类型；第五章 内存管理
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
    if ((b > 0 && a > INT_MAX - b) || (b < 0 && a < INT_MIN - b)) {
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
