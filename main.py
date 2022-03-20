from functions import*


#####################
MAtime = 250
diff = 0.03
gap = 10
#####################




deals1 = []
deals2 = []
ind1 = 0
ind2 = 0
prices = []
last = 0
MAnumbers = [0 for i in range(MAtime)]
sber = []
sberp = []
sberop = open("sber20220201.txt", "r").readlines()
sberpop = open("sberp20220201.txt", "r").readlines()
for i in sberop:
    p = list(i.split(","))[3:5]
    sber.append([TimeInSec(p[0]), float(p[1])])
for i in sberpop:
    p = list(i.split(","))[3:5]
    sberp.append([TimeInSec(p[0]), float(p[1])])



for second in range(25200, 85400):
    while True:
        if sber[ind1][0] > second:
            res1 = sber[ind1 - 1][1]
            break
        elif sber[ind1][0] < second:
            ind1 += 1
        else:
            res1 = sber[ind1][1]
            break

    while True:
        if sberp[ind2][0] > second:
            res2 = sberp[ind2 - 1][1]
            break
        elif sberp[ind2][0] < second:
            ind2 += 1
        else:
            res2 = sberp[ind2][1]
            break

    prices.append([res1, res2])
    del MAnumbers[0]
    MAnumbers.append(res1 - res2)
    if MAnumbers[0] != 0:
        if second - last > gap:
            last = second
            c = Check(MAnumbers, diff, res1 - res2)
            if c == 1:
                deals1.append([second, 1, res1, res2])
            if c == 2:
                deals2.append([second, 2, res1, res2])
    IsMAH = (True, False)[MA(MAnumbers) > res1 - res2]
    if IsMAH:
        for i in range(len(deals2)):
            if len(deals2[i]) == 4:
                deals2[i].append(res1)
                deals2[i].append(res2)
                deals2[i].append(float('{:.3f}'.format(-deals2[i][2] + deals2[i][3] + deals2[i][4] - deals2[i][5])))
    else:
        for i in range(len(deals1)):
            if len(deals1[i]) == 4:
                deals1[i].append(res1)
                deals1[i].append(res2)
                deals1[i].append(float('{:.3f}'.format((deals1[i][2] - deals1[i][3] - deals1[i][4] + deals1[i][5]))))


print(*deals1)
print(*deals2)
profit = 0
for i in deals1:
    profit += i[6]
for i in deals1:
    profit += i[6]
print(f"прибыль: {'{:.3f}'.format(profit)}\nсделок:{len(deals1) + len(deals2)}")

#for i in deals1:
#    print(f"время {i[0]}\nшорт {i[2]} итог {i[4]}\nлонг {i[3]} итог {i[5]}\nпрофит {'{:.3f}'.format(i[6])}\n")
#for i in deals2:
#    print(f"время {i[0]}\nлонг {i[2]} итог {i[4]}\nшорт {i[3]} итог {i[5]}\nпрофит {'{:.3f}'.format(i[6])}\n")














