import datetime
import json
import yaml

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

x =  '{ "name":"John", "age":30, "city":"New York"}'