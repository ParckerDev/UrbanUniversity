def check_email(email):
    if '@' in email and (email[-4:] == '.com' or email[-3:] == '.ru' or email[-4:] == '.net'):
       return True
    return False

def send_email(message, recipient, sender="university.help@gmail.com"):
    if check_email(recipient) == False or check_email(sender) == False:
        print (f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        else:
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
            

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
