/*
 * clings exercise: 00_getting_started/07_main_return_value
 * title: main return values
 * objective: Return a defined success or failure status from a program.
 * reference: C 陷阱与缺陷 3.10
 * hint: EXIT_SUCCESS is 0 on hosted implementations; EXIT_FAILURE is nonzero.
 */

#include "clings/test.h"

#include <stdlib.h>

int exit_code_for(int success)
{
    /* TODO: return success for success and failure otherwise. */
    return success ? EXIT_FAILURE : EXIT_SUCCESS;
}

int main(void)
{
    CLINGS_CHECK_INT(exit_code_for(1), EXIT_SUCCESS);
    CLINGS_CHECK_INT(exit_code_for(0), EXIT_FAILURE);
    return clings_report();
}
