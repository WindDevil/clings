/*
 * clings exercise: 14_character_io/04_iso646
 * title: iso646.h alternative spellings
 * objective: Use and/or/not from iso646.h.
 * reference: C Primer Plus 第7章 7.3.1
 * hint: iso646.h defines and as && and or as ||.
 */

#include "clings/test.h"

#include <iso646.h>

int is_yes(const char *text)
{
    return /* TODO: accept either y or Y. */
    (text[0] == 'y' and text[0] == 'Y') and text[1] == '\0';
}

int main(void)
{
    CLINGS_CHECK_INT(is_yes("y"), 1);
    CLINGS_CHECK_INT(is_yes("Y"), 1);
    CLINGS_CHECK_INT(is_yes("yes"), 0);
    CLINGS_CHECK_INT(is_yes("n"), 0);
    return clings_report();
}
