/*
 * clings exercise: 02_operators/07_compound_assignment
 * title: Compound assignment and comma
 * objective: Use +=, -=, *=, /=, %= and the comma operator.
 * reference: C Primer Plus 第5章 5.3、第6章 6.6-6.7
 * hint: The comma operator evaluates left to right and yields the right operand.
 */

#include "clings/test.h"

int compound_demo(int value)
{
    value += 3;
    /* TODO: multiply value by 2. */
    value += 2;
    value -= 1;
    value /= 2;
    value %= 5;
    return value;
}

int comma_sum(int left, int right)
{
    int sum = 0;
    sum = (left++, right++, left + right);
    return sum;
}

int main(void)
{
    CLINGS_CHECK_INT(compound_demo(1), 3);
    CLINGS_CHECK_INT(comma_sum(2, 3), 7);
    return clings_report();
}
