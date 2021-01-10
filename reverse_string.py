def reverse_string(input):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that is the reverse of input
    """
    
    # TODO: Write your recursive string reverser solution here
        # (Recursion) Termination condition / Base condition
    if len(input) == 0:
        return ""
    else:
        first_char = input[0]
        the_rest = slice(1, None)
        
        print(the_rest)
        sub_string = input[the_rest]  # convert the `slice` object into a list
        
        # Recursive call
        reversed_substring = reverse_string(sub_string)
        
        return reversed_substring + first_char

print(reverse_string("abc"))