def print_params (a = 1, b = 'строка', c = True):
    print("    ", a, b, c)


print("1. Функция с параметрами по умолчанию:")
print_params() # Начальные значения параметров функции по умолчанию
print_params(b=25) # Передаём int значение в изначальный str параметр (некритичная ошибка : Expected type 'str', got 'int' instead)
print_params(c=[1, 2, 3]) # Передаём list значение в изначальный bool параметр (некритичная ошибка : Expected type 'bool', got 'list[int]' instead)

print("2. Распаковка параметров:")
values_list : list = [1, "строка", True]
values_dict : dict = {"a" : 1, "b" : "строка", "c" : True}
print_params(*values_list) # Передача с распакавкой для list
print_params(**values_dict) # Передача с распакавкой для dict

print("3. Распаковка + отдельные параметры:")
values_list_2 : list = [54.32, "строка_2"]
print_params(*values_list_2, 42)