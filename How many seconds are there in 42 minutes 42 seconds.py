def split_int_float(number):
    integer_part = int(number)
    float_part=number-integer_part
    return integer_part,float_part
number=float(input())
interger_part,float_part=split_int_float(number)

def move_decimal_right(number, positions):
    result = number * (10 ** positions)
    return result

# Example usage:
positions_to_move = 2

result = move_decimal_right(float_part, positions_to_move)
b=int(result)
a=interger_part*60
c=a+b
print("Total number of seconds:",c)
