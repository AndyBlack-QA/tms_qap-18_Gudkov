# 1 Привести к целому типу - 1.6, 2.99
def to_int(arr):
    whole = int(arr)
    return whole


print(to_int(1.6))
print(to_int(2.99))

# 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
str_my_site = "www.my_site.com#about"


def replace_sharp_by_slash(site):
    return site.replace('#', '/')


print(replace_sharp_by_slash(str_my_site))

# 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’


def str_plus_ing(string):
    return string + "ing"


print(str_plus_ing('zxcv'))

# 4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
str_ivanou_ivan = 'Ivanou Ivan'


def replace_name_and_surname_place(name_surname):
    str_to_list = (name_surname.split())
    name_surname = str_to_list[1] + ' ' + str_to_list[0]
    return name_surname


print(replace_name_and_surname_place(str_ivanou_ivan))