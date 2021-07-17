def abc():
    print("LISTS:")
    a=[5,2,7,1,6,9,]
    print(a)
    ad=int(input("Enter an element to add in the list\n"))
    a.append(ad)
    print(a)
    print()
    ad=int(input("Enter the element to delete from the list\n"))
    a.remove(ad)
    print(a)
    print()
    print("Sorted list:")
    a.sort()
    print(a)
    print()
    print("\n\n")
    
    

abc()

def abc2():
    print("DICTIONARY:")
    a={0:"Konichiwa",1:"Ohaiyo",2:"Kawaii",3:"Baka",4:"konoyaro",5:"Utsukushi",6:"Arigatho"}
    inp=int((input("Enter a number from 0 to 6\n")))
    print(a[inp])
    print("\n\n")

abc2()



def abc3():
    print("TUPLES:")
    print("Tuples are immutable")
    a=('too','koo','poo')
    print(a)
    print("\n\n")
abc3()
  


def abc4():
    print("SETS:")
    a={0,1,2}
    b={2,3,4}
    print("Intersection",a&b)
    print()
    print("Union",a|b)
    print()
    print("A==B?",a==b)
    print()
    print("A-B",a-b)
    print()
    print("B-A",b-a)
    print()
    print("\n\n")
abc4()    
