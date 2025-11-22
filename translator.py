import os

DICTIONARY_FILE = "dictionary.txt"


def load_dictionary():
    translations = {}

    if not os.path.exists(DICTIONARY_FILE):
        open(DICTIONARY_FILE, "w").close()

    with open(DICTIONARY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line or "=" not in line:
                continue

            lang_pair, words = line.split(":")
            src_word, dst_word = words.split("=")

            lang_pair = lang_pair.strip()
            src_word = src_word.strip().lower()
            dst_word = dst_word.strip()

            if lang_pair not in translations:
                translations[lang_pair] = {}

            translations[lang_pair][src_word] = dst_word

    return translations

def save_translation(lang_pair, src_word, dst_word):
    with open(DICTIONARY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{lang_pair}: {src_word}={dst_word}\n")



def translate_word(translations):
    print("\nაირჩიეთ ენების წყვილი:")
    print("1) ქართული → ინგლისური (ka-en)")
    print("2) ქართული → რუსული (ka-ru)")
    print("3) ინგლისური → ქართული (en-ka)")
    print("4) რუსული → ქართული (ru-ka)")

    choice = input("აირჩიეთ (1-4): ")

    lang_map = {
        "1": "ka-en",
        "2": "ka-ru",
        "3": "en-ka",
        "4": "ru-ka"
    }

    if choice not in lang_map:
        print("არასწორი არჩევანი!")
        return

    lang_pair = lang_map[choice]

    word = input("\nშეიყვანეთ სიტყვა ან ფრაზა: ").strip().lower()

    if word in translations.get(lang_pair, {}):
        print("თარგმანი:", translations[lang_pair][word])
    else:
        print("ეს სიტყვა ლექსიკონში არ მოიძებნა.")

        add = input("გსურთ დაამატოთ თარგმანი? (დიახ/არა): ").strip().lower()
        if add == "დიახ":
            new_trans = input("შეიყვანეთ თარგმანი: ").strip()
            save_translation(lang_pair, word, new_trans)

        
            if lang_pair not in translations:
                translations[lang_pair] = {}
            translations[lang_pair][word] = new_trans

            print("სიტყვა წარმატებით დაემატა ლექსიკონს!")
        else:
            print("სიტყვა არ დაემატა.")


def main():
    translations = load_dictionary()

    while True:
        print("\n--- თარჯიმანის აპლიკაცია ---")
        print("1) თარგმნა")
        print("2) გასვლა")

        choice = input("აირჩიეთ: ")

        if choice == "1":
            translate_word(translations)
        elif choice == "2":
            print("გმადლობთ გამოყენებისთვის!")
            break
        else:
            print("არასწორი არჩევანი!")


if __name__ == "__main__":
    main()
