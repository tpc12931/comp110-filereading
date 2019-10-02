"""
Module: comp110_lab05

Exercises from lab 05, dealing with strings and file reading.
"""

def max_windspeed(filename):
    """
    Finds the maximum windspeed for the hurricane.

    Parameters:
    1. filename (type: string) - Name of the file containing the data

    Returns:
    (type: int) The maximum windspeed of the hurricane.
    """

    pass # replace this line with your implementation of this function


def contains_word(word, review):
    """
    Determines whether the review contains the given word. 

    Note that this should work, regardless of case. For example "ok" is
    considered to be contained in the review "It was an OK movie."

    Parameters:
    1. word (type: string): The word to search for.
    2. review (type: string): The review in which to search.

    Returns:
    (type: boolean) True if word is contained in the review, and false
    otherwise.
    """

    pass # replace this line with your implementation of this function

def test_max_windspeed():
    """ Function that tests the max_windspeed function. """

    # To Do: Call your max_windspeed function on the irma.csv file.
    # Then use an if statement to check if the result was the expect result.
    # If it is, print out the message "max_windspeed('irma.csv') PASSED".
    # Otherwise, print out the message "max_windspeed('irma.csv') FAILED".

    # To Do: Repeat the previous "to do" but testing out florence.csv and
    # dorian.csv.

    print("Done testing max_windspeed")

def test_contains_word():
    """ Function that tests the contains_word function. """

    # To Do: Call your contains_word function for the word/review combination
    # given in the lab write-up. Again, you should check the return value and
    # print a message to indicate whether each test case passed or failed.

    print("Done testing contains word")


def main():
    test_max_windspeed()
    test_contains_word()

# Do not modify anything after this point.
if __name__ == "__main__":
    main()
