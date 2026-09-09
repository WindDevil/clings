#ifndef CLINGS_TEST_H
#define CLINGS_TEST_H

/*
 * Minimal, dependency-free test harness for clings exercises.
 *
 * Every exercise is a normal C program.  The exercise's main() calls
 * CLINGS_CHECK(...) for each expectation and finishes with clings_report().
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int clings_failures = 0;
static int clings_checks = 0;

static inline void clings_record(int passed, const char *expr, const char *file,
                                 int line)
{
    ++clings_checks;
    if (passed) {
        printf("  ok   %s\n", expr);
        return;
    }

    ++clings_failures;
    fprintf(stderr, "  FAIL %s:%d: %s\n", file, line, expr);
}

#define CLINGS_CHECK(expr) \
    clings_record(!!((expr)), #expr, __FILE__, __LINE__)

#define CLINGS_CHECK_MSG(expr, message)                                      \
    do {                                                                     \
        if (!(expr)) {                                                       \
            ++clings_checks;                                                 \
            ++clings_failures;                                               \
            fprintf(stderr, "  FAIL %s:%d: %s (%s)\n", __FILE__, __LINE__,   \
                    #expr, (message));                                       \
        } else {                                                             \
            ++clings_checks;                                                 \
            printf("  ok   %s\n", #expr);                                    \
        }                                                                    \
    } while (0)

#define CLINGS_CHECK_INT(actual, expected)                                    \
    do {                                                                      \
        long long clings_actual_ = (long long)(actual);                       \
        long long clings_expected_ = (long long)(expected);                   \
        if (clings_actual_ != clings_expected_) {                             \
            ++clings_checks;                                                  \
            ++clings_failures;                                                \
            fprintf(stderr, "  FAIL %s:%d: %s == %s (got %lld, want %lld)\n", \
                    __FILE__, __LINE__, #actual, #expected, clings_actual_,    \
                    clings_expected_);                                        \
        } else {                                                              \
            ++clings_checks;                                                  \
            printf("  ok   %s == %s\n", #actual, #expected);                  \
        }                                                                     \
    } while (0)

#define CLINGS_CHECK_STR(actual, expected)                                    \
    do {                                                                      \
        const char *clings_actual_ = (actual);                                \
        const char *clings_expected_ = (expected);                            \
        if (clings_actual_ == NULL || clings_expected_ == NULL ||             \
            strcmp(clings_actual_, clings_expected_) != 0) {                  \
            ++clings_checks;                                                  \
            ++clings_failures;                                                \
            fprintf(stderr, "  FAIL %s:%d: %s == %s (got \"%s\", want \"%s\")\n", \
                    __FILE__, __LINE__, #actual, #expected,                   \
                    clings_actual_ ? clings_actual_ : "(null)",               \
                    clings_expected_ ? clings_expected_ : "(null)");          \
        } else {                                                              \
            ++clings_checks;                                                  \
            printf("  ok   %s == %s\n", #actual, #expected);                  \
        }                                                                     \
    } while (0)

#define CLINGS_CHECK_MEM(actual, expected, size)                              \
    do {                                                                      \
        if (memcmp((actual), (expected), (size)) != 0) {                      \
            ++clings_checks;                                                  \
            ++clings_failures;                                                \
            fprintf(stderr, "  FAIL %s:%d: memory differs: %s vs %s\n",       \
                    __FILE__, __LINE__, #actual, #expected);                  \
        } else {                                                              \
            ++clings_checks;                                                  \
            printf("  ok   %s memory == %s\n", #actual, #expected);           \
        }                                                                     \
    } while (0)

static int clings_report(void)
{
    if (clings_failures == 0) {
        printf("\nAll %d checks passed.\n", clings_checks);
        return EXIT_SUCCESS;
    }

    fprintf(stderr, "\n%d of %d checks failed.\n", clings_failures,
            clings_checks);
    return EXIT_FAILURE;
}

#endif /* CLINGS_TEST_H */
