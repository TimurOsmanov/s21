#include "files_func.h"

#include <stdio.h>

#include "options_func.h"

int count_files_names(int argc, char *argv[]) {
    int c = 0;
    for (int i = 1; i < argc; i++) {
        if (argv[i][0] != '-') {
            c++;
        }
    }
    return c;
}

int check_file(const char *filename) {
    int flag = 0;
    FILE *fptr = fopen(filename, "r");
    flag = (fptr == NULL) ? 0 : 1;
    if (flag) fclose(fptr);
    return flag;
}

void print_file(const char *filename, char *c, char opt[], int *line_cntr_ptr, int *next_file_ptr) {
    // sbneEtTv
    FILE *fptr = fopen(filename, "r");
    int prev_line_empty = 0;
    char next_c;
    while ((next_c = fgetc(fptr)) != EOF) {
        if (*c == '\n') {
            if (opt[0] == 's') option_s(next_c, *c, opt, &prev_line_empty, line_cntr_ptr, next_file_ptr);
            if (opt[1] == 'b') option_b(next_c, c, opt, line_cntr_ptr, next_file_ptr);
            if (opt[2] == 'n') option_n(line_cntr_ptr);
        } else {
            prev_line_empty = 0;
            if (opt[3] == 'e') option_e();
            if (opt[4] == 't') option_t();
            if (opt[5] == 'E') option_E();
            if (opt[6] == 'T') option_T();
            if (opt[7] == 'v') option_v();

            if (!*next_file_ptr) putchar(*c);
        }

        *c = next_c;
        if (*next_file_ptr) *next_file_ptr = 0;
    }
    //  last char
    putchar(*c);
    *next_file_ptr = 1;
    fclose(fptr);
}
