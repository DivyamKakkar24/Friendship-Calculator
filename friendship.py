vowels='aeiouAEIOU'
score=0
print("Enter first name and then enter second name--> ")
#space b/w two names
first,second=map(str,input().split())

for i in first:
    if i in vowels:
        score+=5
    if i in 'friends':
        score+=15
    if i in second:
        score+=20
    else:
        score+=0

for j in second:
    if j in vowels:
        score+=5
    if j in 'friends':
        score+=15
    if j in first:
        score+=20
    else:
        score+=0

if score>=100:
    print("Your friendship score is: ",score)
    print("Congratulations! you both are best friends.")
elif score<100 and score>=35:
    print("Your friendship score is: ",score)
else:
    print("Your friendship score is: ",score)
    print("Just met?")
    



