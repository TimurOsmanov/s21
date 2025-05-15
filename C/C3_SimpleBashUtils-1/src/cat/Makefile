CC=gcc
CFLAGS=-Wall -Werror -Wextra -std=c11 

options = txts/test.txt -b wrong_file_name txts/test2.txt

all:  clean s21_cat valgrind clang run cat

clean:
	-rm -r s21_cat

s21_cat: 
	$(CC) $(CFLAGS) s21_cat.c libs/*.c -o s21_cat -pedantic 

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
	diff cat1.txt cat2.txt