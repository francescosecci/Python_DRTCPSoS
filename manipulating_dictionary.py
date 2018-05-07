dict1 = dict(one=1, two=2, three=3)

dict2 = {"one": 1, "two": 2, "three": 3}

dict3 = dict({"two": 2, "three": 3, "one": 1})

print dict1 == dict2 == dict3

print "\n\n"





print dict3["two"]

#print dict2["two"]

#print dict1["two"]
print "\n\n"

#--------ottenere valore con get della chiave

print dict3.get("three")

#--------appendere un nuovo elemento al dict

dict3["four"] = 4

#--------dimostrazione
print dict3

#--------rimuovere elemento 
print dict3.pop("three")

#--------prova
print dict3

#rimuovere un elemento arbitrario (primo lista)
print dict3.popitem()
print dict3.popitem()

del dict3["one"]

print dict3

dict2.clear()
print dict2

print dict1.items()

print dict1.keys()

for item in dict1.items():
	print item