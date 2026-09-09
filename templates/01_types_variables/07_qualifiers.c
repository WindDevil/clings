/*
 * clings exercise: 01_types_variables/07_qualifiers
 * title: Type qualifiers and storage-class specifiers
 * objective: Use const, volatile, restrict, extern, auto, and register.
 * reference: 第一章 1.1-1.3 auto、register、static；1.11 const；1.12 volatile；1.13 extern
 * hint: restrict promises that the two pointer parameters do not alias.
 */

#include "clings/test.h"

extern int shared_value;
int shared_value = 42;

int read_const(const int *value)
{
    return *value;
}

int read_volatile(volatile int *value)
{
    return *value;
}

int sum_restrict(const int *restrict left, const int *restrict right)
{
    /* TODO: read both restricted pointers. */
    return *left;
}

int register_sum(void)
{
    register int sum = 0;
    for (register int i = 0; i < 3; ++i) {
        sum += i;
    }
    return sum;
}

int auto_value(void)
{
    auto int value = 5;
    return value;
}

int main(void)
{
    int left = 5;
    int right = 7;
    volatile int volatile_value = 9;

    CLINGS_CHECK_INT(shared_value, 42);
    CLINGS_CHECK_INT(read_const(&left), 5);
    CLINGS_CHECK_INT(read_volatile(&volatile_value), 9);
    CLINGS_CHECK_INT(sum_restrict(&left, &right), 12);
    CLINGS_CHECK_INT(register_sum(), 3);
    CLINGS_CHECK_INT(auto_value(), 5);
    return clings_report();
}
