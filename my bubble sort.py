def bubble_sort(p_l):
    for x in range(len(p_l) - 1):
        print(x)
        for i in range(len(p_l)-1-x):
            if p_l[i] > p_l[i+1]:
                p_l[i],p_l[i + 1] = p_l[i + 1],p_l[i]
            print(p_l)

list1 = list(range(10,0,-1))
print(list1)
bubble_sort(list1)
print(list1)