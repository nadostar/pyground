# coding: utf-8

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# indexing or 'Subscription' operation
for index, item in enumerate(shoplist):
    print('Item {} is {}'.format(index, item))


print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
