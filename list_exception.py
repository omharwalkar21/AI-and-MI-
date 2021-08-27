from array import*
ls = [10,20,30,40,50,60,70,80]
try:
    print(ls[int(input("Enter number: "))])
except Exception as e:
    print("we cannot access list out of bound index /",e)

a = array('i',[1,2,3,4,5])
try:
    print(a[int(input("Enter numer: "))])
except Exception as e:
    print("we cannot access array out of bound index element / ",e)
finally:
    print("Successfully Executed")
