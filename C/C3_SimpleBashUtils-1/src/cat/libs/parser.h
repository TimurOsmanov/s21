#ifndef PARSER_H
#define PARSER_H

int parse_short_options(char *opt_short, char all_opt[]);
int parse_long_option(char *opt_long, char all_opt[]);
int parse_args(int argc, char *argv[], char all_opt[], char *files_ptr[]);

#endif