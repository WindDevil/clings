/*
 * clings exercise: 07_dynamic_memory/02_calloc
 * title: Zero-initialized allocation
 * objective: Use calloc when every byte must start as zero.
 * reference: 第五章 5.3.5.3 用 malloc 函数申请 0 字节内存
 * hint: calloc(count, size) returns zeroed memory.
 */

#include "clings/test.h"

#include <stdlib.h>

int *make_zeroed(size_t count)
{
    return calloc(count, sizeof(int));
}

int main(void)
{
    int *values = make_zeroed(5);

    CLINGS_CHECK(values != NULL);
    for (int i = 0; i < 5; ++i) {
        CLINGS_CHECK_INT(values[i], 0);
    }
    free(values);
    return clings_report();
}
