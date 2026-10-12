# ==============================================================
# PYTHON STRINGS ASSIGNMENT
# ==============================================================

# COVER PAGE
# Name: [Angel Gabriel Euresti Conde]
# Student ID: []
# Group: [1-2]
# File name: matricula_ApellidoNombre_t_strings.py
# GitHub Repository: [GITHUB REPOSITORY URL]


# ==============================================================
# EXECUTIVE SUMMARY
# ==============================================================

# A string is a Python data type used to represent a sequence of text
# characters. Strings are immutable, which means that their original
# contents cannot be changed directly; operations create new strings.
# Python provides operations such as concatenation, length calculation,
# indexing, slicing, searching, replacing, splitting, and joining.
# Input validation is important because it prevents empty, malformed,
# or unexpected data from being processed.
# Text normalization using methods such as strip(), lower(), upper(),
# and title() helps make comparisons and formatting more consistent.
# This document contains six problems focused on practical string
# manipulation, validation, transformation, formatting, and testing.
# Each problem includes its description, inputs, outputs, validations,
# three test cases, and a complete Python implementation.


# ==============================================================
# PRINCIPLES AND BEST PRACTICES
# ==============================================================

# - Strings are immutable: any modification creates a new string.
# - It is good practice to normalize input using strip() and lower()
#   before comparing text when appropriate.
# - Avoid magic numbers in indexes; document what each slice extracts.
# - Use built-in string methods instead of rewriting basic logic.
# - Design clear validations: first check that the input is not empty,
#   then validate its expected format.
# - Write readable code using descriptive variable names and clear
#   error messages.
# - Use lower_snake_case for variables and UPPER_SNAKE_CASE for
#   constants.
# - String processing should be separated from validation whenever
#   possible to make the program easier to understand and test.


# ==============================================================
# PROBLEM 1: FULL NAME FORMATTER
# ==============================================================

# Description:
# Receives a person's full name as one string.
# The program removes unnecessary spaces, converts the name to
# Title Case, and generates initials separated by periods.
#
# Inputs:
# - full_name: a string containing at least two words.
#
# Outputs:
# - Formatted name in Title Case.
# - Initials in the format X.X.X.
#
# Validations:
# - The input cannot be empty after strip().
# - The input must contain at least two words.
# - Strings containing only spaces are rejected.
#
# Test cases:
# 1) Normal: "juan carlos tovar" -> "Juan Carlos Tovar", "J.C.T."
# 2) Border: " Ana Lopez " -> "Ana Lopez", "A.L."
# 3) Error: "   " -> Error: invalid input


def format_full_name(full_name):
    full_name = full_name.strip()

    if full_name == "":
        print("Error: invalid input")
        return

    name_parts = full_name.split()

    if len(name_parts) < 2:
        print("Error: at least two words are required")
        return

    formatted_name = " ".join(name_parts).title()

    initials = ""
    for part in name_parts:
        initials += part[0].upper() + "."

    print("Formatted name:", formatted_name)
    print("Initials:", initials)


# ==============================================================
# PROBLEM 2: SIMPLE EMAIL VALIDATOR
# ==============================================================

# Description:
# Validates an email address using a simple structure.
# The email must contain exactly one '@', no spaces, and at least
# one period after the '@' character.
#
# Inputs:
# - email_text: a string containing an email address.
#
# Outputs:
# - Valid email: true/false
# - Domain if the email is valid.
#
# Validations:
# - The input cannot be empty after strip().
# - The email must contain exactly one '@'.
# - The email cannot contain spaces.
# - A period must appear after '@'.
# - There must be text before and after '@'.
#
# Test cases:
# 1) Normal: "student@example.com" -> valid
# 2) Border: "a@b.c" -> valid
# 3) Error: "student example.com" -> invalid


def validate_email(email_text):
    email_text = email_text.strip()

    if email_text == "":
        print("Error: invalid input")
        return

    if " " in email_text:
        print("Valid email: false")
        return

    at_count = email_text.count("@")

    if at_count != 1:
        print("Valid email: false")
        return

    at_position = email_text.find("@")

    if at_position <= 0:
        print("Valid email: false")
        return

    domain_part = email_text[at_position + 1:]

    if domain_part == "":
        print("Valid email: false")
        return

    if "." not in domain_part:
        print("Valid email: false")
        return

    dot_position = domain_part.find(".")

    if dot_position <= 0 or dot_position == len(domain_part) - 1:
        print("Valid email: false")
        return

    print("Valid email: true")
    print("Domain:", domain_part)


