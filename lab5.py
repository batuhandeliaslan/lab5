import random
import string
def get_valid_character(prompt, existing_chars):
    while True:
        char = input(prompt).strip()
        if len(char) == 1 and char in string.ascii_lowercase and char not in existing_chars:
            return char
        print("Lütfen benzersiz ve geçerli bir küçük harf girin.")

def get_unique_replacements(char, num_replacements=3):
    replacements = set()
    while len(replacements) < num_replacements:
        rep_char = input(f"'{char}' için bir özel karakter girin: ").strip()
        if len(rep_char) == 1 and rep_char not in replacements and rep_char not in string.ascii_lowercase:
            replacements.add(rep_char)
        else:
            print("Lütfen tek bir benzersiz özel karakter girin.")
    return list(replacements)

replacement_dict = {}
print("5 küçük harf ve her biri için 3 farklı özel karakter belirleyin.")
for _ in range(5):
    char = get_valid_character("Bir küçük harf girin: ", replacement_dict.keys())
    replacement_dict[char] = get_unique_replacements(char)

passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)

categorized_passwords = {"strong": [], "weak": []}

for password in passwords:
    new_password = list(password)
    replaced_count = 0
    special_char_count = 0

    for i, char in enumerate(new_password):
        if char in replacement_dict:
            new_char = random.choice(replacement_dict[char])
            new_password[i] = new_char
            replaced_count += 1
            special_char_count += 1
        elif new_password[i] in string.punctuation:
            special_char_count += 1

    new_password = ''.join(new_password)

    if special_char_count > 4:
        categorized_passwords["strong"].append(new_password)
    else:
        categorized_passwords["weak"].append(new_password)

print("\n" + "-" * 30)
print("Generated Passwords:")
print("-" * 30)
print("\nSTRONG PASSWORDS:")
if categorized_passwords["strong"]:
    for password in categorized_passwords["strong"]:
        print(f"- {password}")
else:
    print("Yok")

print("\nWEAK PASSWORDS:")
if categorized_passwords["weak"]:
    for password in categorized_passwords["weak"]:
        print(f"- {password}")
else:
    print("Yok")
print("-" * 30)
