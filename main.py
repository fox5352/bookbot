
def read_file(path: str) -> str:
    """
    Opens and reads the contents of a file.

    Args:
        path (str): The path to the file.

    Returns:
        str: The contents of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If an error occurs while reading the file.
    """
    with open(path, 'r', encoding="UTF-8") as f:
        return f.read()
    

def get_word_count(string: str) -> int:
    """
    Counts the number of words in a string.

    Args:
        string (str): The string to count words in.

    Returns:
        int: The number of words in the string.
    """
    return len(string.split())


def get_letter_count(string: str) -> dict:
    """
    Counts the number of occurrences of each letter in a string.

    Args:
        string (str): The string to count letters in.

    Returns:
        dict: The number of occurrences of each letter in the string.
    """
    buffer = dict()

    # loop string and count letters as lowercase letters and filter out spaces newlines and other non letters
    for letter in string.lower():
        if letter.isalpha():
            if letter in buffer:
                buffer[letter] += 1
            else:
                buffer[letter] = 1

    return buffer


def print_report(string: str, count: int, letters: dict) -> None:
    """
    Prints a report of a string.

    Args:
        string (str): The string to report.
        count (int): The number of words in the string.
        letters (dict): The number of occurrences of each letter in the string.
    """
    # convert letters dic into list of dics
    letters_list = list(letters.items())

    def sort_on(dic):
        return dic[1]

    # sort list by value
    letters_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print()

    for block in letters_list:
        print(f"The {block[0]} character was found {block[1]} times")
    
    print("--- End report ---")
    

def main():
    """
    The main function.
    """
    file_contents = read_file(path='./books/frankenstein.txt')

    count = get_word_count(string=file_contents)

    letters_count =  get_letter_count(string=file_contents)

    print_report(string=file_contents, count=count, letters=letters_count)

if __name__ == '__main__':
    main()
