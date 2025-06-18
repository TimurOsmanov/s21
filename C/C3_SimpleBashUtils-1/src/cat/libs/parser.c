#include "parser.h"

#include <stdio.h>
#include <string.h>

#define CORR_OPT_NUM 9
#define LONG_OPT_NUM 4
#define LONG_OPT_LEN 18

int parse_short_options(char *opt_short, char all_opt[]) {
    int i = 1;
    int option_state = 0;
    char correct_options[CORR_OPT_NUM] = "EsbnTvet_";

    while (opt_short[i] != '\0') {
        option_state = 0;

        for (int j = 0; j < CORR_OPT_NUM; j++) {
            if (opt_short[i] == correct_options[j]) {
                all_opt[j] = correct_options[j];
                option_state = 1;
                break;
            }
        }
        if (!option_state) {
            fprintf(stderr, "cat: invalid option -- '%c'\n", opt_short[i]);
            fprintf(stderr, "Try 'cat --help' for more information.\n");
            all_opt[8] = 'w';
            break;
        }
        i++;
    }
    return option_state;
}

int parse_long_option(char *opt_long, char all_opt[]) {
    int option_state = 0;
    char correct_options[LONG_OPT_NUM][LONG_OPT_LEN] = {"--squeeze-blank", "--number-nonblank", "--number",
                                                        "--show-nonprinting"};
    for (int i = 0; i < LONG_OPT_NUM; i++) {
        option_state = 0;
        if (!strcmp(opt_long, (const char *)&correct_options[i])) {
            option_state = 1;
            if (i == 0) all_opt[1] = 's';
            if (i == 1) all_opt[2] = 'b';
            if (i == 2) all_opt[3] = 'n';
            if (i == 3) all_opt[5] = 'v';
            break;
        }
    }
    if (!option_state) {
        fprintf(stderr, "cat: unrecognized option '%s'\n", opt_long);
        fprintf(stderr, "Try 'cat --help' for more information.\n");
        all_opt[8] = 'w';
    }
    return option_state;
}

int parse_args(int argc, char *argv[], char all_opt[], char *files_ptr[]) {
    int option_state = 0;
    int file_num = 0;
    for (int i = 1; i < argc; i++) {
        if (argv[i][0] == '-') {
            if (argv[i][1] != '-')
                option_state = parse_short_options(argv[i], all_opt);
            else
                option_state = parse_long_option(argv[i], all_opt);

            if (!option_state) break;
        } else {
            files_ptr[file_num] = argv[i];
            file_num += 1;
        }
    }
    return option_state;
}

void expand_e_b_t_flags(char all_opt[]) {
    if (all_opt[2] == 'b') all_opt[3] = '_';
    if (all_opt[6] == 'e') {
        all_opt[0] = 'E';
        all_opt[5] = 'v';
        all_opt[6] = '_';
    }
    if (all_opt[7] == 't') {
        all_opt[4] = 'T';
        all_opt[5] = 'v';
        all_opt[7] = '_';
    }
}