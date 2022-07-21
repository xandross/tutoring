import json
import yaml
import datetime

class Person:
    def __init__(self, id: int, first_name: str, last_name: str, birth_date: datetime.date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def __repr__(self):
        return "{0},{1},{2},{3}".format(self.id, self.first_name, self.last_name, self.birth_date)

people = [Person(1,"Janos","Kovacs",datetime.date(1980,1,1)),
        Person(2,"Gabor","Varga",datetime.date(1981,3,3)),
        Person(3,"Mariann","Varga",datetime.date(2002,5,10)),
        Person(4,"Bela","Kovacs",datetime.date(1981,2,3)),
        Person(5,"Dora","Nagy",datetime.date(1985,5,10)),
        Person(6,"Zsuzsa","Kiss",datetime.date(1990,8,11)),
        Person(7,"Geza","Kiss",datetime.date(1990,6,10))]

jsonStr = json.dumps(people[0].__dict__, indent = 4, default = str)

print(jsonStr)

yamlStr = yaml.dump(people[0].__dict__)

print(yamlStr)
