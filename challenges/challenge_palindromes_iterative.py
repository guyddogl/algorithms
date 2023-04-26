def is_palindrome_iterative(word):
    if len(word) < 1:
        return False

    reverse = reversed(word)
    result = "".join(reverse)

    if word == result:
        return True

    return False
