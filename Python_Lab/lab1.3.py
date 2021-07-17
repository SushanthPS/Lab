
print("\"CMR\" \"University\"");

'''
a=int(input("Enter value of a\n"));
b=int(input("Enter value of b\n"));
print("Addition of ",a," and ",b," is: ",a+b);
print("multiplication of ",a," and ",b," is: ",a*b);
print("division of ",a," and ",b," is: ",b/a);
print("subtraction of ",a," and ",b," is: ",b-a);
print("square of ",a,"^",b," is: ",a**b);
print("\n\n\n");
'''
def fibo():
    a=0;
    b=1;
    n=int(input("Enter number of fibonacci numbers required\n"));
    print("The fibonacci series is: \n");
    print(a);
    print(b);
    for i in range(n-2):
        c=a+b;
        print(c);
        a=b;
        b=c;
        
fibo();

def swap():
    print("\n\n\n");
    a=input("Enter the value of a: ");
    b=input("Enter the value of b: ");
    c=a;
    a=b;
    b=c;
    print("The value of a after swapping is: ",a);
    print("The value of b after swapping is: ",b);

swap();
