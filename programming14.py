#  Write a Python program to remove an item from a set if it is present in the set.
b= {1,2,2,3,'hello','ok','python'}
print(b)
if 'hello' in b:
    b.remove('hello')
    print(b)
else:
    print("not present")