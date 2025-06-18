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
    FILE *fptr = fopen(filename, "rb");
    flag = (fptr == NULL) ? 0 : 1;
    if (flag) fclose(fptr);
    return flag;
}

void print_file(const char *filename, char *c, char opt[], int *line_cntr_ptr) {
    // corr_opt = EsbnTvet
    FILE *f_ptr = fopen(filename, "rb");
    int prev_line_empty = 0;
    char next_c;
    while ((next_c = fgetc(f_ptr)) != EOF) {
        if (*c == '\n') {
            if (opt[0] == 'E') option_E(line_cntr_ptr, opt);

            if (opt[1] == 's') option_s(next_c, *c, opt, &prev_line_empty, line_cntr_ptr);
            if (opt[2] == 'b') option_b(next_c, opt, line_cntr_ptr);
            if (opt[3] == 'n') option_n(line_cntr_ptr, opt);
            // no newline opt
            if (opt[0] != 'E' && opt[1] != 's' && opt[2] != 'b' && opt[3] != 'n') {
                if (*line_cntr_ptr) putchar(*c);
                *line_cntr_ptr += 1;
            }

        } else {
            prev_line_empty = 0;
            if (opt[4] == 'T') option_T(*c, opt);
            if (opt[5] == 'v') option_v(*c, opt);
            // no char opt
            if (opt[4] != 'T' && opt[5] != 'v') putchar(*c);
        }

        *c = next_c;
        // GNU: in case of (1||2) \n both at the start && at eof orig cat output is strange
    }

    fclose(f_ptr);
}
