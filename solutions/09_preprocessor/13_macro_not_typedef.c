/*
 * clings exercise: 09_preprocessor/13_macro_not_typedef
 * title: Macros are not type definitions
 * objective: Use typedef instead of an object-like macro for pointer types.
 * reference: C 陷阱与缺陷 6.4
 * hint: INT_POINTER a, b declares b as int, not int *.
 */

#include "clings/test.h"

#include <stddef.h>

typedef int *int_pointer;
#define INT_POINTER int *

int_pointer first = NULL;
int_pointer second = NULL;

int main(void)
{
    CLINGS_CHECK_INT((int)sizeof first, (int)sizeof(int *));
    CLINGS_CHECK_INT((int)sizeof second, (int)sizeof(int *));
    return clings_report();
}
