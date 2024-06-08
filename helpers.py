import random

def generate_random_emails(domain = "yandex.ru", username = "chuburova"):
    random_number = random.randint(0, 9999)
    login = f'{username}{random_number}'
    email = f'{login}@{domain}'

    return email
