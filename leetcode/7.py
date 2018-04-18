li = input()
if int(li) < 0:
    num = li[1:]
    print('-'+num[::-1])
else:
    print(str(int(li[::-1])))