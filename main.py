import random

# List of words
words = ["spaceship", "rockets", "galaxy", "luna", "jupiter"]

# Select a random word
word = random.choice(words)

# Display blanks
random_word = ["_"] * len(word)
#No. of attempts
attempts = 10

print("***** GUESS THE WORD GAME *****")

while attempts > 0 and "_" in random_word:

    print("\nWord:", " ".join(random_word))
    print("Attempts left:", attempts)

    letter = input("Enter a letter: ")

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                random_word[i] = letter
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")

# Result
if "_" not in random_word:
    print("\nCongratulations! You guessed it.")
    print("The word is:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)
