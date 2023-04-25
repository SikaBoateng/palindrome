def is_palindrome(input_string):
    for input in input_string:
        new_string=""
        reverse_string=""
        if input!="":
            new_string=new_string.lower()+input
            reverse_string=input+reverse_string.lower()
    if new_string==reverse_string:
        return True
    return False
print(is_palindrome("NEVER ODD OR EVEN"))
