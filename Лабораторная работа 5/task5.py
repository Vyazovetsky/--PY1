import random
import string


def get_random_password(n=None) -> str:
    # создаём строку из уникальных элементов, по которой будет генерироваться пароль
    start_str_ = string.ascii_uppercase + string.ascii_lowercase + string.digits

    # проверяем длину пароля
    if n is None:  # если длина не задана,то по умолчанию пароль длиной в 8 символов
        n = 8

    elif n >= len(start_str_):  # проверка на длину пароля, иначе пароль не получится создать только из уникальных элементов
        print("Слишком длинный пароль! Введите не больше 62 символов пароля, либо воспользуйтесь паролем из 8 символов:")
        n = 8

    # генерируем список из различных уникальных элементов из созданной строки
    new_list_ = random.sample(start_str_, n)

    # образуем пароль из сгенерированных чисел
    str_ = "".join(new_list_)

    return str_


print(get_random_password())
