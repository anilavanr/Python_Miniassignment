totalrows = int(input("Enter the Total Rows: "))

for rowno in range(1,totalrows+1):
    for colno in range(1,totalrows+1):
        if(colno == totalrows) or (rowno ==1) or (colno == rowno):
            print("*",end=" ")

        else:
            print(" ", end=" ")
    print()