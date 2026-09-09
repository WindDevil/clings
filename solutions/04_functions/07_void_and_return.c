/*
 * clings exercise: 04_functions/07_void_and_return
 * title: void functions and return statements
 * objective: Return early from a void function and return values from int functions.
 * hint: A void function uses a bare return; an int function must return a value.
 */

#include "clings/test.h"

#include <stddef.h>

void set_zero(int *value)
{
    if (value == NULL) {
        return;
    }
    *value = 0;
}

int early_return(int value)
{
    if (value < 0) {
        return -1;
    }
    return value * 2;
}

int main(void)
{
    int value = 5;

    set_zero(&value);
    CLINGS_CHECK_INT(value, 0);
    set_zero(NULL);
    CLINGS_CHECK_INT(value, 0);
    CLINGS_CHECK_INT(early_return(-3), -1);
    CLINGS_CHECK_INT(early_return(4), 8);
    return clings_report();
}
