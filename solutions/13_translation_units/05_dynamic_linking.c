/*
 * clings exercise: 13_translation_units/05_dynamic_linking
 * title: Dynamic linking with dlopen
 * objective: Load a symbol from a shared library at runtime.
 * hint: Use dlopen, dlsym, and dlclose; convert the object pointer through a union.
 */

#include "clings/test.h"

#include <dlfcn.h>
#include <stddef.h>

typedef size_t (*strlen_function)(const char *);

int dynamic_strlen(void)
{
    void *handle = dlopen("libc.so.6", RTLD_LAZY);
    if (handle == NULL) {
        return -1;
    }

    union {
        void *object;
        strlen_function function;
    } converter;
    converter.object = dlsym(handle, "strlen");
    if (converter.function == NULL) {
        dlclose(handle);
        return -1;
    }

    int result = (int)converter.function("hello");
    dlclose(handle);
    return result;
}

int main(void)
{
    CLINGS_CHECK_INT(dynamic_strlen(), 5);
    return clings_report();
}
