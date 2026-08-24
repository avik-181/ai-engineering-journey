print("what the fuck is your name?")
n = input()
print("How many bananas you have?")
b = float(input())
if(b>10):
    print("Lot of bananas")
elif(b>=5 and b<=10): print("Small bunch/ ")
else:
    print("Eat the bananas")

print("Cost of each banana: ")
c = float(input())
print("Hello "+n+"! You have ", b, " bananas.")
t=b*c
print("Total cost of bananas: ", t)
if(t>100):
    print("Thats expensive")
elif(t>50 and t<=100): print("Moderate")
else:print("Cheap")