# coding: utf-8

import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

with open(shoplistfile, 'wb') as f:
    pickle.dump(shoplist, f)

del shoplist

with open(shoplistfile, 'rb') as f:
    storedlist = pickle.load(f)
    print(storedlist)
