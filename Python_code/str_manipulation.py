def demonstrate_string_operations():
    print("1. String Concatenation:")
    first = "Hello"
    second = "World"
    # Using + operator
    result1 = first + " " + second
    print(f"Using + operator: {result1}")
    
    # Using join()
    words = ["Hello", "World"]
    result2 = " ".join(words)
    print(f"Using join(): {result2}")
    print()

    print("2. String Repetition:")
    word = "Ha"
    result = word * 3
    print(f"Repeating 'Ha' three times: {result}")
    print()

    print("3. String Indexing and Slicing:")
    text = "Python"
    first_char = text[0]
    last_char = text[-1]
    slice_text = text[1:4]
    reverse = text[::-1]
    print(f"Original text: {text}")
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")
    print(f"Slice (1:4): {slice_text}")
    print(f"Reversed: {reverse}")
    print()

    print("4. String Case Manipulation:")
    text = "Python Programming"
    print(f"Original text: {text}")
    print(f"Upper case: {text.upper()}")
    print(f"Lower case: {text.lower()}")
    print(f"Title case: {text.title()}")
    print()

    print("5. Finding and Replacing:")
    text = "Hello World"
    pos = text.find("World")
    new_text = text.replace("World", "Python")
    print(f"Original text: {text}")
    print(f"Position of 'World': {pos}")
    print(f"After replacing 'World' with 'Python': {new_text}")
    print()

    print("6. Checking String Content:")
    text = "Python123"
    print(f"Text to check: {text}")
    print(f"Is alphabetic? {text.isalpha()}")
    print(f"Is alphanumeric? {text.isalnum()}")
    print(f"Is digit? {text.isdigit()}")
    print(f"Starts with 'Py'? {text.startswith('Py')}")
    print(f"Ends with '123'? {text.endswith('123')}")
    print()

    print("7. Stripping Whitespace:")
    text = "  Hello World  "
    print(f"Original text: '{text}'")
    print(f"After strip(): '{text.strip()}'")
    print(f"After lstrip(): '{text.lstrip()}'")
    print(f"After rstrip(): '{text.rstrip()}'")
    print()

    print("8. Splitting and Joining:")
    text = "Hello,World,Python"
    words = text.split(",")
    print(f"Original text: {text}")
    print(f"After splitting: {words}")
    
    words = ["Hello", "World"]
    joined_text = "-".join(words)
    print(f"Joining words with '-': {joined_text}")
    print()

    print("9. Format Strings:")
    name = "Alice"
    age = 25
    # Using format()
    text1 = "I am {} and I'm {} years old".format(name, age)
    # Using f-strings
    text2 = f"I am {name} and I'm {age} years old"
    print(f"Using format(): {text1}")
    print(f"Using f-string: {text2}")
    print()

    print("10. Checking Membership:")
    text = "Python Programming"
    print(f"Text to check: {text}")
    print(f"'Python' in text: {'Python' in text}")
    print(f"'Java' in text: {'Java' in text}")

if __name__ == "__main__":
    demonstrate_string_operations()
