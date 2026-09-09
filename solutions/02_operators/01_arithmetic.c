/*
 * clings exercise: 02_operators/01_arithmetic
 * title: Integer arithmetic
 * objective: Practice integer division, modulo, and truncation.
 * reference: 第二章 2.4 逻辑运算符；2.8 除法
 * hint: Integer division truncates toward zero.
 */

#include "clings/test.h"

int quotient(int a, int b)
{
    return a / b;
}

int int_remainder(int a, int b)
{
    return a % b;
}

int average_floor(int a, int b)
{
    return (a + b) / 2;
}

int main(void)
{
    CLINGS_CHECK_INT(quotient(7, 3), 2);
    CLINGS_CHECK_INT(quotient(-7, 3), -2);
    CLINGS_CHECK_INT(int_remainder(7, 3), 1);
    CLINGS_CHECK_INT(average_floor(2, 3), 2);
    return clings_report();
}
