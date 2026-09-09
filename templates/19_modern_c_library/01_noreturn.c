/*
 * clings exercise: 19_modern_c_library/01_noreturn
 * title: _Noreturn functions
 * objective: Declare a function that never returns and observe its exit status.
 * reference: C Primer Plus 第16章 16.8
 * hint: The child process calls terminate_now and exits with status 7.
 */

#include "clings/test.h"

#include <stdnoreturn.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

_Noreturn void terminate_now(void)
{
    /* TODO: terminate with status 7. */
    _Exit(0);
}

int run_noreturn(void)
{
    pid_t child = fork();
    if (child == 0) {
        terminate_now();
    }
    if (child < 0) {
        return 0;
    }
    int status = 0;
    if (waitpid(child, &status, 0) < 0) {
        return 0;
    }
    return WIFEXITED(status) && WEXITSTATUS(status) == 7;
}

int main(void)
{
    CLINGS_CHECK_INT(run_noreturn(), 1);
    return clings_report();
}
