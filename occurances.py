def count_char_occurrences(s, char):
    return s.count(char)

if __name__ == "__main__":
    s = input("Enter a string: ")
    char_to_count = input("Enter the character to count: ")

    result_count = count_char_occurrences(s, char_to_count)
    print(f"Count of '{char_to_count}' in '{s}': {result_count}")
