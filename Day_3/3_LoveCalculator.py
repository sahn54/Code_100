# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()


t_score = lower_name1.count('t') + lower_name2.count('t')
r_score = lower_name1.count('r') + lower_name2.count('r')
u_score = lower_name1.count('u') + lower_name2.count('u')
e_score = lower_name1.count('e') + lower_name2.count('e')

l_score = lower_name1.count('l') + lower_name2.count('l')
o_score = lower_name1.count('o') + lower_name2.count('o')
v_score = lower_name1.count('v') + lower_name2.count('v')
e_score2 = lower_name1.count('e') + lower_name2.count('e')

total_1 = str(t_score + r_score + u_score + e_score)
total_2 = str(l_score + o_score + v_score + e_score2)

loveScore = int(total_1 + total_2)


if loveScore >= 90 or loveScore <= 10:
    print(f"Your score is {loveScore} , you go together like coke and mentos ")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore} , you are alright together ")
else:
    print(f"Your score is {loveScore}")
