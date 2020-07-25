


#mynestedlist = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#mynestedlist = [['Harsh', 20], ['Beria', 20], ['Varum', 19], ['Kakunami', 19], ['Vikas',21]]
mynestedlist = [['Rachel', -50], ['Mawer', -50], ['Sheen', -50], ['Shaheen', 51]]
for i in range(0,len(mynestedlist)):
    for j in range(i, len(mynestedlist)):
        if mynestedlist[i][1] > mynestedlist[j][1]:
            temp = mynestedlist[j]
            mynestedlist[j] = mynestedlist[i]
            mynestedlist[i] = temp
print(mynestedlist)
for i in range(0,len(mynestedlist)-1):
    if mynestedlist[i][1] <= 0:
        mynestedlist.pop(i)
print(mynestedlist)
nameholder = []
startval = 0
if len(mynestedlist) != 1:
    for i in range (0,len(mynestedlist)):
        if mynestedlist[i][1] == mynestedlist[i+1][1]:
            startval += 1
        else:
            break
    print('Start Val {}'.format(startval))
    nameholder.append(mynestedlist[startval+1][0])
    for i in range(startval+1,len(mynestedlist)):
        if mynestedlist[i][1] == mynestedlist[i+1][1]:
            nameholder.append(mynestedlist[i+1][0])
        else:
            break
    nameholder = sorted(nameholder)
    for i in range(len(nameholder)):
        print(nameholder[i])
else:
    print(mynestedlist[0][0])

    #     mynestedlist = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     mynestedlist.append([name,score])
    # for i in range(0,len(mynestedlist)):
    #     for j in range(i, len(mynestedlist)):
    #         if mynestedlist[i][1] > mynestedlist[j][1]:
    #             temp = mynestedlist[j]
    #             mynestedlist[j] = mynestedlist[i]
    #             mynestedlist[i] = temp
    # nameholder = []
    # startval = 0
    # for i in range (0,5):
    #     if mynestedlist[i][1] == mynestedlist[i+1][1]:
    #         startval += 1
    #     else:
    #         break
    # nameholder.append(mynestedlist[startval+1][0])
    # for i in range(startval+1,len(mynestedlist)):
    #     if mynestedlist[i][1] == mynestedlist[i+1][1]:
    #         nameholder.append(mynestedlist[i+1][0])
    #     else:
    #         break
    # nameholder = sorted(nameholder)
    # for i in range(len(nameholder)):
    #     print(nameholder[i])
