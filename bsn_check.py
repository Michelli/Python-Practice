# Checks whether the input is a valid Dutch social security number

def validate_user_input():
    input_number = "burgerservicenummer"

    while input_number.isdigit() == False and len(input_number) != 9:
        check_input = input("Enter a BSN: ")

        if check_input.isdigit() == False:
            print("That's not a BSN.\n")
        elif len(check_input) != 9:
            print("A BSN consists of 9 digits.\n")
        else:
            input_number = check_input

    return input_number

def elfproef(bsn):
    # Works by calculated a weighted average that is divisable by 11

    running_count = 0

    for index,digit in enumerate(bsn):
        # First digit is multiplied by 9, second by 8, etc.
        multiplier = 9 - index
        
        if index != 8:
            calc = int(digit) * multiplier
            running_count += calc
        
        # Control number, so multiply by -1
        else:
            calc = int(digit) * -1
            running_count += calc

    return running_count % 11 == 0 and running_count != 0

print(elfproef(validate_user_input()))