from stats import get_num_words
from stats import get_char_count
from stats import print_report
import sys


# function to read the contents of a file and return it as a string
def get_book_text(book):
    """
    This function takes a filepath as input and returns the contents of the file as a string.
    """
    with open(book, 'r', encoding='utf-8') as file:
        # Read the contents of the file
        book_text = file.read()
    # Return the contents of the file
    return book_text


# main function - uses get_book_text with the relative path to your frankenstein.txt file to print the entire contents of the book to the console.
def main():
    # Get the text of the book from arguments
    # Check if the user provided a file path as an argument
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:        
        # print usage: 'Usage: python3 main.py <path_to_book>'
        print("Usage: python3 main.py <path_to_book>")        
        sys.exit(1)
    # Get the text of the book
    book_text = get_book_text(book_path)
    # Print the text of the book
    print_report(book_text, book_path)

if __name__ == "__main__":
    main()
