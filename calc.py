import math
f = open('values.txt', 'r+')
lines = []
for line in f.readlines():
    lines.append(line.rstrip()) #remove those pesky new lines
f.close()
def placeCalc(code):
    lower = 0
    upper = 127
    seatID = 0
    #print(f"lower:{lower} and upper:{upper}")
    for ch in code:
        if lower == upper:
            break
        #print(ch)
        if ch == "F":
            upper = math.floor((lower+upper)/2)
        if ch == "B":
            lower = math.floor((lower+upper)/2)+1
    #print(f"lower:{lower} and upper:{upper}")
    rowLower = 0
    rowUpper = 7
    for ch in code:
        if(rowLower == rowUpper):
            break
        if ch == "L":
            rowUpper = math.floor((rowLower+rowUpper)/2)
        if ch == "R":
            rowLower = math.floor((rowLower+rowUpper)/2)+1
    #print(f"lower:{rowLower} and upper:{rowUpper}")
    seatID = upper * 8 + rowLower
    #print(seatID)
    return (seatID)
biggest = 0
ids = []
for line in lines:
    temp = placeCalc(line)
    ids.append(temp)
    if temp > biggest:
        biggest = temp
print(biggest)
ids.sort()
startingPoint = 45
for seat in ids:
    if seat == startingPoint:
        startingPoint+=1
    else:
        startingPoint+=2
        realSeat = seat - 1
        print(f"skipped {realSeat}")




