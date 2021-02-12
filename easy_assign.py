
'''

This file contains the functions that you need for completing this assignment. 

1. append_two_strings() --> Function to append a string2 to string1. -- 30%
2. append_character() --> Function to append a character to the end of string. -- 30% 
3. append_num_to_string() --> Function to append a number to the end of a string. -- 40%

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''

def append_two_strings(string_1, string_2):
    result = string_1 + string_2
    return result 


def append_character(string_1, char_1):
    result = string_1 + char_1
    return result 



def append_num_to_string(string_1, num_1):
    result = string_1 + str(num_1)
    return result 



if __name__ == "__main__":
    string_1 = str(input("assign string_1: "))
    string_2 = str(input("assign string_2: "))
    value = append_two_strings(string_1, string_2)
    print(value)
    
    string_1 = str(input("assign string_1: "))
    char_1 = str(input("assign char_1: "))
    if len(char_1) > 1:
        print("Error! Only 1 character allowed!")
    value_2 = append_character(string_1, char_1)
    print(value_2)

    string_1 = str(input("assign string_1: "))
    num_1 = int(input("assign num_1: "))
    value_3 = append_num_to_string(string_1, num_1)
    print(value_3)
