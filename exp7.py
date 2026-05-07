thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
list1={}
list1=thisdict.copy()

print(thisdict)

print(list1)

list1.clear()
print(list1)

print(thisdict.fromkeys("model","year"))

print(thisdict.get("model"))

print(thisdict.items())

print(thisdict.keys())

thisdict.pop("year")
print(thisdict)

thisdict.update({"nick":5})
print(thisdict)

print(thisdict.values())