word = input()
print(word)
store = dict()

for ch in word:
    if ch in store:
        store[ch] = store[ch] + 1
    else:
        store[ch] = 1
print(store)
resultchar = '#'
resultfrequency = 0

allkeys = store.keys()
for ele in allkeys:
    if store[ele] > resultfrequency:
       resultfrequency = store[ele]
       resultchar = ele
print(resultchar, resultfrequency) 


OUTPUT:

abeabedrtrtkasrdkfva
{'a': 4, 'b': 2, 'e': 2, 'd': 2, 'r': 3, 't': 2, 'k': 2, 's': 1, 'f': 1, 'v': 1}
a 4
