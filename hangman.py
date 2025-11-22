import random

words = ["წიგნი", "პროგრამა", "პითონი", "კალათა", "წვიმა", "მზე"]

secret_word = random.choice(words)

hidden_word = ["_"] * len(secret_word)

used_letters = set()

attempts = 10

print("გამოიცანი სიტყვა:")
print(" ".join(hidden_word))

while attempts > 0 and "_" in hidden_word:
    print(f"\დარჩენილი მცდელობები: {attempts}")
    guess = input("შეიტანე სიმბოლო: ").strip()

    if len(guess) != 1:
        print("გთხოვ, შეიყვანე მხოლოდ ერთი სიმბოლო.")
        continue

    if guess in used_letters:
        print("ეს სიმბოლო უკვე სცადე.")
        continue

    used_letters.add(guess)

    if guess in secret_word:
        print("✔ სწორია!")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                hidden_word[i] = guess
    else:
        print("✘ ასეთი სიმბოლო არ არის სიტყვაში.")
        attempts -= 1

    print(" ".join(hidden_word))

if "_" not in hidden_word:
    print("\nგილოცავ! სიტყვა გამოიცანი:", secret_word)
else:
    print("\nსამწუხაროდ წააგე! სწორი სიტყვა იყო:", secret_word)
