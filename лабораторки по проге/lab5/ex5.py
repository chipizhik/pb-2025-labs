def palindrome(text):
    text = text.lower()
    bez_probelov = text.replace(' ', '')
    return bez_probelov == bez_probelov[::-1]
input_text = input()
if palindrome(input_text):
    print("Да")
else:
    print("Нет")