from random import randint, choice

key_name = {}
names = []
keys = []
key_swap = {}
choosing = 0

with open("names.txt", 'r') as f:
    for line in f:
        names.extend(line.split(','))
    names = tuple(names)

with open("keys.txt", 'w') as f2:
    for i in range(len(names)):
        f2.write(str(randint(69000,70000)))
        if i < len(names) - 1:
            f2.write(',')

with open("keys.txt", 'r') as f3:
    for line in f3:
        keys.extend(line.split(','))

for i in range(len(names)):
    key_name[keys[i]] = names[i]

with open("keys to names.txt", 'w') as f4:
    f4.write(str(key_name))


recipient = keys.copy()

for i in range(len(keys)):
    choosing = choice(recipient)
    if choosing != keys[i]:
        key_swap[keys[i]] = choosing
        recipient.remove(key_swap[keys[i]])
    else:
        while choosing == keys[i]:
            choosing = choice(recipient)
        key_swap[keys[i]] = choosing
        recipient.remove(key_swap[keys[i]])

with open("keys to keys.txt", 'w') as f5:
    f5.write(str(key_swap))

#user = str(input("What is the number that was given to you by Tashfin?"))
#print("Hello " + key_name[user] + ", you are the Secret Santa for "
 #     + key_name[key_swap[user]])
