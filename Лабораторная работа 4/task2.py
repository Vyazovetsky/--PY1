def get_count_char(str_):  # функция, котороая принимает строку
    letter_dict = {}  # и возвращает словарь с частотой каждого символа
    DEFAULT_COUNT = 0

    str_ = str_.lower()
    list_ = str_.split()
    # list_.sort() # если применить сортировку,как написано в тексте :)
    str_ = "".join(list_)

    for letter in str_:
        if letter.isalpha():
            letter_dict[letter] = letter_dict.get(letter, DEFAULT_COUNT) + 1

    return letter_dict

    # функция, которая принимает словарь символов
    # и возвращает новый словарь,где кол-во кажого эл-та
    # заменено на процентное соотношение ко всем элементам


def dict_char(dict_):
    total_char = sum(dict_.values())

    new_dict_ = {}

    for letter, value in dict_.items():
        new_dict_[letter] = round(((value / total_char) * 100), 1)

    return new_dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(dict_char(get_count_char(main_str)))
