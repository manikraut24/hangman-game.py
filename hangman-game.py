#Python console-based Guess The Word (Hangman) game.
name = input("what is your name: ")
print("Good Luck! ",name)

import random

# List of fruit names
fruits = [
    "apple", "banana", "orange", "grape", "kiwi",
    "mango", "pineapple", "strawberry", "blueberry", "watermelon"
]

def play_game():
    word = random.choice(fruits)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []

    print("Let's play Hangman!")
    print(word_completion)
    print("\n")

    while not guessed:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        
        print(word_completion)
        print("\n")
    
    print("Congratulations, you guessed the word! You win!")

if __name__ == "__main__":
    play_game()
