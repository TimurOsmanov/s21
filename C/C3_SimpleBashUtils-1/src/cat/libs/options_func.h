#ifndef OPTIONS_FUNC_H
#define OPTIONS_FUNC_H

void print_num(int line_cntr);
void option_s(char next_c, char c, char opt[], int *prev_line_empty, int *line_cntr);
void option_b(char next_c, char opt[], int *line_cntr);
void option_n(int *line_cntr, char opt[]);
void option_v(int c, char opt[]);
void option_E(int *line_cntr, char opt[]);
void option_T(char c, char opt[]);

#endif