#Uloha 1
def fun1():
    for i in range(1,11):
        print (i)
#fun1()


#Uloha 2 a
def fun2a():
    a = int(input("Zadaj hodnotu:"))
    for x in range(1, a + 1):
        print(x)
#fun2()


#Uloha 2 b
def fun2b():
    a = int(input("Zadaj hodnotu: "))
    for x in range(1, a + 1):
        if x == a:
            print(x, end="")                    #pri tomto som si musel pomôcť internetom pretože som nevedel ako to vypísať za sebou,
        else:                                   #našiel som si že na to existuje funkcia end a potom som to dorobil celé sám
            print(x, end=", ")
#fun2b()


#Uloha 3
def fun3():
    for i in range(5,16):
        if i % 2 == 1:
            print(i)
#fun3()


#Uloha 4
def fun4(N):
    for i in range(1, N +1):
        print (i,":", i ** 2 )
#fun4(9)


#Uloha 5
def fun5(odkial, pokial):
    for i in range(1, pokial +1):
        odmocnina = round(i ** 0.5, 2)                  #aj ked sme funkciu round nepoužívali tento rok, pamatam si ju z minule roťníka
        print (i,":", odmocnina )
#fun5(1, 10)


#Uloha 6
def fun6():
    for x in range(1, 21):
        if x - 3 == 0:
            print ("x =", x, "funkcia nie je definovaná")
        else:
            y = (x ** 2 - 1) / (x - 3)
            print("x =", x, "y =", y)
#fun6()


#Uloha 7
def fun7(N):
    for i in range(1, N +1):
        if i % 3 == 0:
            print (i)
#fun7(30)


#Uloha 8
def fun8():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)
#fun8()


#Uloha 9
def fun9():
    z = int(input("Zadaj začiatočnú hodnotu:"))
    k = int(input("Zadaj konečnú hodnotu:"))
    for i in range (z, k + 1):
        if i % 2 != 0:
            print(i)
#fun9()


#Uloha 10
def fun10():
    N = int(input("Zadaj hodnotu:"))
    for i in range(N, 0, -1):                       #N = odkial, 0 = pokial, -1 = o kolko sa má zniznit
        print(i)
#fun10()


#Uloha 11
def fun11():
    N = int(input("Zadaj hodnotu:"))
    for i in range(1, N):
        if i % 7 == 0 and i % 4 == 0:
            print(i)
#fun11()

#Uloha 12
def fun12(N):
    x = 0
    for i in range(1, N+1):
        x += i
    return x
#print(fun12(10))


#Uloha 13
def fun13(N):
    x = 0
    for i in range(1, N):
        if i % 2 == 0:
            x += i
    return x
#print(fun13(10))


#Uloha 14
def fun14(z, k):
    x = 0
    for i in range(z, k + 1):
        if i % 8 == 0:
           x += 1
    return x
#print(fun14(1, 80))