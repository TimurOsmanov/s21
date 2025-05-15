#include "parser.h"

#include <stdio.h>
#include <string.h>

#define CORR_OPT_NUM 8
#define LONG_OPT_NUM 4
#define LONG_OPT_LEN 18

int parse_short_options(char *opt_short, char all_opt[]) {
    int i = 1;
    int option_state = 0;
    char correct_options[CORR_OPT_NUM] = "sbnetvET";

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
            printf("cat: invalid option -- '%c'\n", opt_short[i]);
            printf("Try 'cat --help' for more information.\n");
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
            if (i == 0) all_opt[i] = 's';
            if (i == 1) all_opt[i] = 'b';
            if (i == 2) all_opt[i] = 'n';
            if (i == 3) all_opt[5] = 'v';
            break;
        }
    }
    if (!option_state) {
        printf("cat: unrecognized option '%s'\n", opt_long);
        printf("Try 'cat --help' for more information.\n");
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