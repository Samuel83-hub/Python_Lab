def remove_char(s, char):
    return s.replace(char, "")

if __name__ == "__main__":
    s = input("Enter a string: ")
    char_to_remove = input("Enter the character to remove: ")

    result_removed = remove_char(s, char_to_remove)
    print(f"String after removing '{char_to_remove}': {result_removed}")
