def get_vowels(text: str) -> str:
    """Extract vowels from the input string and return them in a comma-separated format."""
    vowels = "aeiouAEIOU"
    extracted = [char for char in text if char in vowels]
    return ", ".join(extracted)


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print(get_vowels(user_input))

# this is a comment added to the file