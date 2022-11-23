import random


def get_unique_list_numbers() -> list[int]:

    length = 15  # размер списка

    # диапозон случайных чисел
    min_number = -10
    max_number = 10

    # создаю множество рандомных уникальных чисел в указанном диапозоне
    list_ = set([random.randint(min_number, max_number + 1) for _ in range(length)])

    # создаю множество всевозможных чисел в указанном диапозоне
    new_list_ = set([n for n in range( min_number, max_number + 1)])

    # нахожу разность между эти множествами, откуда получаю список уникальных чисел, не совпадающих с исходным
    new_list_ = list(new_list_.difference(list_))

    # перемешиваю получившийся список уникальных чисел
    random.shuffle(new_list_)

    # пришиваю этот список к исходному списку уникальных чисел
    list_ = list(list_) + [n for n in list(new_list_)]

    # обрезаю этот список на заданной длине
    list_ = list_[:length]

    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
