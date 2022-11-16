def modal(lis = [], mayor = True):
    first_flag = True
    mod = ""
    if mayor:
        lis.sort(reverse = True)
        print(lis)
    else:
        lis.sort()
        print(lis)

    for i in lis:
        cant = lis.count(i)
        if first_flag:
            mod = [i, cant]
            first_flag = False
        elif cant > mod[1]:
            mod = [i, cant]
    return mod

print(modal([1,1,1,3,3,3], False))