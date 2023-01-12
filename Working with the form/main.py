import sys
L, S =[1, 2, 3], "spam"
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=" ")
for i in range(len(L)):
    L = L[1:] + L[:1]
    print(L,end="")





#x = [1,2,3,4,5,6,7,8,9,10]
#filtered = iter(filter(lambda x: x % 2 == 0, seq))
#print(list(filtered), 'Тут отфильтровано')



from tkinter import Button, mainloop
x = Button (
    text = 'Press me',
    command = (lambda: print('Spam\n')))
x.pack()
mainloop()


L = [1,2,3,4]
res = L[0]
for x in L[1:]:
    res = res + x
print(res)



