# casesensitivity:the difference between uppercase & lowercase .
# we can re-use the variable in python

# variables are used to store the Value
# a variable can start with alphabets(uppercase/lowercase)
# a variable can't start with numeric,but it can be in the middle and at the end
# the only special symbol which can be used is underscore __
# underscore can be at the starting , middle and at the end.
# a variable should not have a space between them

# the another name for variable 'isidentifier'
        #  a=3  # here a : variable(or)identifer
              # here = : assignment operator
              # here 3 : value

# isidentifier : the variable declared is vaild/invaild       
# print('pravalika'.isidentifier())    # true 
# print('6ty'.isidentifier())          # false
# print('_'.isidentifier())            # true
# print('a_b'.isidentifier())          # true 
# print('a b'.isidentifier())          # false
# print('a3b5'.isidentifier())         # true
# print('a6b3 '.isidentifier())        # false
# print('a6h8_'.isidentifier())        # true

            # "swapping of 2 variables"

# a=5
# b=7
# a,b=b,a 
# print(a)    #  7
# print(b)    #  5
            