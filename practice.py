# Using the format method to create a string from user input

n1 = input('Enter a noun:')
v = input('Enter a verb:')
adj = input('Enter an adjective:')
n2 = input('Enter a noun:')

r = '''The {} {} the {} {}'''.format(n1, v, adj, n2)

print(r)


# Using split method to separate full name into first, last, etc.
# Possibly create as a function for use on file input

fName = ' '
mName = ' '
lName = ' '

name = input('Enter the full name: ')

split_name = name.split(' ')

if len(split_name) == 2:
    fName = split_name[0]
    lName = split_name[1]
else:
    fName = split_name[0]
    mName = split_name[1]
    lName = split_name[2]

print('First name is - ' + fName)
print('Middle name is - ' + mName)
print('Last name is - ' + lName)


        
    
