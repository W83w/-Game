qwqe = int(input())
first = int(input())
second = int(input())
third = int(input())

plays = 0
machin = 0

while qwqe >= 1:
    qwqe = qwqe - 1

    if machin == 0:
        first = first + 1
        if first == 35:
            first = 0
            qwqe = qwqe + 30
    elif machin == 1:
        second = second + 1
        if second == 100:
            second = 0
            qwqe = qwqe + 60
    elif machin == 2:
        third = third + 1
        if third == 10:
            third = 0
            qwqe = qwqe + 9
plays = plays + 1
machin = machin + 1
if machin == 3:
    machin = 3
print("Марни банкрот")