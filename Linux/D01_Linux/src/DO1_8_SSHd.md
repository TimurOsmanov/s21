## 1. Install the SSHd service.
1. sudo apt-get install openssh-server

## 2. Add an auto-start of the service whenever the system boots.
1. sudo systemctl enable ssh --now
2. sudo systemctl start ssh

## 3. Reset the SSHd service to port 2022.
1. sudo nano /etc/ssh/sshd_config
2. add Port 2022 after #Port 22
3. sudo systemctl restart sshd
4. sudo ufw allow 2022/tcp

## 4. Show the presence of the sshd process using the ps command. To do this, you need to match the keys to the command.

1. ps aux | grep '[s]shd'Она состоит из двух частей, соединенных через символ | (пайп), который передает вывод первой команды как ввод для второй. Команда ps aux выводит список всех процессов в системе с подробной информацией. Когда мы передаем вывод ps aux через grep sshd, 
получаем только те строки, которые содержат слово sshd

## 5. Reboot the system

## Explain the meaning of the -tan keys, the value of each output column, the value 0.0.0.0. in the report.

1. Команда netstat используется для отображения сетевых соединений, таблиц маршрутизации, статистики интерфейсов и других сетевых данных. 
В данном случае она показывает активные TCP-соединения.
-t — отображает только TCP-соединения.
-a — показывает все активные соединения и слушающие порты 
(то есть, и установленные соединения, и те, что ожидают входящих).
-n — выводит адреса и номера портов в числовом виде, 
без попытки преобразовать их в имена (например, IP-адреса вместо доменных имен, номера портов вместо имен служб).
2. Объяснение колонок:
Proto — протокол (здесь tcp)
Recv-Q — количество байтов в очереди на прием
Send-Q — количество байтов в очереди на отправку
Local Address — локальный IP-адрес и порт
Foreign Address — удаленный IP-адрес и порт (или *, если слушающий порт)
State — состояние соединения (ESTABLISHED, LISTEN, CLOSE_WAIT, и т.д.)
3. 0.0.0.0	"Все IP-адреса" или "слушать на всех интерфейсах"
