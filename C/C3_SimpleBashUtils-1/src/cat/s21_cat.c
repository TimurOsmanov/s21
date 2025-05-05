#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define CORR_OPT_NUM 4
#define CORR_OPT_LEN 18

int check_file(const char *filename) {
    int flag = 0;
    FILE *fptr = fopen(filename, "r");
    flag = (fptr == NULL) ? 0 : 1;
    if (flag) fclose(fptr);
    return flag;
}

void print_file(const char *filename) {
    FILE *fptr = fopen(filename, "r");
    char line[256];
    int counter = 1;
    while ((fgets(line, 256, fptr)) != NULL) {
        printf("     %d %s", counter, line);
        counter++;
    }
    fclose(fptr);
}

int check_short_options(char *options, char *all_opt_ptr[]) {
    int i = 1;
    int option_state = 0;
    char correct_options[8] = "vsbneEtT";

    while (options[i] != '\0') {
        option_state = 0;

        for (int j = 0; j < 8; j++) {
            if (options[i] == correct_options[j]) {
                option_state = 1;
                (*all_opt_ptr)[j] = correct_options[j];
                break;
            }
        }

        if (!option_state) {
            printf("\ncat: invalid option -- '%c'\n", options[i]);
            printf("Try 'cat --help' for more information.\n");
            break;
        }
        i++;
    }
    return option_state;
}

int check_long_option(char *option, char *all_opt_ptr[]) {
    int option_state = 0;
    char correct_options[CORR_OPT_NUM][CORR_OPT_LEN] = {"--show-nonprinting", "--squeeze-blank",
                                                        "--number-nonblank", "--number"};
    for (int i = 0; i < CORR_OPT_NUM; i++) {
        option_state = 0;
        if (!strcmp(option, (const char *)&correct_options[i])) {
            option_state = 1;
            if (i == 0) (*all_opt_ptr)[i] = 'v';
            if (i == 1) (*all_opt_ptr)[i] = 's';
            if (i == 2) (*all_opt_ptr)[i] = 'b';
            if (i == 3) (*all_opt_ptr)[i] = 'n';
            break;
        }
    }

    if (!option_state) {
        printf("\ncat: unrecognized option '%s'\n", option);
        printf("Try 'cat --help' for more information.\n");
    }
    return option_state;
}

int check_args(int argc, char *argv[], char all_opt[], char **files_ptr[]) {
    int option_state = 0;
    int file_num = 0;
    for (int i = 1; i < argc; i++) {
        if (argv[i][0] == '-') {
            if (argv[i][1] != '-')
                option_state = check_short_options(argv[i], &all_opt);
            else
                option_state = check_long_option(argv[i], &all_opt);

            if (!option_state) break;
        } else {
            (*files_ptr)[file_num] = argv[i];
            file_num += 1;
        }
    }
    return option_state;
}

int count_files_names(int argc, char *argv[]) {
    int c = 0;
    for (int i = 1; i < argc; i++) {
        if (argv[i][0] != '-') {
            c++;
        }
    }
    return c;
}

int main(int argc, char *argv[]) {
    int num_files = count_files_names(argc, argv);
    char **files = (char **)calloc(num_files, sizeof(char *));

    char all_opt[] = {'_', '_', '_', '_', '_', '_', '_', '_'};
    int options_state = check_args(argc, argv, all_opt, &files);

    if (options_state) {
        printf("\nmain all_opt = %s", all_opt);
    }

    for (int i = 0; i < num_files; i++) {
        if (check_file(files[i])) {
            if (i != 0) printf("\n");
            print_file(files[i]);
        } else
            printf("\ncat: %s: No such file or directory", files[i]);
    }

    free(files);
    printf("\n\n");
    return 0;
}