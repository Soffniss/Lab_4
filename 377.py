text=input()
char=input()
first=text.find(char)
last=text.rfind(char)
part1=text[:first+1]
part2=text[first+1:last].replace(char, char.upper())
part3=text[last:]
print(part1+part2+part3)