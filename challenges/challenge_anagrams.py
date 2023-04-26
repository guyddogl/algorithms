def get_pivot(array, start, end):
    pivot = array[end]
    last_smaller = start - 1

    for current in range(start, end):
        if array[current] <= pivot:
            last_smaller += 1
            array[last_smaller], array[current] = (
                array[current],
                array[last_smaller],
            )

    array[last_smaller + 1], array[end] = array[end], array[last_smaller + 1]

    return last_smaller + 1


def sort(array, start, end):
    if end - start < 1:
        return

    pivot = get_pivot(array, start, end)
    sort(array, start, pivot - 1)
    sort(array, pivot + 1, end)


def is_anagram(first_string, second_string):
    word_one = first_string.lower()
    word_two = second_string.lower()

    list_word_one = [letter for letter in word_one]
    list_word_two = [letter for letter in word_two]

    sort(list_word_one, 0, len(list_word_one) - 1)
    sort(list_word_two, 0, len(list_word_two) - 1)

    is_anagram = list_word_one == list_word_two

    if first_string == "" or second_string == "":
        is_anagram = False

    return ("".join(list_word_one), "".join(list_word_two), is_anagram)
