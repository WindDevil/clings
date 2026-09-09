/*
 * clings exercise: 04_functions/02_parameters_return
 * title: Parameters and return values
 * objective: Return values through parameters and clamp a range.
 * hint: When count is zero, leave the outputs unchanged.
 */

#include "clings/test.h"

int clamp(int value, int low, int high)
{
    if (value < low) {
        /* TODO: clamp to the lower bound. */
        return high;
    }
    if (value > high) {
        return high;
    }
    return value;
}

void min_max(const int *values, int count, int *min_out, int *max_out)
{
    if (count <= 0 || values == NULL || min_out == NULL || max_out == NULL) {
        return;
    }

    int minimum = values[0];
    int maximum = values[0];
    for (int i = 1; i < count; ++i) {
        if (values[i] < minimum) {
            minimum = values[i];
        }
        if (values[i] > maximum) {
            maximum = values[i];
        }
    }
    *min_out = minimum;
    *max_out = maximum;
}

int main(void)
{
    const int values[] = {4, -2, 9, 1};
    int minimum = 0;
    int maximum = 0;

    CLINGS_CHECK_INT(clamp(5, 1, 10), 5);
    CLINGS_CHECK_INT(clamp(0, 1, 10), 1);
    CLINGS_CHECK_INT(clamp(11, 1, 10), 10);
    min_max(values, 4, &minimum, &maximum);
    CLINGS_CHECK_INT(minimum, -2);
    CLINGS_CHECK_INT(maximum, 9);
    return clings_report();
}
