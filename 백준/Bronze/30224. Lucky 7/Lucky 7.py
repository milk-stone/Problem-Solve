l = input()
l_int = int(l)

containss = False
for i in range(len(l)):
    if l[i] == '7':
        containss = True
        break

dividess = False
if l_int % 7 == 0:
    dividess = True

if not containss:
    if not dividess:
        print(0)
    else:
        print(1)
else:
    if not dividess:
        print(2)
    else:
        print(3)