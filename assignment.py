# # multiplication table
# def print_multiplication_table():
#     for i in range (2, 13):
#         print(f"multiplicat ion table of {i}:")
#         for j in range(1, 11):
#             print(f"{i} x {j} = {i * j}")
#         print()
# print_multiplication_table()


# def print_calender_range():
#     year = int(input("enter the year: "))
#     start_month_input = ("enter the starting month (name or number)" )
#     end_month_input = ("enter the ending month (name or number): ")
    
# # convert end month input to integer if its a number

# if start_month = input.isdigit():
#     start_month = int(start_month_input)
# else:
#     start_month = list(calender.month_name).index(start_month_input.capitalize())
    
# # convert end month input to integer if its a number

# if end_month_input.isdigit():
#     end_month = int(end_month_input)
# esle:
#     end_month = list(calender.month_name).index(end_month_input.capitalize())
    
# # print the calender for each month in the range

# print(f"\nthe calender from {calender.month_name{start_month}} to {calender.month_name{end_month}}")
# for month in range(start_month, end_month + 1):
#     print("\n", calender.month_name[month], year)
#     print(calender.monthcalender(year, month))
    
# print_calender_range()
    
#    eg 1 
# for i in range(4):
#     for j in range(4 - i):
#          print("#", end=" ")
#     print()
    
# for i in range(4):
#     for j in range(i + 1):
#         print("#", end=" ")
#     print()

# for i in range(5):
#     for j in range(i + 1):
#         print("#", end=" ")
#     print()
    
    # creating shapes
# for i in range(7):
#     for j in range(6 - 1):
#         print("  ", end="")
#     for j in range(i + 1):
#         print(" * ", end="")
#     print()

# Inverted right triangle

# n = 9
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print("  ", end="")
#     for k in range (i):
#         print(" # ", end="")
#     print()

# paschals right triangle

def right_aligned_triangle(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print("  ", end="")
        for k in range(i):
            print(" * ", end="")
            print()