# ==============================================================
# PROBLEM 3: PALINDROME CHECKER
# ==============================================================

# Description:
# Determines whether a phrase is a palindrome.
# Spaces and letter case are ignored during the comparison.
#
# Inputs:
# - phrase: a string containing a phrase.
#
# Outputs:
# - Is palindrome: true/false
# - Normalized phrase.
#
# Validations:
# - The phrase cannot be empty after strip().
# - The cleaned phrase must contain at least three characters.
#
# Test cases:
# 1) Normal: "Anita lava la tina" -> true
# 2) Border: "aba" -> true
# 3) Error: "ab" -> Error: input is too short


def check_palindrome(phrase):
    phrase = phrase.strip()

    if phrase == "":
        print("Error: invalid input")
        return

    normalized_phrase = phrase.lower().replace(" ", "")

    if len(normalized_phrase) < 3:
        print("Error: input must contain at least 3 characters")
        return

    reversed_phrase = normalized_phrase[::-1]

    print("Normalized phrase:", normalized_phrase)

    if normalized_phrase == reversed_phrase:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")


# ==============================================================
# PROBLEM 4: SENTENCE WORD STATS
# ==============================================================

# Description:
# Receives a sentence, removes unnecessary spaces, and separates
# it into words. The program calculates the number of words and
# identifies the first, last, shortest, and longest words.
#
# Inputs:
# - sentence: a string containing one or more words.
#
# Outputs:
# - Word count
# - First word
# - Last word
# - Shortest word
# - Longest word
#
# Validations:
# - The sentence cannot be empty after strip().
# - The sentence must contain at least one word.
#
# Test cases:
# 1) Normal: "Python is very useful"
# 2) Border: "Hello"
# 3) Error: "     "


def sentence_word_stats(sentence):
    sentence = sentence.strip()

    if sentence == "":
        print("Error: invalid input")
        return

    words = sentence.split()

    if len(words) == 0:
        print("Error: no valid words found")
        return

    shortest_word = words[0]
    longest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word

        if len(word) > len(longest_word):
            longest_word = word

    print("Word count:", len(words))
    print("First word:", words[0])
    print("Last word:", words[-1])
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)


# ==============================================================
# PROBLEM 5: PASSWORD STRENGTH CLASSIFIER
# ==============================================================

# Description:
# Classifies a password as weak, medium, or strong.
#
# Rules:
# - Weak: length is less than 8 characters.
# - Medium: length is at least 8 and contains letters/digits but
#   does not satisfy all strong requirements.
# - Strong: length is at least 8 and contains at least one uppercase
#   letter, one lowercase letter, one digit, and one special symbol.
#
# Inputs:
# - password_input: a string containing a password.
#
# Outputs:
# - Password strength: weak/medium/strong
#
# Validations:
# - The password cannot be empty.
# - Password length is checked before classification.
#
# Test cases:
# 1) Normal: "Password123!" -> strong
# 2) Border: "Abcdef12" -> medium
# 3) Error: "" -> Error: invalid input


def classify_password(password_input):
    password_input = password_input.strip()

    if password_input == "":
        print("Error: invalid input")
        return

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    password_length = len(password_input)

    if password_length < 8:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    print("Password strength:", strength)


# ==============================================================
# PROBLEM 6: PRODUCT LABEL FORMATTER
# ==============================================================

# Description:
# Creates a product label with a fixed width of exactly 30 characters.
# The format is:
# Product: <NAME> | Price: $<PRICE>
#
# If the generated label is shorter than 30 characters, spaces are
# added to the right. If it is longer than 30 characters, it is
# truncated to exactly 30 characters.
#
# Inputs:
# - product_name: product name.
# - price_value: positive numeric price.
#
# Outputs:
# - Label containing exactly 30 characters.
#
# Validations:
# - Product name cannot be empty after strip().
# - Price must be convertible to a positive number.
#
# Test cases:
# 1) Normal: "Notebook", "25.50"
# 2) Border: "Pen", "1"
# 3) Error: "Laptop", "-50"


