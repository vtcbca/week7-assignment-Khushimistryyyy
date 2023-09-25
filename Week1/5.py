#Write a python script to enter any string and count vowel.
print("\npython script to enter any string and count vowel.")
str=input("Enter String: ")
count_vowel=0
vowel=['a','e','i','o','u','A','E','I','O','U']
for i in str:
    if i in vowel:
        count_vowel+=1
print("Available Vowel In String Is: ",count_vowel)



 
