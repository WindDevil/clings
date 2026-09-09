/*
 * clings exercise: 09_preprocessor/09_std_macros
 * title: Predefined macros
 * objective: Use __FILE__, __LINE__, __func__, and __STDC_VERSION__.
 * reference: 第三章 3.1 宏定义；编译器预定义宏
 * hint: __func__ is the name of the current function.
 */

#include "clings/test.h"

const char *current_file(void)
{
    return __FILE__;
}

const char *current_function(void)
{
    return __func__;
}

int current_line(void)
{
    return __LINE__;
}

int standard_version(void)
{
    return (int)(__STDC_VERSION__ / 100L);
}

int main(void)
{
    CLINGS_CHECK(strstr(current_file(), "09_std_macros.c") != NULL);
    CLINGS_CHECK_STR(current_function(), "current_function");
    CLINGS_CHECK(current_line() > 0);
    CLINGS_CHECK(standard_version() >= 2011);
    return clings_report();
}
