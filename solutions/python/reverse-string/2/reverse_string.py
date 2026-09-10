"""Module to reverse a string"""
def reverse(text):
    """Method to reverse a string
        Input: text (string)
        Output: (string)"""
    return text[::-1]

    # """Alternative Method: First convert to list then reverse then join"""
    # string_list = text.split()
    # string_list.reverse()
    # return "".join(string_list)