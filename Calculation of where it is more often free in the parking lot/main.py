

##title = input()
##total = 0
##for char1 in title:
  ##      total = total + 1
##print(total)


yesterday = input()
today = input()
occupied = 0
for i in range(len(yesterday)):
        if yesterday[i] == 'c' and today[i] == 'c':
                occupied = occupied + 1
                print("YEs")
        if yesterday[i] == 'n' and today[i] == 'n':
                occupied = occupied + 1
                print("no")
        if yesterday[i] == 'c' and today[i] != 'c':
                occupied = occupied - 0
                print("Иногда есть место")
        if yesterday[i] == 'n' and today[i] != 'n':
                occupied = occupied - 0
                print("Редко есть место")
if occupied <= 0:
        occupied = 0

print(occupied)
