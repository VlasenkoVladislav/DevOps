import pandas as pd
import smtplib
# Данные для входа
sendAddress = "boss.lalka.undegraund18@gmail.com"
passwords = "hwxc mvfd uedq ehad"
# Создание списка email
emails = pd.Series(["vlasenkovladislav21@gmail.com"])
# Подключение к серверу
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()  # Включаем безопасное соединение
server.login(sendAddress, passwords)
# Формируем письмо
subject = "ALARM"
msg = "The email message"
body = f"Subject: {subject}\n\n{msg}"
# Отправка письма каждому email из списка
for email in emails:
    server.sendmail(sendAddress, email, body)
# Завершаем соединение
server.quit()

print('test git1')
print("test git2")
print("test git3")
print("test git4")
print("test main2")