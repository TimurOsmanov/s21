## Allow user created in Part 2 to execute sudo command.
1. sudo adduser other_user sudo

### Change the OS hostname via the user created in Part 2 (using sudo);
1. su - other_user
2. sudo hostnamectl set-hostname new-hostname (для системы нельзя использоваить нижнее подчеркивание)
3. sudo nano /etc/hosts (change shireeth to new-hostname)
4. sudo reboot

### In the report explain the true purpose of sudo command (don’t write about the fact that this word is "magic" one)

1. Команда sudo в Ubuntu, как и в других системах Linux, предоставляет пользователю возможность выполнять команды с повышенными привилегиями, обычно правами суперпользователя (root). Это позволяет обычному пользователю временно получать права администратора для выполнения определенных задач, не требуя постоянного входа в систему под учетной записью root. 

