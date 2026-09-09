/*
 * clings exercise: 10_stdlib_io/05_math_functions
 * title: The math library
 * objective: Use hypot and other functions from math.h.
 * reference: 第一章 1.4 基本数据类型；标准库 math.h 资料
 * hint: hypot(x, y) computes sqrt(x*x + y*y) without avoidable overflow.
 */

#include "clings/test.h"

#include <math.h>

double distance(double x1, double y1, double x2, double y2)
{
    /* TODO: compute the Euclidean distance. */
    return fabs(x2 - x1) + fabs(y2 - y1);
}

int main(void)
{
    CLINGS_CHECK_INT(distance(0.0, 0.0, 3.0, 4.0) == 5.0, 1);
    CLINGS_CHECK_INT(distance(1.0, 1.0, 1.0, 1.0) == 0.0, 1);
    return clings_report();
}
