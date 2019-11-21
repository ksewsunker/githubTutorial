lastnumber = 10
for row in range(1, lastnumber):
    for column in range(1, row+1):
        print(row * column, end=' ')
    print("")
