#include "options_func.h"

#include <stdio.h>

void option_s(char next_c, char c, char opt[], int *prev_line_empty, int *line_cntr, int *next_file_ptr) {
    if (opt[1] == 'b') opt[2] = '_';

    if (next_c == c && *prev_line_empty == 0) {
        *prev_line_empty = 1;
        putchar(c);

    } else if (next_c != c && (*prev_line_empty == 0 || *prev_line_empty > 0)) {
        // next if used to avoid first blank line
        if (*line_cntr != 0 && *next_file_ptr != 1)
            putchar(c);
        else
            *line_cntr = 1;
    }
}

void option_b(char next_c, char *c, char opt[], int *line_cntr, int *next_file_ptr) {
    if (next_c != '\n') {
        if (*line_cntr) {
            if (!*next_file_ptr) {
                if (opt[0] == 's') {
                    printf("     %d	", *line_cntr);
                    *line_cntr += 1;
                } else {
                    *line_cntr += 1;
                    printf("\n     %d	", *line_cntr);
                }
            } else {
                if (opt[0] == 's') {
                    if (*c == '\n') {
                        printf("     %d	", *line_cntr);
                        *line_cntr += 1;
                    }
                } else {
                    *line_cntr += 1;
                    printf("     %d	", *line_cntr);
                }
            }
        } else {
            *line_cntr += 1;
            printf("     %d	", *line_cntr);
        }

    } else if (opt[0] != 's')
        putchar(next_c);
}

void option_n(int *line_cntr) {
    // if !s
    if (*line_cntr != 0) {
        *line_cntr += 1;
        printf("\n     %d  ", *line_cntr);
    } else {
        *line_cntr = 1;
        printf("     %d  ", *line_cntr);
    }
}

void option_v() {}

void option_E() {}

void option_e() {}

void option_T() {}

void option_t() {}