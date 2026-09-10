"""Exercises for standard predefined macros."""

from spec import ex

SPECS = [
    ex(
        topic="20_predefined_macros",
        slug="01_stdc",
        title="__STDC__",
        objective="Use __STDC__ to detect a conforming C implementation.",
        reference="",
        hint="defined(__STDC__) checks that the macro exists; __STDC__ is 1 for a conforming implementation.",
        code=r"""
int is_standard_c(void)
{
#if defined(__STDC__) && __STDC__
    return 1;
#else
    return 0;
#endif
}
""",
        tests=r"""
CLINGS_CHECK_INT(is_standard_c(), 1);
""",
        breaks=[
            (
                "#if defined(__STDC__) && __STDC__\n    return 1;\n#else\n    return 0;\n#endif",
                "/* TODO: detect a conforming C implementation. */\n    return 0;",
            )
        ],
    ),
    ex(
        topic="20_predefined_macros",
        slug="02_stdc_version",
        title="__STDC_VERSION__",
        objective="Read the C standard version from __STDC_VERSION__.",
        reference="",
        hint="__STDC_VERSION__ is 201710L for C17; divide by 100 to get the year.",
        code=r"""
int standard_c_year(void)
{
#if defined(__STDC_VERSION__)
    return (int)(__STDC_VERSION__ / 100L);
#else
    return 0;
#endif
}
""",
        tests=r"""
CLINGS_CHECK(standard_c_year() >= 2011);
#if defined(__STDC_VERSION__)
CLINGS_CHECK_INT(standard_c_year(), (int)(__STDC_VERSION__ / 100L));
#endif
""",
        breaks=[
            (
                "#if defined(__STDC_VERSION__)\n    return (int)(__STDC_VERSION__ / 100L);\n#else\n    return 0;\n#endif",
                "/* TODO: return the C standard year. */\n    return 0;",
            )
        ],
    ),
    ex(
        topic="20_predefined_macros",
        slug="03_stdc_hosted",
        title="__STDC_HOSTED__",
        objective="Distinguish hosted and freestanding implementations.",
        reference="",
        hint="__STDC_HOSTED__ is 1 for a hosted implementation and 0 for freestanding.",
        code=r"""
int is_hosted_implementation(void)
{
#if defined(__STDC_HOSTED__)
    return __STDC_HOSTED__;
#else
    return 0;
#endif
}
""",
        tests=r"""
CLINGS_CHECK_INT(is_hosted_implementation(), 1);
""",
        breaks=[
            (
                "#if defined(__STDC_HOSTED__)\n    return __STDC_HOSTED__;\n#else\n    return 0;\n#endif",
                "/* TODO: return the hosted/freestanding indicator. */\n    return 0;",
            )
        ],
    ),
    ex(
        topic="20_predefined_macros",
        slug="04_file",
        title="__FILE__",
        objective="Use __FILE__ to obtain the current source file name.",
        reference="",
        hint="__FILE__ expands to a string literal.",
        code=r"""
const char *current_file_name(void)
{
    return __FILE__;
}
""",
        tests=r"""
CLINGS_CHECK(strstr(current_file_name(), "04_file.c") != NULL);
""",
        breaks=[
            (
                "return __FILE__;",
                "/* TODO: return the current file name. */\n    return \"unknown.c\";",
            )
        ],
    ),
    ex(
        topic="20_predefined_macros",
        slug="05_line",
        title="__LINE__",
        objective="Use __LINE__ to obtain the current source line number.",
        reference="",
        hint="__LINE__ expands to an integer constant for the current line.",
        code=r"""
int first_line(void)
{
    return __LINE__;
}

int second_line(void)
{
    return __LINE__;
}

int line_numbers_differ(void)
{
    return first_line() != second_line();
}
""",
        tests=r"""
CLINGS_CHECK(first_line() > 0);
CLINGS_CHECK_INT(line_numbers_differ(), 1);
""",
        breaks=[
            (
                "return __LINE__;",
                "/* TODO: return the current line number. */\n    return 0;",
            )
        ],
    ),
    ex(
        topic="20_predefined_macros",
        slug="06_func",
        title="__func__",
        objective="Use __func__ to obtain the current function name.",
        reference="",
        hint="__func__ is a predefined identifier, not a macro.",
        code=r"""
const char *current_function_name(void)
{
    return __func__;
}
""",
        tests=r"""
CLINGS_CHECK_STR(current_function_name(), "current_function_name");
""",
        breaks=[
            (
                "return __func__;",
                "/* TODO: return the current function name. */\n    return \"other\";",
            )
        ],
    ),
    ex(
        topic="20_predefined_macros",
        slug="07_date_time",
        title="__DATE__ and __TIME__",
        objective="Read the compilation date and time.",
        reference="",
        hint="__DATE__ uses the form \"Mmm dd yyyy\" and __TIME__ uses \"hh:mm:ss\".",
        code=r"""
#include <string.h>

const char *compilation_date(void)
{
    return __DATE__;
}

const char *compilation_time(void)
{
    return __TIME__;
}

int date_has_expected_shape(void)
{
    const char *date = __DATE__;
    return strlen(date) >= 11 && date[3] == ' ' && date[6] == ' ';
}
""",
        tests=r"""
CLINGS_CHECK(strlen(compilation_date()) >= 11);
CLINGS_CHECK(strstr(compilation_time(), ":") != NULL);
CLINGS_CHECK_INT(date_has_expected_shape(), 1);
""",
        breaks=[
            (
                "return __DATE__;",
                "/* TODO: return the compilation date. */\n    return \"unknown\";",
            )
        ],
    ),
    ex(
        topic="20_predefined_macros",
        slug="08_optional_features",
        title="Optional-feature macros",
        objective="Detect unavailable optional C features with __STDC_NO_* macros.",
        reference="",
        hint="If __STDC_NO_ATOMICS__ is not defined, atomics are available.",
        code=r"""
int has_atomics(void)
{
#if defined(__STDC_NO_ATOMICS__)
    return 0;
#else
    return 1;
#endif
}

int has_threads(void)
{
#if defined(__STDC_NO_THREADS__)
    return 0;
#else
    return 1;
#endif
}

int has_iec_559(void)
{
#if defined(__STDC_IEC_559__) && __STDC_IEC_559__
    return 1;
#else
    return 0;
#endif
}
""",
        tests=r"""
CLINGS_CHECK_INT(has_atomics(), 1);
CLINGS_CHECK_INT(has_threads(), 1);
CLINGS_CHECK_INT(has_iec_559(), 1);
""",
        breaks=[
            (
                "#if defined(__STDC_NO_ATOMICS__)\n    return 0;\n#else\n    return 1;\n#endif",
                "/* TODO: detect whether atomics are unavailable. */\n    return 0;",
            )
        ],
    ),
]
