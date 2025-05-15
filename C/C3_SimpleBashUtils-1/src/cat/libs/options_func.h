#ifndef OPTIONS_FUNC_H
#define OPTIONS_FUNC_H

void option_s(char next_c, char c, char opt[], int *prev_line_empty, int *line_cntr, int *next_file_ptr);
void option_b(char next_c, char *c, char opt[], int *line_cntr, int *next_file_ptr);
void option_n(int *line_cntr);
void option_v();
void option_E();
void option_e();
void option_T();
void option_t();

#endif