#dictionaries creating

word = input()
print(word)
store = dict()
print(store)

store['q'] = 12
store['p'] = 23
store['W'] = 18
store["channaveeresh"] = 17
print(store)

allkeys = store.keys()
print(allkeys)

allvalues = store.values()
print(allvalues)

#for each loop
for ele in allkeys:
    print(ele)

for ch in "channaveeresh":
    print(ch)


output:DICTIONARIES
{}
{'q': 12, 'p': 23, 'W': 18, 'channaveeresh': 17}
dict_keys(['q', 'p', 'W', 'channaveeresh'])
dict_values([12, 23, 18, 17])
q
p
W
channaveeresh
c
h
a
n
n
a
v
e
e
r
e
s
h
