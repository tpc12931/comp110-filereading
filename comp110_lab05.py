"""
Module: comp110_lab05

Exercises from lab 05, dealing with strings and file reading.
"""

def max_wind_speed(hurricane_filename):
    """
    Finds the maximum wind speed for the hurricane.

    Parameters:
    1. hurricane_filename (type: string) - Name of the file containing the data

    Returns:
    (type: int) The maximum wind speed of the hurricane.
    """
    f = open(hurricane_filename, 'r')
    biggest = 0
    for line in f:
        vals = line.split(',')
        new_value = int(vals[4])
        if new_value > biggest:
            biggest = new_value
    return biggest



def contains_word(word, review):
    """
    Determines whether the review contains the given word. 

    Note that should ignore the "casing" of letters. For example "ok" is
    considered to be contained in the review "It was an OK movie."

    Parameters:
    1. word (type: string): The word to search for.
    2. review (type: string): The review in which to search.

    Returns:
    (type: boolean) True if word is contained in the review, and false
    otherwise.
    """
    word = word.lower()
    review = review.lower().split()
    if word in review:
        return True
    else:
        return False
    



def test_max_wind_speed():
    """ Function that tests the max_wind_speed function. """

    print("Starting test of max_wind_speed")

    # To Do: Call your max_wind_speed function on the irma.csv file, using an if
    irma_test = max_wind_speed("irma.csv")
     # statement to indicate whether the result was correct or not.
    if irma_test == 185:
        print("max_wind_speed(irma.csv)PASSED")
    else:
        print("max_wind_speed(irma.csv)FAILED")

    Florence_test = max_wind_speed("florence.csv")
    if Florence_test == 140:
        print("max_wind_speed(florence.csv)PASSED")
    else:
        print("max_wind_speed(florence.csv)FAILED")

    Dorian_test = max_wind_speed("Dorian.csv")
    if Dorian_test == 185:
        print("max_wind_speed(dorian.csv)PASSED")    
    else:
        print("max_wind_speed(dorian.csv)FAILED")
    # Then repeat the process for the florence.csv and dorian.csv files to check
    # whether your function works for those files.



    print("Done testing max_wind_speed")


def test_contains_word():
    """ Function that tests the contains_word function. """

    print("\nStarting test of contains word")

    if contains_word('ok', 'ok') != True:
        print("FAILED: contains_word('ok', 'ok')")
    elif contains_word('ok', 'OK') != True:
        print("FAILED: contains_word('ok', 'OK')")
    elif contains_word('ok', 'bad') != False:
        print("FAILED: contains_word('ok', 'bad')")
    elif contains_word('ok', 'movie ok') != True:
        print("FAILED: contains_word('ok', 'movie ok')")
    elif contains_word("God", "god") != True:
        print("FAILED: contains_word('God', 'god')")
    elif contains_word("god", "God") != True:
        print("FAILED: contains_word('god', 'God')")
    elif contains_word("god", "goddess") == True:
        print("FAILED: contains_word('god', 'goddess')")
    else:
        print("ALL TEST HAVE PASSED")
        print("Done testing contains word")


def main():
    """ Calls the tester functions in the code. """
    test_max_wind_speed()
    test_contains_word()

# Do not modify anything after this point.
if __name__ == "__main__":
    main()
