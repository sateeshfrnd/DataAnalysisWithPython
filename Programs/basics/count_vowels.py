'''
Write a program named count_vowels.py that prompts the user for a string and then displays a count of each of the vowels (a, e, i, o, u) and the total number of vowels contained in that string.
Hint: Remember that vowels can also be uppercase letters.
'''

def count_vowels(str): 
    
    # Initializing count variable to 0 
    vowels_count = 0
    
    # Creating a dictionary with key as a vowel and the value as 0
    vowel_count_dict = {}.fromkeys("aeiou", 0) 
    
    # casefold has been used to ignore cases 
    str_casefold = str.casefold() 
    
    # count the vowels
    for char in str_casefold:
        if char in vowel_count_dict: 
            vowel_count_dict[char] += 1
            vowels_count += 1
            
    return vowels_count, vowel_count_dict

inputStr = input("Enter a String = ")
vowels_count, vowel_count_dict = count_vowels(inputStr)
print("Total number of vowels = ",vowels_count)
print("Count of each of the vowels = ",str(vowel_count_dict))