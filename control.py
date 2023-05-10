# Write a Python program that takes a list of numbers as input and outputs the median of the numbers.

numbers = [4,5,6,7]
numbers.sort()
length = len(numbers)
if length % 2 == 0:
    median = (numbers[(length)//2] + numbers[(length)//2-1])/2
else:
    median = numbers[(length-1)//2]
print(median)

# Write a Python program that takes a list of numbers as input and outputs the second largest number
# in the list using conditional statements and a for loop.
ls1 = [56,8,90,43,23,1]
new_list = set(ls1)
new_list.remove(max(new_list))
print(max(new_list))



# Write a Python program that takes a year as input and determines if it is a leap year.
year = 2000

if(year %4 == 0) and (year % 100 == 0):

    print("{year} is a leap year")

elif(year % 4 == 0) and (year %100 != 0):
    print("{year} is a leap year")
else:

 print("{year} is not a leap year")

#  Write a Python program that takes a string as input and checks if it is a palindrome 
#  (reads the same forwards and backwards), ignoring spaces and punctuation.
def isPalindrome(str):
   return str == str[::-1]
str = "mum"
res = isPalindrome(str)

if res:
   print("yes")
else:
   print("no")
# Write a Python program that takes a list of strings as input and outputs the number of times 
# each string appears in the list, using a dictionary and conditional statements.  
   
   
def countFrequency(my_list):
   list1 = {}
   for item in my_list:
      if(item in list1):
         list1[item] +=1
      else:
         list1[item]=1
my_list = ["apple","tomatoes","apple","mangoes"]  
countFrequency(my_list)       
  


