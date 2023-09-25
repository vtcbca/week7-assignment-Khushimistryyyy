
#Write a python script to enter any string, replace vowel with its position number.
print("\nWrite a python script to enter any string, replace vowel with its position number.")
string_input=input(("Enter The String: "))
vowels='aeiouAEIOU'
result=''
position=1
for char in string_input:
    if char in vowels:
        result+=str(position)
        position+=1
    else:
        result+=char

print(result)
