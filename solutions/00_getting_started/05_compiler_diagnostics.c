/*
 * clings exercise: 00_getting_started/05_compiler_diagnostics
 * title: Read compiler diagnostics
 * objective: Fix a format-string warning that the compiler reports.
 * hint: size_t has its own length modifier; do not use %d for it.
 */

#include "clings/test.h"

#include <stdio.h>

int format_size(char *buffer, size_t size, size_t value)
{
    return snprintf(buffer, size, "%zu", value);
}

int main(void)
{
    char buffer[32];

    CLINGS_CHECK_INT(format_size(buffer, sizeof buffer, 123), 3);
    CLINGS_CHECK_STR(buffer, "123");
    return clings_report();
}
