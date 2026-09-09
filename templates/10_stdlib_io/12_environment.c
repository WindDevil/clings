/*
 * clings exercise: 10_stdlib_io/12_environment
 * title: Environment variables
 * objective: Read and write environment variables with getenv and setenv.
 * reference: 第五章 5.3.1.3 函数的入口校验；标准库 stdlib.h 资料
 * hint: setenv must succeed before getenv can find the new value.
 */

#include "clings/test.h"

#include <stdio.h>
#include <stdlib.h>

int set_and_get(const char *name, const char *value, char *out, size_t size)
{
    if (setenv(name, value, 1) != 0) {
        return -1;
    }
    /* TODO: read the environment variable back. */
    const char *found = NULL;
    if (found == NULL) {
        return -1;
    }
    snprintf(out, size, "%s", found);
    return 0;
}

int main(void)
{
    char buffer[32];
    const char *name = "CLINGS_TEST_ENV_VARIABLE";

    CLINGS_CHECK_INT(
        set_and_get(name, "hello", buffer, sizeof buffer), 0);
    CLINGS_CHECK_STR(buffer, "hello");
    unsetenv(name);
    return clings_report();
}
