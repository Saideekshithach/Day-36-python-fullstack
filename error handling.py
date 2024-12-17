'''There are 3 types of errors
1.syntax error->compile error
2.run time error-> during execution time it will happens
3.logical error-> error in logic(can't visible)'''
#syntax error
'''for i in range(10):
print(i)'''
#run time error
'''a=int(input("a value:"))
b=int(input("b value:"))
print(a//b)#10/0->zero division error'''

#logical error
'''a=10
b=20
print(a-b)'''


#Exception handling
'''try->Instructions from which we are expecting the exceptions
except->exceptions are raised in try block.It will be handled by the block.
else->optional(no exceptions)
finally->always'''

a=int(input("a value:"))
b=int(input("b value:"))
try:
    c=a//b
    print(c)
'''#except:
    print("exception is raised")
#else:
    print("optional")'''
finally:
    print("always")

