import timeit

def checkio(text):
    start = timeit.default_timer()

    container = {}
    text = text.lower()
    # Remove special carakters and sort alphabetic
    valids = []
    for character in text:
        if character.isalpha():
            valids.append(character)
    text =  ''.join(sorted(valids))

    for l in text:
        if l in container:
            container[l] = container[l] +1
        else:
            container[l] = 1
    result = max(container, key=lambda i: container[i])

    stop = timeit.default_timer()
    print(stop - start)
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
