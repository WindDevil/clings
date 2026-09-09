/*
 * clings exercise: 00_getting_started/01_hello_world
 * title: Hello, C!
 * objective: Understand the minimal C program and formatted output.
 * hint: Use snprintf(buffer, size, ...) and the exact string from the test.
 */

#include "clings/test.h"

#include <stdio.h>

int print_greeting(char *buffer, size_t size)
{
    /* TODO: write the greeting into buffer. */
    return snprintf(buffer, size, "Hello, world!");
}

int main(void)
{
    char buffer[32];

    CLINGS_CHECK_INT(print_greeting(buffer, sizeof buffer), 9);
    CLINGS_CHECK_STR(buffer, "Hello, C!");
    return clings_report();
}
