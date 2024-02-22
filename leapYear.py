cases = int(input()) 

for i in range(cases): #go through the other lines
    line = int(input())

    for j in range(line):
        time = int(input())
        if time < 1582:
            print("No")

        elif time%4>0:
            print("No")

        elif time%100>0:
            print("Yes")

        elif time%400>0:
            print("No")
    

        else:
            print("Yes")