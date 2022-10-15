import pandas as pd
import numpy as np

# nevesített függvény
def func(e):
    return len(e)

# anonim függvény
f = lambda a : len(a)

# list

# print("List műveletek")
l = ["a", "b", "c", "d"]
print(f"concat l+l: {l + l}")
print(f"multiply 3: {3 * l}")
k = l.copy()
k.clear()
print(k)
k = list(l)
k.append("E")
k.extend(iter(l))
print(f"append E, extend list: {k}")
print(f"index E: {k.index('E')}")
z = k.pop(0)
print(f"pop: {z}")
print(f"after pop: {k}")
k.remove('E')
print(f"remove E: {k}")
j = k.copy()
j.reverse()
print(f"reverse: {j}")
j = ["aa", "bbbb", "ccc", "d"]
j.sort(key = lambda a : len(a)) # függvény, ami alapján sortol
j.sort(key = func) # függvény, ami alapján sortol
print(f"sort: {j}")

# dict - listhez hasonlóm, csak index helyett kulcs
# dict fgv-ek: clear(), copy(), fromkeys(), get() - [], setdefault(), update()
# items(), keys(), values() - iteralashoz
# pop() - adott kulcshoz tartozó itemet szed ki, popitem() - az utolsót
# setdefault() - setdefault("szin", "piros")

parameterek = {
    "szin" : "kek",
    "minta" : "pottyos"
}
print(parameterek)
value = parameterek.setdefault("szin", "piros")
print(value)
value2 = parameterek.setdefault("meret", "kicsi")
print(value2)
print(parameterek)

parameterek.update({"szin" : "zold"}) # utananezni
print(parameterek)

# set: nem tartalmaz duplikátumokat, és nem rendezett
# set fgv-ek:
# add(), clear(), copy() - mint a list
# difference(), difference_update(), intersection(), intersection_update(), symmetric_difference(), symmetric_difference_update(), union(), update() - halmazműveletek
# isdisjoint(), issubset(), issuperset() - halmazműveletek
# discard(), remove(), pop() - kiszedések


# duplicate removal: set/map segítségével
print("# set - nem tartalmaz duplikált elemeket (mint a dict value nélkül)")
input = ["a", "b", "a", "c", "c"]
list1 = list(set(input))
print(list1)

print("# set comprehension")
list2 = list({s for s in input})
print(list1)

# hashing
print("# hash")
print(hash((1, "Janos", "Kovacs")))
print(hash((1, "Janos", "Kovacs")))
print(hash((1, "Janos", "Kovacx")))

print("# hash collision")
print(hash(1.1))
print(hash(4504.1))

print("# object duplikáció, eq-hash")
class Person:
    def __init__(self, id: int, first_name: str, last_name: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "{0},{1},{2}".format(self.id, self.first_name, self.last_name)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }

    def __hash__(self):
        return hash((self.id, self.first_name, self.last_name))

    def __eq__(self, other):
        return (self.id, self.first_name, self.last_name) == (other.id, other.first_name, other.last_name)

people = [Person(1,"Janos","Kovacs"),
        Person(2,"Gabor","Varga"),
        Person(3,"Janos","Kovacs"),
        Person(2,"Gabor","Varga"),
        Person(5,"Janos","Nagy")]

people_wo_dupl = list(set(people))
print(people_wo_dupl)

print("# tuple: van eq/hash")
names_wo_dupl = list({(s.first_name, s.last_name) for s in people})
print(names_wo_dupl)

print("# object/tuple, duplikátumok kiszűrése nem az összes field, csak kulcs (pl. field subset) alapján")
names_wo_dupl_full_obj = {(s.first_name, s.last_name):s for s in people}
print(names_wo_dupl_full_obj)
print(list(names_wo_dupl_full_obj.values()))



# Pandas duplicates
print("# pandas")
df = pd.DataFrame.from_records([p.to_dict() for p in people])
print(df)

print("# pandas: összes column figyelembe véve")
print(df.drop_duplicates())

print("# pandas: key - csak first_name")
print(df.drop_duplicates(subset=["first_name"], keep="last"))

print("# pandas: key - first_name + last_name")
print(df.drop_duplicates(subset=["first_name", "last_name"]))

print("# pandas: key - derived")
df["key"] = np.where(df["last_name"].str.match(r'N..y'), df["last_name"], "X")
print(df)
print(df.drop_duplicates(subset=["key"]))




# Iterator/Iterable
print("# Iterator: valami megszámlálható van a háttérben, amiken lehet lépkedni")
print("# Iterable: olyan object, amitől lehet iteratort kérni")

print("# A list/tuple/dict Iterable:")
t = ("elso", "masodik", "harmadik")
t_it = iter(t)
print(next(t_it))
print(next(t_it))
print(next(t_it))

print("# A for a háttérben iterál, iterable-től elkéri az iteratort, iteratoron végigmegy:")
for x in t:
  print(x)

for x in iter(t):
  print(x)

print("# Egyedi iterator (akár végtelen is lehetne):")
class IteratorExample:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

it = iter(IteratorExample())
for x in it:
  print(x)

print("# Pandas iterator:")
for index, row in df.iterrows():
  print(f"{index} : {row['first_name']} {row['last_name']}")