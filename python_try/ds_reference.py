# coding: utf-8

print('Sample Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist is just another name pointing to the same object!
mylist = shoplist

# I purchased the first item, so, I remove it from the list
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is ', mylist)

# notice the both shoplist and mylist both point
# the same list without the 'apple' confirming that
# they point to the same object

print('Copy by making a full slce')
# make a copy by doing a full slice
mylist = shoplist[:]
del mylist[0]

print('shopping list is ', shoplist)
print('mylist is ', mylist)

# notice that now the two lists are different
