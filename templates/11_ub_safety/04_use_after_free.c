/*
 * clings exercise: 11_ub_safety/04_use_after_free
 * title: Use-after-free
 * objective: Clear a pointer after freeing its target.
 * reference: 第五章 5.3.6 内存已经被释放了，但是继续通过指针来使用
 * hint: Write NULL through the pointer-to-pointer after free.
 */

#include "clings/test.h"

#include <stdlib.h>

void free_and_clear(int **pointer)
{
    free(*pointer);
    /* TODO: clear the caller's pointer. */
}

int is_null(const void *pointer)
{
    return pointer == NULL;
}

int main(void)
{
    int *value = malloc(sizeof *value);

    CLINGS_CHECK(value != NULL);
    *value = 7;
    free_and_clear(&value);
    CLINGS_CHECK_INT(is_null(value), 1);
    return clings_report();
}
