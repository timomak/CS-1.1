import random

# Possible mystery words
wordsList = ["spacemans", "new", "toonew"]
# Pick a random from the array.
currentWord = random.choice(wordsList)

# List to store low dashes for each letter in the word.
mysteryWord = list()

# current word but in pieces
notSoMysteryWord = list()

# Need this to check if user won
numberOfCorrectTries = 0

# List of user guesses
guesses = list()
numberOfWrongGuesses = 0

gameOver = False

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# Function to count and make a dash for each letter in word
def hiddenWord():
    loadSentence = "Mystery word: "
    for letters in currentWord:
        notSoMysteryWord.append(letters)
        mysteryWord.append("_")
        print(mysteryWord)
        # Underscore the not yet guessed letters from the mystery word
        loadSentence = loadSentence + "_ "
    print(loadSentence)

# Starts the game by laying out the hidden word.
hiddenWord()

# Function to get letter
def getLetter():
    newLetter = input("New letter: ")

    # Check if it's a single letter.
    if len(newLetter) > 1:
        print("Type only one letter.")
        return

    newLetter = newLetter.lower()
    if newLetter in alphabet:
        # Check if the word exists already, append otherwise
        checkIfLetterExists(newLetter)
    else:
        print("Please try again with a single letter.")


# Function to keep track of all the wordsList
def checkIfLetterExists(letter: str):
    if len(guesses) > 0 :
        for i in guesses:
            if letter == i:
                print("You already tried that!")
                return
        # Change append into checking if it mathces
        checkIfTheGuessIsCorrect(letter)
    else:
        # Change append into checking if it mathces
        checkIfTheGuessIsCorrect(letter)

# Check if the letter corresponds to any of the letters in the mystery word.
def checkIfTheGuessIsCorrect(guess:str):
    global numberOfCorrectTries
    global numberOfWrongGuesses
    index = 0
    found = False

    for eachLetter in notSoMysteryWord:
        if guess == eachLetter:
            print("The guess was correct!")
            mysteryWord[index] = guess
            found = True
            numberOfCorrectTries = numberOfCorrectTries + 1
        guesses.append(guess)
        index = index + 1
        print(mysteryWord)

    if found == False:
        numberOfWrongGuesses = numberOfWrongGuesses + 1
        print("Guessed Wrong number: ", numberOfWrongGuesses)
        # TODO: Show number of incorrect tries
        # TODO: Check if game won


while numberOfCorrectTries != len(notSoMysteryWord) and gameOver == False:
    getLetter()
    if numberOfWrongGuesses == 5:
        gameOver = True
        print("You Lost!")


if numberOfCorrectTries == len(notSoMysteryWord):
    print("YOU WON!")

# function to keep track of all the wrong guesses
