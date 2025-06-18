#include <stdio.h>
#include <stdlib.h>

#include "libs/files_func.h"
#include "libs/parser.h"

int main(int argc, char *argv[]) {
    int num_files = count_files_names(argc, argv);
    char **files_arr = (char **)calloc(num_files, sizeof(char *));

    char opt_arr[] = {'_', '_', '_', '_', '_', '_', '_', '_', '_'};
    int options_state = parse_args(argc, argv, opt_arr, files_arr);

    if (num_files && opt_arr[8] != 'w') {
        expand_e_b_t_flags(opt_arr);
        int line_cntr = 0;
        char c = '\n';

        for (int i = 0; i < num_files; i++) {
            if (check_file(files_arr[i])) {
                print_file(files_arr[i], &c, opt_arr, &line_cntr);
            } else {
                // fflush to avoid unpredictable output of stderr:
                // stderr is not buffered - it outputs instantly, stdout is buffered
                fflush(stdout);
                if (c != '\n')
                    fprintf(stderr, "cat: %s: No such file or directory\n", files_arr[i]);
                else
                    fprintf(stderr, "\ncat: %s: No such file or directory", files_arr[i]);
            }
        }
        // last char of run
        if (opt_arr[0] == 'E' && c == '\n') printf("$");
        putchar(c);
    } else {
        if (!options_state && !num_files) {
            fprintf(stderr, "cat: No file or directory && no options entered.\n");
        } else {
            if (!num_files) fprintf(stderr, "cat: No file or directory entered.\n");
        }
    }

    free(files_arr);
    return 0;
}