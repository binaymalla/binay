# Write a Python program to convert a tuple to a string.
tuple = ('a', 'b', 'h', 'y', 'a', 's')
j=''
for i in tuple:
    i=j+i
    print(i,end='')
print()
print(type(i))




def convertTuple(cup):
		# initialize an empty string
	str = ''
	for item in cup:
		str = str + item
	return str


# Driver code
tuple = ('h', 'e', 'l', 'l', 'o','w','o','r','l','d')
str = convertTuple(tuple)
print(str)


 