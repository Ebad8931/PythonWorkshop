# Solution to Problem on https://www.101computing.net/is-my-credit-card-valid/
# Level - Intermediate


# credit card argument is of type string and convert_to_list converts it to a list of 16 elements
def convert_to_list(credit_card_number):
    return [int(i) for i in credit_card_number if i != ' ']


# luhn_double_digit(digit) performs doubling as per luhn algorithm on a single digit
def luhn_double_digit(digit):
    digit = digit*2
    if digit > 9:
        list_of_2_digits = list(map(int, str(digit)))
        digit = sum(list_of_2_digits)
    return digit


# luhn_double(digit_list) performs doubling as per luhn algorithm on a the credit card digits list
def luhn_double(digits_list):
    for i in range(0, 16, 2):
        digits_list[i] = luhn_double_digit(digits_list[i])
    return digits_list


# check_credit_card(check_sum) returns true or false depending on whether the checksum end with 0 or not
def check_credit_card(checksum):
    if checksum % 10 == 0:
        return True
    else:
        return False


# is_my_credit_card_valid(credit_card) is the parent function to check if given credit card is valid or invalid
def is_my_credit_card_valid(credit_card):
    result = convert_to_list(credit_card)
    result = luhn_double(result)
    result = sum(result)
    result = check_credit_card(result)
    return result


# Test cases for validity of Given credit cards
card_1 = '4137 8947 1175 5904'
card_2 = '6499 8024 5027 3568'
card_3 = '8504 1721 9127 3888'
card_4 = '0043 6687 8348 5480'


print(is_my_credit_card_valid(card_1))
print(is_my_credit_card_valid(card_2))
print(is_my_credit_card_valid(card_3))
print(is_my_credit_card_valid(card_4))
