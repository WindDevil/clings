/*
 * clings exercise: 20_predefined_macros/07_date_time
 * title: __DATE__ and __TIME__
 * objective: Read the compilation date and time.
 * hint: __DATE__ uses the form "Mmm dd yyyy" and __TIME__ uses "hh:mm:ss".
 */

#include "clings/test.h"

#include <string.h>

const char *compilation_date(void)
{
    /* TODO: return the compilation date. */
    return "unknown";
}

const char *compilation_time(void)
{
    return __TIME__;
}

int date_has_expected_shape(void)
{
    const char *date = __DATE__;
    return strlen(date) >= 11 && date[3] == ' ' && date[6] == ' ';
}

int main(void)
{
    CLINGS_CHECK(strlen(compilation_date()) >= 11);
    CLINGS_CHECK(strstr(compilation_time(), ":") != NULL);
    CLINGS_CHECK_INT(date_has_expected_shape(), 1);
    return clings_report();
}
