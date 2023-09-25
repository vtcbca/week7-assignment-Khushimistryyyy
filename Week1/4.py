
#Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.
print("\nprogram to check Enter the Number It Is armstrong Or Not:")
num = int(input("Enter a number: "))
sum = 0
n1 = len(str(num))
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n1
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")








    
