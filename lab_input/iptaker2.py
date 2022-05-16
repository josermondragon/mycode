#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address:")
    
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)

    # challenge 01
    vendor = input("Please input the vendor name: ")
    print("The name of your vendor is: ", vendor)

main()

