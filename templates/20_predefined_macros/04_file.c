/*
 * clings exercise: 20_predefined_macros/04_file
 * title: __FILE__
 * objective: Use __FILE__ to obtain the current source file name.
 * hint: __FILE__ expands to a string literal.
 */

#include "clings/test.h"

const char *current_file_name(void)
{
    /* TODO: return the current file name. */
    return "unknown.c";
}

int main(void)
{
    CLINGS_CHECK(strstr(current_file_name(), "04_file.c") != NULL);
    return clings_report();
}
