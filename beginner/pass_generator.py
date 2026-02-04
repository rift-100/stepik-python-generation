import random


def generate_password(length, chars):
    return "".join(random.sample(chars, length))


def add_symbols(text, conditon):
    if conditon == "да":
        return text
    return ""


digits = "012345556789"
lowaercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = lowaercase_letters.upper()
punctuation = "!#$%&*+-=?@^_"
weird_symbols = "il1Lo0O"

count_of_passwords = int(input("Введите количество паролей для генерации: "))
password_len = int(input("Введите длину одного пароля: "))

is_digits = input("Включить цифры? (да/нет) ").strip().lower()
is_lower = input("Включить строчные буквы? (да/нет) ").strip().lower()
is_upper = input("Включить прописные буквы? (да/нет) ").strip().lower()
is_punctuation = input("Включить символы? (да/нет) ").strip().lower()
is_weird = input("Исключить неоднозначные символы? (да/нет) ").strip().lower()

chars = (
    add_symbols(digits, is_digits)
    + add_symbols(lowaercase_letters, is_lower)
    + add_symbols(uppercase_letters, is_lower)
    + add_symbols(punctuation, is_punctuation)
)

filtred_chars = ""

if is_weird == "да":
    for c in chars:
        if c not in weird_symbols:
            filtred_chars += c
else:
    filtred_chars = chars

for _ in range(count_of_passwords):
    print(generate_password(password_len, filtred_chars))
