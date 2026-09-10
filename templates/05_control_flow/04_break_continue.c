/*
 * clings exercise: 05_control_flow/04_break_continue
 * title: break and continue
 * objective: Use break to stop early and continue to skip one iteration.
 * hint: continue skips the rest of the current iteration; break exits the loop.
 */

#include "clings/test.h"

int first_even(const int *values, int count)
{
    for (int i = 0; i < count; ++i) {
        if (values[i] % 2 == 0) {
            return values[i];
        }
    }
    return -1;
}

int sum_positive(const int *values, int count)
{
    int sum = 0;
    for (int i = 0; i < count; ++i) {
        if (values[i] <= 0) {
            /* TODO: skip this value, do not stop the loop. */
            break;
        }
        sum += values[i];
    }
    return sum;
}

int main(void)
{
    const int values[] = {1, -3, 4, 5, -6};

    CLINGS_CHECK_INT(first_even(values, 5), 4);
    CLINGS_CHECK_INT(sum_positive(values, 5), 10);
    CLINGS_CHECK_INT(sum_positive((const int[]){-1, -2}, 2), 0);
    return clings_report();
}
