/*
 * clings exercise: 06_pointers/06_dangling_wild
 * title: Dangling pointers and safe free
 * objective: Set a freed pointer to NULL to prevent accidental reuse.
 * reference: 第五章 5.1 什么是野指针；5.3.5 内存泄漏
 * hint: After free(*pointer), assign NULL through the pointer-to-pointer.
 */

#include "clings/test.h"

#include <stdlib.h>

void safe_free(int **pointer)
{
    free(*pointer);
    /* TODO: make the caller's pointer null after freeing it. */
}

int is_null(const void *pointer)
{
    return pointer == NULL;
}

int main(void)
{
    int *value = malloc(sizeof *value);

    CLINGS_CHECK(value != NULL);
    *value = 42;
    safe_free(&value);
    CLINGS_CHECK_INT(is_null(value), 1);
    return clings_report();
}
