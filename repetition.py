"""
while condition:
    # code to be executed

example:

i = 0
while i < 5:
    print(i)

"""

i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)
   

"""
for condition:
    # code to be executed

example:
for i in range(5):
    print(i)


"""

list = [1, 2, 3, 4, 5]

for i in list:
    print(i)


for i in range(100):
    print('test', i)