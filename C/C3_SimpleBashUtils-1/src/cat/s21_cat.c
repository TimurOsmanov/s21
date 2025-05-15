#include <stdio.h>
#include <stdlib.h>

#include "libs/files_func.h"
#include "libs/parser.h"

int main(int argc, char *argv[]) {
    int num_files = count_files_names(argc, argv);
    char **files_arr = (char **)calloc(num_files, sizeof(char *));

    char opt_arr[] = {'_', '_', '_', '_', '_', '_', '_', '_'};
    int options_state = parse_args(argc, argv, opt_arr, files_arr);

    if (!options_state) {
        printf("\n no options");
    } else {
        int line_cntr = 0;
        int next_file = 0;
        char c = '\n';
        for (int i = 0; i < num_files; i++) {
            if (check_file(files_arr[i])) {
                print_file(files_arr[i], &c, opt_arr, &line_cntr, &next_file);
            } else {
                if (!i) printf("cat: %s: No such file or directory", files_arr[i]);
                if (i) printf("cat: %s: No such file or directory\n", files_arr[i]);
                // if (!i) fprintf(stderr, "cat: %s: No such file or directory", files_arr[i]);
                // if (i) fprintf(stderr, "cat: %s: No such file or directory\n", files_arr[i]);
                // perror(" ");
                // perror("123");
            }
        }
    }

    free(files_arr);
    return 0;
}