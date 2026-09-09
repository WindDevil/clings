/*
 * clings exercise: 05_arrays_strings/06_safe_format
 * title: Bounded formatting with snprintf
 * objective: Format text into a fixed-size buffer without overflow.
 * hint: Keep the space between the first and last name.
 */

#include "clings/test.h"

#include <stdio.h>

int format_name(char *buffer, size_t size, const char *first, const char *last)
{
    return snprintf(buffer, size, "%s %s", first, last);
}

int main(void)
{
    char buffer[8];

    CLINGS_CHECK_INT(format_name(buffer, sizeof buffer, "Ada", "Lovelace"), 12);
    CLINGS_CHECK_STR(buffer, "Ada Lov");
    return clings_report();
}
