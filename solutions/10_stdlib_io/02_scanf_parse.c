/*
 * clings exercise: 10_stdlib_io/02_scanf_parse
 * title: Parsing with scanf
 * objective: Parse a comma-separated pair with sscanf.
 * reference: 第一章 1.6 条件判断；标准库 scanf 资料
 * hint: The literal comma in the format must match the input.
 */

#include "clings/test.h"

#include <stdio.h>

int parse_pair(const char *input, int *first, int *second)
{
    return sscanf(input, "%d,%d", first, second) == 2 ? 0 : -1;
}

int main(void)
{
    int first = 0;
    int second = 0;

    CLINGS_CHECK_INT(parse_pair("3,4", &first, &second), 0);
    CLINGS_CHECK_INT(first, 3);
    CLINGS_CHECK_INT(second, 4);
    CLINGS_CHECK_INT(parse_pair("3 4", &first, &second), -1);
    return clings_report();
}
