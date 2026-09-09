/*
 * clings exercise: 00_getting_started/01_hello_world
 * title: Hello, C!
 * objective: Understand the minimal C program and formatted output.
 * reference: 第一章 前言；任意 C 入门章节
 * hint: Use snprintf(buffer, size, ...) and the exact string from the test.
 */

#include "clings/test.h"

#include <stdio.h>

int print_greeting(char *buffer, size_t size)
{
    return snprintf(buffer, size, "Hello, C!");
}

int main(void)
{
    char buffer[32];

    CLINGS_CHECK_INT(print_greeting(buffer, sizeof buffer), 9);
    CLINGS_CHECK_STR(buffer, "Hello, C!");
    return clings_report();
}
