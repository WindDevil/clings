/*
 * clings exercise: 01_types_variables/01_integer_types
 * title: Integer types and ranges
 * objective: Use sizeof, CHAR_BIT, INT_MIN, and INT_MAX correctly.
 * reference: 第一章 1.4 基本数据类型
 * hint: The number of bits in an int is sizeof(int) * CHAR_BIT.
 */

#include "clings/test.h"

#include <limits.h>

int int_bits(void)
{
    /* TODO: measure the width of int, not char. */
    return (int)(sizeof(char) * CHAR_BIT);
}

int long_can_hold_int(long value)
{
    return value >= INT_MIN && value <= INT_MAX;
}

int main(void)
{
    CLINGS_CHECK(int_bits() >= 16);
    CLINGS_CHECK_INT(long_can_hold_int(0), 1);
    CLINGS_CHECK_INT(long_can_hold_int((long)INT_MAX), 1);
    CLINGS_CHECK_INT(long_can_hold_int((long)INT_MAX + 1L), 0);
    return clings_report();
}
