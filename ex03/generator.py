import random

def generator(text, sep=" ", option=None):
    '''
        Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings before it is yielded.
    '''
    try:
        text_list = text.split(sep)
    except AttributeError or TypeError:
        raise AssertionError("Text given is not a string") from None
        return 1
    except TypeError:
        raise AssertionError("Separator given is not a string") from None

    if option is None:
        for word in text_list:
            yield word
    elif option == "shuffle":
        for _ in range(len(text_list)):
            index = random.randint(0, len(text_list)-1)
            yield text_list[index]
            text_list.remove(text_list[index])
    elif option == "unique":
        aux_list = []
        for word in text_list:
            if word not in aux_list:
                aux_list.append(word)
                yield word
    elif option == "ordered":
        text_list.sort()
        for word in text_list:
            yield word
    else:
        raise AssertionError("Invalid option")
        return 1


def main():
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" "):
        print(word)
    print()
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print()
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print()
    text = "Lorem Ipsum Lorem Ipsum"
    for word in generator(text, sep=" ", option="unique"):
        print(word)
    print()
    for word in generator(text, sep=1):
        print(word)
    text = 1.0
    for word in generator(text, sep="."):
        print(word)


if __name__ == "__main__":
    main()
