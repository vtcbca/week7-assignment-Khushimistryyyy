

#Write a python script to enter any string and print only part of string. Take input of start character and end character from user.
print("\nWrite a python script to enter any string and print only part of string. Take input of start character and end character from user.")
string_input=input(("Enter The String: "))
first_input=input(("Enter The First Character: "))
last_input=input(("Enter The Last Character: "))

start_index=string_input.find(first_input)
end_index=string_input.find(last_input)

if start_index==-1:
    print("Start Character Is Not Found")
    exit()

if end_index==-1:
    print("End Character Is Not Found")
    exit()

if end_index<start_index:
    print("End Character Cannot be Before Start Character")
    exit()

print("Result: ",string_input[start_index:end_index+1])



      
