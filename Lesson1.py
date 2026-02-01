#Типы данных
#Python - с нестрогой типизацией

#get - понятно, что достаем из словаря, а через [] можно и из других типов
#если в словаре нет такого ключа, то get выдаст None, а [] ошибку
#словарь хорошо работает до 1000 элементов
#d1={'f':1,"s":2,"t":3}
w = 0
def my_func(p_a,p_b):
    global w
    for e in p_b:
        p_a[e]=p_b.get(e)
        if type(p_b[e]) != list:
            w += p_b.get(e)
        print(w)
        if type(p_b[e]) is list:
            for i in p_b[e]:
                if i == 41:
                    continue
                print(i)
    print(p_a)
d1={1:10}
print(d1)
my_func(d1,{2:20,3:30,4:[40,41,42,43],5:50})
print(d1)
print(w)
