/*
 * clings exercise: 09_preprocessor/08_pragma_error_line
 * title: #error, #line, and #pragma pack
 * objective: Use diagnostics, line control, and packing pragmas.
 * reference: 第三章 3.4 #error；3.5 #line；3.6.8 #pragma pack
 * hint: #pragma pack(push, 1) removes padding between the two members.
 */

#include "clings/test.h"

#include <stddef.h>

#if 0
#error "this branch is disabled"
#endif

/* TODO: pack the struct without padding. */
#pragma pack(push, 4)
struct packed {
    char first;
    int second;
};
#pragma pack(pop)

int packed_size(void)
{
    return (int)sizeof(struct packed);
}

int line_number(void)
{
#line 1000
    return __LINE__;
}

int main(void)
{
    CLINGS_CHECK_INT(packed_size(), (int)(sizeof(char) + sizeof(int)));
    CLINGS_CHECK_INT(line_number(), 1000);
    return clings_report();
}
