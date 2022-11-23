from pprint import pprint

numbers = 15
list_ = [{'bin': bin(num), 'dec': num, 'oct': oct(num), 'hex': hex(num)} for num in range(numbers + 1)]

pprint(list_)
