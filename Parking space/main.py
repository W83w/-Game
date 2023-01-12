
yesterday = input()
today = input()
occupied = 0
for i in range(len(yesterday)):
        if yesterday[i] == 'y' and today[i] == 'y':
                occupied = occupied + 1
                print("Место есть")
        if yesterday[i] == 'n' and today[i] == 'n':
                occupied = occupied + 0
                print("no")
        if yesterday[i] == 'y' and today[i] != 'y':
                occupied = occupied + 0
                print("Иногда есть место")
        if yesterday[i] == 'n' and today[i] != 'n':
                occupied = occupied + 0.5
                print("Редко есть место")
if occupied <= 0:
        occupied = 0

print(occupied)
