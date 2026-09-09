/*
 * clings exercise: 11_ub_safety/08_null_pointer
 * title: Null pointer checks
 * objective: Never dereference a null pointer.
 * reference: 第四章 4.1.3 int *p = NULL 和 *p = NULL 有什么区别
 * hint: Use a conditional expression to provide a fallback.
 */

#include "clings/test.h"

int dereference_or_default(const int *pointer, int fallback)
{
    return pointer != NULL ? *pointer : fallback;
}

int main(void)
{
    int value = 42;

    CLINGS_CHECK_INT(dereference_or_default(&value, -1), 42);
    CLINGS_CHECK_INT(dereference_or_default(NULL, -1), -1);
    return clings_report();
}
