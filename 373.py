string=input()
lower_count=0
upper_count=0
for char in string:
    if char.islower():
        lower_count+=1
    elif char.isupper():
        upper_count+=1
length=len(string)
lower_perc=(lower_count/length)*100
upper_perc=(upper_count/length)*100
print(f"{lower_perc:.2f}")
print(f"{upper_perc:.2f}")