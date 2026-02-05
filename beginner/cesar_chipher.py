def encrypt(text, step, alphabet):
    answer = ""
    for i in range(len(text)):
        if not text[i].isalpha():
            answer += text[i]
        else:
            is_lower = text[i].islower()
            if not is_lower:
                alphabet = alphabet.upper()
            else:
                alphabet = alphabet.lower()
            next_idx = alphabet.index(text[i]) + step
            if next_idx > len(alphabet) - 1:
                next_idx -= len(alphabet)
            elif next_idx < 0:
                next_idx += len(alphabet)
            answer += alphabet[next_idx]
    return answer

def decipher(text, step, alphabet):
    return encrypt(text, -step, alphabet)

# direction: "encrypt" or "decipher"
# lang: "en" or "ru"
# step: an int


def cesar_chipher(text, direction, lang, step):
    alphabet = None
    if lang == "en":
        alphabet = "abcdefghijklmnopqrstuvwxyz"
    elif lang == "ru":
        alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    if direction == "encrypt":
        return encrypt(text, step, alphabet)
    elif direction == "decipher":
        return decipher(text, step, alphabet)

print(cesar_chipher("Блажен, кто верует, тепло ему на свете!", "encrypt", "ru", 10))
print(cesar_chipher("To be, or not to be, that is the question!", "encrypt", "en", 17))
print(cesar_chipher("Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.", "decipher", "ru", 7))
print(cesar_chipher("Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.", "decipher", "en", 25))

for i in range(26):
    print(cesar_chipher("Hawnj pk swhg xabkna ukq nqj.", "decipher", "en", i))
