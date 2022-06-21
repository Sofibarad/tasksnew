# sukurti funkcija, kuri grazintu lista jame sugeneruotais random integeriais, kurie negali buti maziau uz 0 daugiau 100 turi buti grazintas nuo min
# iki max

# import random

# def list_generator():
#     my_list = []
#     for x in range(0, 6):
#         my_list.append(random.randint(0, 100))
#     return sorted(my_list)

# print(list_generator())

import random

def list_generator() ->list:
    return sorted ([random.randint(0, 100) for _ in range (0, 6)])
print(list_generator())





