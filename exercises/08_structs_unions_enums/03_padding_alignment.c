/*
 * clings exercise: 08_structs_unions_enums/03_padding_alignment
 * title: Padding and alignment
 * objective: Observe padding and member offsets with offsetof.
 * reference: 第一章 1.14.1 空结构体多大；第三章 3.6.8 #pragma pack
 * hint: offsetof takes the struct type and the member name.
 */

#include "clings/test.h"

#include <stddef.h>

struct padded {
    char first;
    int value;
    char last;
};

int value_offset(void)
{
    /* TODO: measure the offset of the value member. */
    return (int)offsetof(struct padded, first);
}

int padded_size(void)
{
    return (int)sizeof(struct padded);
}

int main(void)
{
    CLINGS_CHECK(value_offset() >= (int)sizeof(char));
    CLINGS_CHECK(padded_size() >= value_offset() + (int)sizeof(int) + 1);
    CLINGS_CHECK_INT((int)sizeof(struct padded) % (int)sizeof(int), 0);
    return clings_report();
}
