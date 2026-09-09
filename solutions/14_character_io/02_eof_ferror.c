/*
 * clings exercise: 14_character_io/02_eof_ferror
 * title: EOF, feof, and ferror
 * objective: Read until EOF and distinguish end-of-file from an error.
 * hint: feof is true only after a read attempts to pass the end of the file.
 */

#include "clings/test.h"

#include <stdio.h>

int read_all(FILE *file, char *buffer, size_t size)
{
    size_t index = 0;
    int character;
    while (index + 1 < size && (character = fgetc(file)) != EOF) {
        buffer[index] = (char)character;
        ++index;
    }
    buffer[index] = '\0';
    if (ferror(file)) {
        return -1;
    }
    return (int)index;
}

int main(void)
{
    FILE *file = tmpfile();
    char buffer[16];

    CLINGS_CHECK(file != NULL);
    fputs("abc", file);
    rewind(file);
    CLINGS_CHECK_INT(read_all(file, buffer, sizeof buffer), 3);
    CLINGS_CHECK_STR(buffer, "abc");
    CLINGS_CHECK_INT(feof(file), 1);
    fclose(file);
    return clings_report();
}
