import gtts
import os

def read_from_file():
    global words_bank
    files = os.listdir()
    if "translate.txt" in files:
        file = open("./translate.txt")
        temp = file.read().split("\n")
        file.close()
        words_bank = []    
        for i in range(0, len(temp), 2):
            my_dict = {"en": temp[i], "fa": temp[i+1]}
            words_bank.append(my_dict)
    else:
        print("database file not found!")
        exit(0)

def add_new_word_to_file():
    global words_bank
    files = os.listdir()
    if "translate.txt" in files:
        file = open("translate.txt", "a")
        new_word_en = input("Enter the english word: ")
        new_word_fa = input("Enter the persian translation of the entered word: ")
        file.write("\n" + new_word_en + "\n" + new_word_fa)
        file.close()
        words_bank.append({"en": new_word_en, "fa": new_word_fa})
        print("new word successfully added to database!")
    else:
        print("database file not found!")

def show_menu():
    print("Welcome to translator")
    print("1- translate english to persian")
    print("2- translate persian to english")
    print("3- add a new word to database")
    print("4- exit")

def translate_english_to_persian():
    user_sentences = input("Enter your english text: ").split(".")
    output = ""
    for user_words in user_sentences:
        if user_words != "":
            splited_user_words = user_words.split(" ")
            for user_word in splited_user_words:
                for word in words_bank:
                    if user_word == word["en"]:
                        output += word["fa"] + " " if user_word != splited_user_words[len(splited_user_words)-1] else word["fa"]
                        break
                else:
                    output += user_word + " " if user_word != splited_user_words[len(splited_user_words)-1] else user_word
            output += "."
    print(output)
    gtts.gTTS(output).save("translate.mp3")

def translate_persian_to_english():
    user_sentences = input("Enter your persian text: ").split(".")
    output = ""
    for user_words in user_sentences:
        if user_words != "":
            splited_user_words = user_words.split(" ")
            for user_word in splited_user_words:
                for word in words_bank:
                    if user_word == word["fa"]:
                        output += word["en"] + " " if user_word != splited_user_words[len(splited_user_words)-1] else word["en"]
                        break
                else:
                    output += user_word + " " if user_word != splited_user_words[len(splited_user_words)-1] else user_word
            output += "."
    print(output)
    gtts.gTTS(output).save("translate.mp3")

read_from_file()
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    show_menu()
    choice = input("enter your choice: ")
    if choice == "1":
        translate_english_to_persian()
    elif choice == "2":
        translate_persian_to_english()
    elif choice == "3":
        add_new_word_to_file()
    elif choice == "4":
        exit(0)