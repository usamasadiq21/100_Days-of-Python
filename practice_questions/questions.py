# 1. How to find Averaage of N numbers in python.

# num = int(input('How many numbers ?'))
# total_sum = 0

# for n in range(num):
#     number = int(input('Enter number!!'))
#     total_sum += number

# avg = total_sum / num 

# print(avg)

# 2. How to sum the first N positive integers in python.

number = int(input('Enter Number of values, you want to enter to get Sum.!!'))
sum = 0
values_list = []
for n in range(number):
    value_to_sum = int(input('ENter values!!'))
    if value_to_sum > 0:
        values_list.append(value_to_sum)
        sum += value_to_sum
    elif value_to_sum < 0:
        number != len(values_list)
        values_list.append(value_to_sum)
        continue

    else:
        print('Enter Positive numbers only!!')

print('Sum', sum)
print(values_list)




