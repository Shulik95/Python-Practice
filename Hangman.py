HANGMAN_ASCII_ART = """
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
  """

MAX_TRIES = 7
HANGMAN_PHOTOS = {0: "", 1: "x-------x", 2: """    x-------x\n    |\n    |\n    |
    |\n    |\n""", 3: """    x-------x\n    |       |\n    |       0\n    |
    |\n    |""", 4: """    x-------x\n    |       |\n    |       0
    |       |\n    |\n    |""", 5: """    x-------x\n    |       |
    |       0\n    |      /|\\\n    |\n    |""", 6: """    x-------x
    |       |\n    |       0\n    |      /|\\\n    |      /\n    |""",
                  7: """    x-------x\n    |       |\n    |       0
    |      /|\\\n    |      / \\\n    |"""}


def create_board():
    word = input("Please enter a word: ")
    board = "".zfill(len(word)).replace('0', '_ ')
    print(board)


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    checks legality of given user input
    :param old_letters_guessed: list of previously guessed letters.
    :param letter_guessed: the letter the user guessed
    :return: True if guess is legal, False otherwise
    :rtype: boolean
    """
    if len(letter_guessed) != 1 or not letter_guessed.isalpha() or \
            letter_guessed.lower() in old_letters_guessed:
        return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """

    :param letter_guessed:
    :param old_letters_guessed:
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):  # user guess is illegal
        print("X")
        guess_str = " -> ".join(sorted(old_letters_guessed))
        print("Let us remind you of the letters you guessed so far: ",
              guess_str)
        return False
    else:
        old_letters_guessed.append(letter_guessed.lower())
        return True


def show_hidden_word(secret_word, old_letters_guessed):
    """
    shows the player his advancement in guessing the word.
    :param secret_word: word to guess
    :param old_letters_guessed: list of the letters the user guessed so far
    :return string representing the parts of the secret word the user guessed
    :rtype: string
    """
    word_as_list = list('_' * len(secret_word))
    for letter in old_letters_guessed:
        for i in range(len(secret_word)):
            if letter == secret_word[i]:
                word_as_list[i] = letter
    return " ".join(word_as_list)


def check_win(secret_word, old_letters_guessed):
    """
    checks if all the letters of the word were guessed
    :param secret_word: word to guess
    :param old_letters_guessed: list of guessed letters by user
    :return: True if the player won, False otherwise
    :rtype: boolean
    """
    guessed_word = show_hidden_word(secret_word, old_letters_guessed).replace(" ", '')
    return secret_word == guessed_word


def print_hangman(num_of_tries):
    """
    prints the state of the
    :param num_of_tries:
    :return:
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def choose_word(file_path, index):
    """

    :param file_path:
    :param index:
    :return:
    """
    word_dict = {}
    file = open(file_path)
    all_words_lst = (file.readline()).split(" ")  # create array of words
    for word in all_words_lst:
        if word in word_dict:
            word_dict[word] += 1
        else:  # create new entry for the word
            word_dict[word] = 0
    return all_words_lst[(index - 1) % len(all_words_lst)]


def start_game():
    """
    the main function on the games, runs it from start to finish.
    """
    guessed_letters = []
    num_of_guesses = 0
    print(HANGMAN_ASCII_ART)
    file_path = input("Please insert the file adress: ")
    word_idx = int(input("Please choose a number: "))  # get index of a word
    secret_word = choose_word(file_path, word_idx)
    while not check_win(secret_word, guessed_letters):
        user_guess = input("Please choose a letter: ")
        if not try_update_letter_guessed(user_guess, guessed_letters):
            continue
        print(show_hidden_word(secret_word, guessed_letters))
        print()
        if user_guess not in secret_word:  # update drawing
            num_of_guesses += 1
        print_hangman(num_of_guesses)
        if num_of_guesses == MAX_TRIES:
            print("Loser :(")
            return
    print("Winner! you win nothing")


if __name__ == '__main__':
    start_game()
