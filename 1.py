def format_text():
    # Дана строка
    s = "Python is a high level, general-purpose programming language."

    # Нужно написать код который форматирует данную строку
    # в текст вида
    """
    Python is a
    high level, general-purpose
    programming language.
    """

    ##############################
    # Решение

    new_s = ""

    for index, itm in enumerate(s.split(" ")):
        if index % 3 == 0:
            new_s += f"\n{itm} "

        else:
            new_s += f"{itm} "

    return new_s


print(format_text())
