n=[]
for i in range(7):
    v=float(input("Enter expense: "))
    n.append(v)
c=0
t=0
num=0
l=0;

for i in n:
    t=t+i;
    num=num+1;
    if(i>l):
        l=i
    if i>10:
        c=c+1
avg=t/num
print(f"Total Expense: {t} Number : {num} Largest: {l} Greater than 10: {c} Average Expense {avg}")