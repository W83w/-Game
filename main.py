print('apple')
apple_total = int(input())
apple_total2 = int(input())
apple_total3 = int(input())
apple_totalresultat = (apple_total3 * 3) + (apple_total2 * 2 ) + apple_total
print('banano')
banana_total = int(input())
banana_total2 = int(input())
banana_total3 = int(input())
banana_totalresultat = (banana_total3 * 3) + (banana_total2 * 2) + banana_total

if apple_totalresultat > banana_totalresultat:
    print('A')
if banana_totalresultat > apple_totalresultat:
    print('B')
elif banana_totalresultat == apple_totalresultat:
    print('A == b 2 x')
else:
    print('A = B ez game')
