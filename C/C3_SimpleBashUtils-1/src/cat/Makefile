CC=gcc
CFLAGS=-Wall -Werror -Wextra -std=c11 -pedantic
filename = "test5_0blank_sof_0blank_eof.txt"
options1 = test/$(filename) -be wrong_file_name test/$(filename)
# options2 = bytes.txt -be
options2 = bytes.txt -z
options = $(options2)

all:  clean s21_cat valgrind clang run cat diff

clean:
	-rm -r s21_cat

s21_cat: 
	$(CC) $(CFLAGS) s21_cat.c libs/*.c -o s21_cat

valgrind:
	# ver 3.23
	valgrind --tool=memcheck --leak-check=yes --show-leak-kinds=all --track-origins=yes -s ./s21_cat $(options)

clang:
	clang-format-18 -i *.c
	clang-format-18 -i libs/*.c
	clang-format-18 -i libs/*.h

run:
	./s21_cat $(options)

cat:
	-cat $(options)

diff:
	./s21_cat $(options) > cat1.txt
	-cat $(options) > cat2.txt
	diff cat1.txt cat2.txt