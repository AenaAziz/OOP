from letter_permutator import LetterPermutator

if __name__ == "__main__":

    alp1 = LetterPermutator("fish")
    alp1.make_possible_strings()

    alp1.letters = "is"
    alp1.make_possible_strings()

    print(alp1.letters)

