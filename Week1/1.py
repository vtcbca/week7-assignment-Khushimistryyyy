#Write a python script to enter any number and check its prime or not.
print("Program to check number is prime or not)")
n=int(input("Enter the Number: "))
if n > 1:
	for i in range(2, int(n/2)+1):
		if (n % i) == 0:
			print(n, "is not a prime number")
		break
	else:
		print(n, "is a prime number")
else:
	print(n, "is not a prime number")



