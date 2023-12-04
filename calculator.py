#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Dec 4th, 2023
# This program asks the user for two numbers
# and a sign (+, -, x, /, %)
# then displays the answer of the expression


def calc_result(num1, num2, sign):
    # Return result to main
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    elif sign == "x":
        return num1 * num2
    elif sign == "/":
        return num1 / num2
    elif sign == "%":
        return num1 % num2


def main():
    # get numbers and sign from user
    user_num_1_str = input("Enter a number: ")
    user_num_2_str = input("Enter a second number: ")
    user_sign = input("Enter one of the following signs (+, -, x, /, %): ")

    # Check if input is valid
    try:
        user_num_1_float = float(user_num_1_str)
        try:
            user_num_2_float = float(user_num_2_str)

            # If user tries to divide 0
            if user_num_1_float == 0 and user_sign == "/":
                print("0/{} is undefined.".format(user_num_2_str))

            # If user enters an invalid sign
            elif (
                user_sign != "+"
                and user_sign != "-"
                and user_sign != "x"
                and user_sign != "/"
                and user_sign != "%"
            ):
                print("{} is not a valid sign.".format(user_sign))
            else:
                # Call function to find answer
                calculated_result = calc_result(
                    user_num_1_float, user_num_2_float, user_sign
                )

                # Display answer
                print(
                    "{} {} {} = {:.2f}".format(
                        user_num_1_float, user_sign, user_num_2_float, calculated_result
                    )
                )
        except:
            # num 2 is not a float
            print("{} is not a float.".format(user_num_2_str))
    except:
        # num 1 is not a float
        print("{} is not a float.".format(user_num_1_str))


if __name__ == "__main__":
    main()
