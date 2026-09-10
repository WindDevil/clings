/*
 * clings exercise: 20_predefined_macros/06_func
 * title: __func__
 * objective: Use __func__ to obtain the current function name.
 * hint: __func__ is a predefined identifier, not a macro.
 */

#include "clings/test.h"

const char *current_function_name(void)
{
    /* TODO: return the current function name. */
    return "other";
}

int main(void)
{
    CLINGS_CHECK_STR(current_function_name(), "current_function_name");
    return clings_report();
}
