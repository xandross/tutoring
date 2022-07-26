import datetime
import math

class Person:
    def __init__(self, id: int, first_name: str, last_name: str, birth_date: datetime.date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def __repr__(self):
        return "{0},{1},{2},{3}".format(self.id, self.first_name, self.last_name, self.birth_date)

def printPeople(lst: list):
    print("Emberek:")
    print("")
    print(*lst, sep='\n')

people = [Person(1,"Janos","Kovacs",datetime.date(1980,1,1)),
        Person(2,"Gabor","Varga",datetime.date(1981,3,3)),
        Person(3,"Mariann","Varga",datetime.date(2002,5,10)),
        Person(4,"Bela","Kovacs",datetime.date(1981,2,3)),
        Person(5,"Dora","Nagy",datetime.date(1985,5,10)),
        Person(6,"Zsuzsa","Kiss",datetime.date(1990,8,11)),
        Person(7,"Geza","Kiss",datetime.date(1990,6,10))]

print("1.) Mindenki minden adata")
people1 = [
    p                           # SELECT *
    for p in people             # FROM PERSON
]
print(*people1, sep='\n')

print("2.) K-val kezdődő vezetéknevű személyek nagybetűs keresztnevei")
people2 = [
    p.first_name.upper()        # SELECT UPPER(first_name) 
    for p in people             # FROM PERSON
    if p.last_name[0] == 'K'    # WHERE last_name like 'K%';
]
printPeople(people2)

print("3.) Kiss vezetéknevűek minden adata")

print("4.) Kiss Zsuzsa id-ja")

print("5.) 1990-01-01 után születettek vezeték és keresztneve space-szel elválasztva")

print("6.) Az össze embernek megfelelő 1-1 új person object, amik id-ja 10-zel nagyobb az eredetinél")

print("7.) egyedi vezetéknevek") # set comprehension

print("8.) {id -> (vezeték + keresztnév)} párok dictionary-ben") # dict comprehension (list input)
people8 = {
    p.id: p.last_name + " " + p.first_name
    for p in people
}
print(people8.items(), sep='\n')

print("9.) a 8-as eredményéből a páros id-júak value-ja") # dict comprehension (dict input)
people9 = {
    k: v
    for (k,v) in people8.items()
    if k % 2 == 0
}
print(people9.items(), sep='\n')

print("10.) Az összes keresztnév összes karaketere egymás után egy listában") # 2 for
people10 = [
    x
    for p in people
    for x in p.first_name
]
print(*people10, sep='\n')



# HF 2. kör
print("11.) 0-100 között a 7-tel osztható számok") # range
num11 = [
    p
    for p in range(0, 101)
    if p % 7 == 0
]
print(*num11, sep='\n')

print("12.) az input_num12 lista elemei az indexükkel dictben { (0->0), (1->7), (2->14) stb ...}") # zip + len + dict comp
input_num12 = [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
num12 = {
    p[0] : p[1]
    for p in zip(range(0, len(num11)), num11)
}
print(num12.items(), sep='\n')

print("13.) input_num13 nested lista flattelve, 1 listában")
input_num13 = [[[0, 1, 2], [3, 4, 5]], [[0, 1, 2], [3, 4, 5]], [[0, 1, 2], [3, 4, 5]], [[0, 1, 2], [3, 4, 5]]]
num13 = [
    x
    for l1 in input_num13
    for l2 in l1
    for x in l2
]
print(*num13, sep='\n')

print("14.) az input_num14 listából az int típusúak négyzete") # type
input_num14 = [2, 2.3, 5.6, 8, 2+5j, 1.024e3, 0xF]
num14 = [
    x**2
    for x in input_num14
    if type(x) == int
]
print(*num14, sep='\n')

print("15.) az input_num15 listából a nem complexek egészre kerekeítve") # round, type
input_num15 = [2, 2.3, 5.6, 8, 2+5j, 1.024e3, 0xF]
num15 = [
    str(round(x, 0))
    for x in input_num15
    if type(x) != complex
]
print(*num15, sep='\n')

print("16.) az input_num16 listából a (nem complexek és) 2 hatványok stringgé konvertálva") # math.log2, is_integer, str
input_num16 = [2, 2.3, 5.6, 8, 2+5j, 1.024e3, 0xF]
num16 = [
    str(x)
    for x in input_num16
    if type(x) != complex and math.log2(x).is_integer()
]
print(*num16, sep='\n')

print("17.) az input_people_17 listából a páratlan karakterszámú vezetéknevűek") # len
input_people_17 = [Person(1,"Janos","Kovacs",datetime.date(1980,1,1)),
        Person(2,"Gabor","Varga",datetime.date(1981,3,3)),
        Person(3,"Mariann","Varga",datetime.date(2002,5,10)),
        Person(4,"Bela","Kovacs",datetime.date(1981,2,3)),
        Person(5,"Dora","Nagy",datetime.date(1985,5,10)),
        Person(6,"Zsuzsa","Kiss",datetime.date(1990,8,11)),
        Person(7,"Geza","Kiss",datetime.date(1990,6,10))]
people17 = [
    p
    for p in people
    if len(p.last_name) %2 == 1
]
print(*people17, sep='\n')

print("18.) az input_people_17 listából a vezetéknevek, de minden Kiss lecserélve Kis-re") # expression if
input_people_17 = [Person(1,"Janos","Kovacs",datetime.date(1980,1,1)),
        Person(2,"Gabor","Varga",datetime.date(1981,3,3)),
        Person(3,"Mariann","Varga",datetime.date(2002,5,10)),
        Person(4,"Bela","Kovacs",datetime.date(1981,2,3)),
        Person(5,"Dora","Nagy",datetime.date(1985,5,10)),
        Person(6,"Zsuzsa","Kiss",datetime.date(1990,8,11)),
        Person(7,"Geza","Kiss",datetime.date(1990,6,10))]
people18 = [
    p.last_name if p.last_name != 'Kiss' else 'Kis'
    for p in input_people_17
]
print(*people18, sep='\n')

print("19.) az alábbi szövegből a számok") # split, isnumeric
input_text_19 = """
Öt évvel ezelőtt, a Covid előtti – nemcsak fesztiváli értelemben vett – békeidőkben 89900 forint volt a normál árú Sziget-bérlet, 
vagyis öt év alatt nagyjából 45 százalék volt a drágulás. Az utolsó, 2019-ben tartott fesztivál 110 ezréhez képest csaknem 
20 százalékkal nőtt az egész hétre érvényes bérlet ára. Ami abból kiindulva igazából nem is sok, hogy az éves infláció 11 százalék közelében van.
"""
nums19 = [
    x
    for x in input_text_19.split()
    if x.isnumeric()
]
print(*nums19, sep='\n')

print("20.) az előző szöveg mondatainak a karakterszáma") # split, isnumeric
input_text_20 = """
Öt évvel ezelőtt, a Covid előtti – nemcsak fesztiváli értelemben vett – békeidőkben 89900 forint volt a normál árú Sziget-bérlet, 
vagyis öt év alatt nagyjából 45 százalék volt a drágulás. Az utolsó, 2019-ben tartott fesztivál 110 ezréhez képest csaknem 
20 százalékkal nőtt az egész hétre érvényes bérlet ára. Ami abból kiindulva igazából nem is sok, hogy az éves infláció 11 százalék közelében van.
"""
nums20 = [
    len(x)
    for x in input_text_20.split(". ")
]
print(*nums20, sep='\n')