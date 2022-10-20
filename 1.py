def conversion(CC):
    chislo_v_CC=''
    chislo=n
    while chislo>0:
        chislo_v_CC=str(chislo%CC)+chislo_v_CC
        chislo=chislo//CC
    return chislo_v_CC

n=int(input("Введите число: "))
CC=int(input("Введите целую систему счисления: "))
print(n, '-->', conversion(CC))
