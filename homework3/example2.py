# 2. Написать скрипт, который будет делать ping google.com.
# Если сервер отвечает, то выводить - success, если нет - doesn't work.
import os

print("Пингуем Гугл")
print("Введите IP-адрес или доменное имя:")

target = input()  

if os.name == 'nt':
    command = f"ping -n 1 {target}"

response = os.system(command)

if response == 0:
    print("success") 
else:
    print("doesn't work")