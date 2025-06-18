#ifndef FILES_FUNC_H
#define FILES_FUNC_H

int count_files_names(int argc, char *argv[]);
int check_file(const char *filename);
void print_file(const char *filename, char *c, char opt[], int *line_cntr_ptr);

#endif