#include "options_func.h"

#include <stdio.h>

#define GNU_SPACES 5

void print_num(int line_cntr) {
    int order = 0;
    int copy_line_cntr = line_cntr;
    while (copy_line_cntr / 10 != 0) {
        copy_line_cntr /= 10;
        order++;
    }
    for (int i = 0; i < GNU_SPACES - order; i++) printf(" ");

    printf("%d	", line_cntr);
}

void option_s(char next_c, char c, char opt[], int *prev_line_empty, int *line_cntr) {
    if (next_c == c && !*prev_line_empty) {
        *prev_line_empty = 1;
        if (opt[0] == 'E') printf("$");
        putchar(c);
        if (opt[3] == 'n') {
            *line_cntr += 1;
            print_num(*line_cntr);
        };

    } else if (next_c != c) {
        if (!*line_cntr) {
            *line_cntr = 1;
            if (opt[2] == 'b' || opt[3] == 'n') print_num(*line_cntr);
        } else {
            if (opt[0] == 'E') printf("$");
            putchar(c);
            *line_cntr += 1;
            if (opt[2] == 'b' || opt[3] == 'n') print_num(*line_cntr);
        }
    }
}

void option_b(char next_c, char opt[], int *line_cntr) {
    if (opt[1] != 's') {
        if (next_c != '\n') {
            if (!*line_cntr) {
                *line_cntr = 1;
                print_num(*line_cntr);
            } else {
                *line_cntr += 1;
                if (opt[0] == 'E') printf("$");
                printf("\n");
                print_num(*line_cntr);
            }
        } else {
            if (opt[0] == 'E') printf("$");
            putchar(next_c);
        }
    }
}

void option_n(int *line_cntr, char opt[]) {
    if (opt[1] != 's') {
        *line_cntr += 1;
        if (*line_cntr != 1) {
            if (opt[0] == 'E') printf("$");
            printf("\n");
        }
        print_num(*line_cntr);
    }
}

void option_v(int c, char opt[]) {
    if (c < 32 && c != '\t') {
        printf("^%c", c + 64);
    } else if (c > 127 && c < 160) {
        printf("M-^%c", c - 64);
    } else if (c >= 160) {
        printf("M-%c", c - 128);
    } else if (c == 127) {
        printf("^?");
    } else {
        if (opt[4] == 'T') {
            if (c != '\t') putchar(c);
        } else
            putchar(c);
    }
}

void option_E(int *line_cntr, char opt[]) {
    if (opt[1] != 's' && opt[2] != 'b' && opt[3] != 'n') {
        if (!*line_cntr)
            *line_cntr = 1;
        else
            printf("$\n");
    }
}

void option_T(char c, char opt[]) {
    if (c == '\t')
        printf("^I");
    else {
        if (opt[5] != 'v') {
            putchar(c);
        }
    }
}