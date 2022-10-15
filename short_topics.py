import math
import numpy as np
import jinja2

# None, NaN, tuple unpacking (multiple assignment), String formatting

# NaN - Not a number
x = 5
y = float('nan')

# print(0/0) # signaling NaN <-> quiet NaN

print(f"művelet: {x}, {y}, {x + y}, {5 * y}")
print(f"compare: {y < y}, {y > y}, {y == y}, {y != y}")
print(f"Nan check: {y != y}, {math.isnan(y)}, {np.isnan(y)}")

z = float('-inf')
u = float('inf')
print(f"-inf check: {z == z}, {math.isnan(z)}, {math.isinf(z)}, {np.isneginf(z)}, {np.isposinf(z)}")
print(f"+inf check: {u == u}, {math.isnan(u)}, {math.isinf(u)}, {np.isneginf(u)}, {np.isposinf(u)}")

# None - null, típusa: NoneType
x = None
print(x)
print(type(x))

if x:
  print("x -> True")
elif x is False:
  print ("x -> False")
else:
  print("Egyik sem")

# tuple unpacking
t = (1, 2, 3)
i, j, k = t

# String formatting
s = f"string interpolation: {i}, {j}, {k}, {3+5}" # legújabb
print(s)
s = "új stílus, index alapján: {0}, {1}, {2}".format(i, j, k)
print(s)
s = "új stílus, index nélkül: {}, {}, {}".format(i, j, k)
print(s)
s = "régi stílus: %d %d %d, %s" % (i, j, k, "blah")
print(s)
s = "régi stílus: %(elso)d, %(masodik)s" % {"elso": i, "masodik": "blah"}
print(s)

# templating
environment = jinja2.Environment()
template = environment.from_string( # load template
'''Hello {{ name }}!
I'm happy to inform you that you did very well on today's {{ test_name }}.
You reached {{ score }} out of {{ max_score }} points.

'''
)

# data
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
]

for student in students:
    content = template.render(
        student,
        max_score=100,
        test_name=test_name
    )
    print(content)