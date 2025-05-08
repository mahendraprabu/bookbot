# function to count words in a string
def get_num_words(text):
    """
    This function takes a string as input and returns the number of words in the string.
    """
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    # Return the number of words
    return len(words)

# Add a new function to your stats.py file that takes the text from the book as a string, and returns the number of times each character, 
# (including symbols and spaces), appears in the string.
# Convert any character to lowercase using the .lower() method, we don't want duplicates.
# Use a dictionary of String -> Integer. The returned dictionary should look something like this:
# {'p': 6121, 'r': 20818, 'o': 25225, ...

def get_char_count(text):
    """
    This function takes a string as input and returns a dictionary with the count of each character in the string.
    """
    # Create an empty dictionary to store the character counts
    char_count = {}
    
    # Iterate over each character in the text
    for char in text:
        # Convert the character to lowercase
        char = char.lower()
        # If the character is not already in the dictionary, add it with a count of 1
        if char not in char_count:
            char_count[char] = 1
        # If the character is already in the dictionary, increment its count by 1
        else:
            char_count[char] += 1
    
    # Return the dictionary with character counts
    return char_count

# Define a new function to print report. 
# ============ BOOKBOT ============
# Analyzing book found at books/frankenstein.txt...
# ----------- Word Count ----------
# Found 75767 total words
# --------- Character Count -------
# e: 44538
# t: 29493
# a: 25894
# o: 24494
# i: 23927
# n: 23643
# s: 20360
# r: 20079
# h: 19176
# d: 16318
# l: 12306
# m: 10206
# u: 10111
# c: 9011
# f: 8451
# y: 7756
# w: 7450
# p: 5952
# g: 5795
# b: 4868
# v: 3737
# k: 1661
# x: 691
# j: 497
# q: 325
# z: 235
# æ: 28
# â: 8
# ê: 7
# ë: 2
# ô: 1
# ============= END ===============

def print_report(book_text, book_path):
    """
    This function takes book_text, book_path as inputs and prints a report with the word count and character count.
    """

    # Get the number of words in the text
    num_words = get_num_words(book_text)
    # Get the character count
    char_count = get_char_count(book_text)
    # Get the sorted character count
    sorted_char_count = get_sorted_char_count(char_count)

    
    # Print the report
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_char_count:
        # If the character is not an alphabetical character (using the .isalpha() method), just skip it.
        if not char['char'].isalpha():
            continue
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


# Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
# Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
# Sort the list from greatest to least by the count.
# The .sort() method will be helpful here (see the hint).
def get_sorted_char_count(char_count):
    """
    This function takes a dictionary of character counts and returns a sorted list of dictionaries.
    Each dictionary contains the character and its count.
    """
    # Create a list of dictionaries from the character count dictionary
    sorted_char_count = [{"char": char, "num": count} for char, count in char_count.items()]
    
    # Sort the list by the count in descending order
    sorted_char_count.sort(key=lambda x: x["num"], reverse=True)
    
    # Return the sorted list
    return sorted_char_count

