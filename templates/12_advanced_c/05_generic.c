/*
 * clings exercise: 12_advanced_c/05_generic
 * title: _Generic selection
 * objective: Choose an expression based on the type of a value.
 * reference: C11 标准 _Generic 资料
 * hint: The controlling expression is not evaluated; only its type is used.
 */

#include "clings/test.h"

#define type_name(value)                                                     \
    _Generic((value), /* TODO: return "int" for the int case. */ int: "integer", double: "double", char *: "char *",        \
             default: "other")

int main(void)
{
    CLINGS_CHECK_STR(type_name(1), "int");
    CLINGS_CHECK_STR(type_name(1.0), "double");
    CLINGS_CHECK_STR(type_name("text"), "char *");
    CLINGS_CHECK_STR(type_name(1L), "other");
    return clings_report();
}
