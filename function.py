#Write a function that takes an array of numbers as input and returns the sum of all the numbers
def sum_of_numbers(arr):
    print(arr)

#Write a function that takes two numbers as input and returns true if their sum is greater than 100,
#And false otherwise
 def take_in (num1,num2):
    return(num1+num2)>100
    result=take_in(30,20)

#Write a function that takes a string as input and returns the number of vowels in the string
    def vowel(string):
        vowel="aeiouAEIOU"
        count=0
        for element in string:
            if element in vowel:
                count+=1
                return count
                result=vowel("hello world")
                print(result)
