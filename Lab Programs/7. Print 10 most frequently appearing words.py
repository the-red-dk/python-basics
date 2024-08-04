#Print 10 most occuring words 

import pprint, operator
f = open("text5.txt")
content = f.read().lower()
w = content.split()
d = {}
for i in w:
    d.setdefault(i, 0)
    d[i] += 1
pprint.pprint(d)
sort = sorted(d.items(), key = operator.itemgetter(1), reverse = True)
pprint.pprint(sort)
print("Dictionary in descending order: ")
for i in sort[:10]:
    print(i)
