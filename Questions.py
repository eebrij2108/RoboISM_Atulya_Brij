def func1(lst,st):
    if st=="asc":
        lst.sort()
    elif st=="desc":
        lst.sort(reverse=True)
    else:
        pass
    print(lst)
print("func1")
func1([1,4,2,3,8,5,6,9],"asc")
func1([1,4,2,3,8,5,6,9],"desc")
print()
    
def func2(credit):
    lst = list(credit)
    n = len(lst)
    for i in range(0,n-4):
        lst[i]="*"
    st = "".join(lst)
    print(st)
print("func2")
func2("123456787654323456765")
func2("345678987654345678")
print()


def func3(p1,p2,p3):
    print(eval(p1+p2+p3))
print("func3")
func3("1","+","3")
func3("2","*","10")
print()

def func4(st):
    lst = list(st)
    lst2 = []
    for i in lst:
        j=i*2
        lst2.append(j)
    st2 = "".join(lst2)
    print(st2)
print("func4")
func4("gdft837eygbhed8u97ye21")
func4("eufvg3te76uiedhb")
print()
    
def func5(arr):
    arr2=[]
    for i in arr:
        if i in arr2:
            print(i)
            break
        else:
            pass
        arr2.append(i)
print("func5")
func5([1,2,3,4,5,6,7,8,9,10,11,12,13,5,60,56])
print()


def func6(ran): # ran in form [x,y]
    for a in range(ran[0],ran[1]):
        if a>1:
            for i in range(2,a):
                if a%i==0:
                    break
            else:
                print(a)
print("func6")
func6([1,20])
func6([50,80])
print()

def func7(arr):
    max = 0
    ans = arr[0]
    for i in arr:
        frequency = arr.count(i)
        if frequency > max:
            max = frequency
            ans = i
    print(ans)
print("func7")
func7([1,2,3,3,4,3,5,6,6,7,8,9,10,3,3,3,3,3,3])
print()

def func8(str):
    lst = list(str)
    lst2 = ['1','2','3','4','5','6','7','8','9','0']
    sumo = 0
    for i in lst:
        if i in lst2:
            sumo+=int(i)
    print(sumo)
print("func8")
func8("h20 15 wa73r")
func8("jhgfcg8765rdfg654edg7yh 654edfgh7b 7ygv")
print()
      
def func9(str):
    lst = list(str)
    lst.sort()
    str2 = "".join(lst)
    print(str2)
print("func9")
func9("sdfygfdcfgyuyhgvhuhg")
func9("zawedsxcftrfdcvbvfyhjnmkiu")
print()

def func10(x,y):
    x = x^y
    y = x^y
    x = x^y
    print(x)
    print(y)
print("func10")
func10(2,3)
func10(4,3)
print()
    
def func11(str):
    lst = list(str)
    if lst == lst[::-1]:
        print("YES")
    else:
        print("NO")
print("func11")
func11("asddsa")
func11("brij")
func11("robobor")
print()

def func12(arr):
    arr.sort()
    for i in range(0,len(arr)):
        if arr[i]==arr[i+1]:
            print(arr[i])
            break
print("func12")
func12([1,2,3,3,4,5,7])
func12([1,4,7,9,2,3,7])
print()


def func15():
     str=input('Input a string')
     count1=0
     count2=0
     count3=0
     count4=0
     for i in str:
        if i.isdigit():
            count1+=1
        elif i.isalpha():
            count2+=1
        elif i.isspace():
            count3+=1
        else:
            count4+=1
     print(str)
     print('Digits:',count1)
     print('Alphabets:',count2)
     print('Special Characters:',count4)
print("func15")
func15()
func15()
print()

def func16(n):
    lst=[]
    b=2
    while len(lst)<n:
        for i in range(2,b):
            if b%i==0:
                break
        else:
            lst.append(b)
        b=b+1
    print(lst,end=' ')
print("func16")
func16(10)
print()

def func18(lst):
    a=True
    b=True
    while (a or b)==True:
        if (('NORTH' in lst) and ('SOUTH' in lst))==True:
            lst.remove('NORTH')
            lst.remove('SOUTH')
        else:
            a=False
        if (('EAST' in lst) and ('WEST' in lst))==True:
            lst.remove('EAST')
            lst.remove('WEST')
        else:
            b=False
            
    print(lst)
print("func18")
func18(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST'])
print()

def func19():            
    import random
    number = random.randint(0,9999)
    guess = int(input("GUESS:"))
    lst = list(str(guess))
    num = list(str(number))
    check = True
    for i in lst:
        if i in num:
            pass
        else:
            check = False
    if check == False:
        print("B")
    else:
        if lst == num:
            print("R")
        else:
            print("Y")
print("func19")
func19()
print()

def func20():
    def prime(num):
        prime = False
        for i in range(2,num):
            if  num%i==0:
                break
    
        else:
            prime = True
        return prime
            
    import itertools as it
    def rotation(lsti):
        n = len(lsti)
        list2=[]
        for i in range(n):
            a = lsti[i:n]+lsti[0:i]
            list2.append(a)
        return list2
    b = list(it.combinations_with_replacement('1379', 6))
    c = list(it.combinations_with_replacement('1379', 5))
    d = list(it.combinations_with_replacement('1379', 4))
    e = list(it.combinations_with_replacement('1379', 3))
    f = list(it.combinations_with_replacement('1379', 2))
    g = list(it.combinations_with_replacement('1379', 1))
    lst =  b + c + d + e + f + g
    Total = 1 #1 because 5 was excluded in taking digits and 5 is a prime number . But for other numbers some rotation having 5 at last is composite. 
    for i in lst:
        num = int("".join(list(i)))
        if prime(num)==True:
            check = True
            h = rotation(list(str(num)))
            for k in h:
                num2 = int("".join(list(k)))
                if prime(num2)==False:
                        check=False
            if check == True:
                Total = Total + len(str(num))
                
    print(Total)
    # 1 is neither composite nor prime
    # 2 is prime number
    # If we use 2,4,6,8,5 , the number will definietly not a prime in one of its rotations
    # Program assumes 2 as 1 , but there is no change in final answer
print("func20")
func20()