def format_product_label(product_name, price_value):
    product_name = product_name.strip()
    price_value = price_value.strip()

    if product_name == "":
        print("Error: invalid product name")
        return

    if price_value == "":
        print("Error: invalid price")
        return

    try:
        numeric_price = float(price_value)
    except ValueError:
        print("Error: price must be numeric")
        return

    if numeric_price <= 0:
        print("Error: price must be positive")
        return

    label = f"Product: {product_name} | Price: ${price_value}"

    if len(label) > 30:
        label = label[:30]
    else:
        label = label + (" " * (30 - len(label)))

    print("Label:", f'"{label}"')
    print("Label length:", len(label))


# ==============================================================
# TEST SECTION
# ==============================================================

# The following section executes the three required test categories
# for every problem:
# - Normal case
# - Border case
# - Error case


def run_all_tests():
    print("=" * 60)
    print("PROBLEM 1 TESTS")
    print("=" * 60)

    print("\nNormal case:")
    format_full_name("juan carlos tovar")

    print("\nBorder case:")
    format_full_name(" Ana Lopez ")

    print("\nError case:")
    format_full_name("   ")


    print("\n" + "=" * 60)
    print("PROBLEM 2 TESTS")
    print("=" * 60)

    print("\nNormal case:")
    validate_email("student@example.com")

    print("\nBorder case:")
    validate_email("a@b.c")

    print("\nError case:")
    validate_email("student example.com")


    print("\n" + "=" * 60)
    print("PROBLEM 3 TESTS")
    print("=" * 60)

    print("\nNormal case:")
    check_palindrome("Anita lava la tina")

    print("\nBorder case:")
    check_palindrome("aba")

    print("\nError case:")
    check_palindrome("ab")


    print("\n" + "=" * 60)
    print("PROBLEM 4 TESTS")
    print("=" * 60)

    print("\nNormal case:")
    sentence_word_stats("Python is very useful")

    print("\nBorder case:")
    sentence_word_stats("Hello")

    print("\nError case:")
    sentence_word_stats("     ")


    print("\n" + "=" * 60)
    print("PROBLEM 5 TESTS")
    print("=" * 60)

    print("\nNormal case:")
    classify_password("Password123!")

    print("\nBorder case:")
    classify_password("Abcdef12")

    print("\nError case:")
    classify_password("")


    print("\n" + "=" * 60)
    print("PROBLEM 6 TESTS")
    print("=" * 60)

    print("\nNormal case:")
    format_product_label("Notebook", "25.50")

    print("\nBorder case:")
    format_product_label("Pen", "1")

    print("\nError case:")
    format_product_label("Laptop", "-50")


# ==============================================================
# MAIN PROGRAM
# ==============================================================

if __name__ == "__main__":
    run_all_tests()


# ==============================================================
# CONCLUSIONS
# ==============================================================

# String manipulation is essential for processing user input and
# producing clear and useful output in Python programs.
# Methods such as strip(), lower(), split(), join(), replace(), and
# title() are useful for cleaning, normalizing, and transforming text.
# Normalizing text before comparisons makes programs more reliable
# when users enter different combinations of spaces and capitalization.
# Clear validation prevents empty, malformed, or invalid data from
# reaching the processing stage and causing unexpected results.
# The exercises also demonstrate that strings are immutable, so
# operations such as replace() and lower() return new strings.
# Slicing provides a simple way to extract or truncate portions of
# strings, which was especially useful for the fixed-width label.
# Overall, these exercises demonstrate practical string techniques
# that can be applied to many real-world programming problems.


# ==============================================================
# REFERENCES
# ==============================================================

# 1) Python Documentation - Built-in Types:
#    Text Sequence Type — str
#
# 2) Python Documentation - Common String Operations
#
# 3) Python Documentation - Built-in Functions:
#    len()
#
# 4) Python Documentation - String Methods:
#    split(), join(), replace(), find(), strip()
#
# 5) Python Documentation - String Formatting:
#    Formatted String Literals (f-strings)
#
# 6) Python Documentation - Built-in Types:
#    Numeric Types and Boolean Type
#
# 7) Python Software Foundation - Python Tutorial:
#    More Control Flow Tools and Data Structures
#
# GitHub Repository:
# [GITHUB REPOSITORY URL]