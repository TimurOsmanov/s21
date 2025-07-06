## 1. Using each of the three selected editors, create a test_X.txt file, where X is the name of the editor in which the file is created. Write your nickname in it, close the file and save the changes.

1. vim
   1. vim test_VIM.txt
   2. i
   3. ESC
   4. :wq

2. nano
   1. nano test_NANO.txt
   2. ctrl+s
   3. ctrl+x

3. joe
   1. joe test_JOE.txt
   2. Ctrl+K X

## 2. Using each of the three selected editors, open the file for editing, edit the file by replacing the nickname with the "21 School 21" string, close the file without saving the changes.

1. vim
   1. vim test_VIM.txt
   2. i
   3. 21 School 21
   4. ESC
   5. :q!

2. nano
   1. nano test_NANO.txt
   2. 21 School 21
   3. ctrl+x n

3. joe
   1. joe test_JOE.txt
   2. 21 School 21
   3. Ctrl+K q n

## 3. Using each of the three selected editors, edit the file again (similar to the previous point) and then master the functions of searching through the contents of a file (a word) and replacing a word with any other one.

1. vim
   1. поиск
       1. vim test_VIM.txt
       2. i
       3. 21 School 21
       4. ESC
       5. /21 Enter n - next

   2. замена
       1. :s/21/word/g


2. nano
   1. поиск
       1. nano test_NANO.txt
       2. 21 School 21
       3. ctrl+w 21 enter alt+w - next

   2. замена
       1. ctrl+\ 21 enter word enter A

3. joe
   1. поиск
      1. joe test_JOE.txt
      2. 21 School 21
      3. Ctrl+K F 21 B

   2. замена
      1. Ctrl+K F 21 R word R
