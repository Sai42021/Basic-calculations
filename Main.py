#Given three numbers from user input, decrement the first number by 1 and increment the third
#number by 2, Then do the magic calculations as follows: get the sum of the first two numbers,
#deduct the third number from the second and get the product of the first and third number, then sum
#up the results of the three magic calculations and finally divide you outcome by 3.
#Sample run 1:
#Enter three numbers separated by spaces: 4 2 3
#Output: Result of Magic calculations = 5
#Sample run 2:
#Enter three numbers separated by spaces: 2 8 5
#Output: Result of Magic calculations = 5
from pip._vendor.distlib.compat import raw_input
import math
ThreeNums = raw_input("Enter three numbers separated by spaces: ")
num1, num2, num3 = (ThreeNums.split(" "))
#Converting the three numbers from strings to integers>>>
int_num1 = int(num1)
int_num2 = int(num2)
int_num3 = int(num3)
decrement_Num1 = int_num1 - 1
increment_Num3 = int_num3 + 2
Sum_Of_first_TwoNums = decrement_Num1 + int_num2
deduct_thirdNum_FromSecond = int_num2 - increment_Num3
Product_of_first_and3rd = decrement_Num1 * increment_Num3
Result_of_Magic_calculations = (Sum_Of_first_TwoNums + deduct_thirdNum_FromSecond + Product_of_first_and3rd) / 3
#Use math.trunc(Result_of_Magic_calculations) to truncate shiznet after decimal point but import math first>
print("Result of Magic calculations = ", math.trunc(Result_of_Magic_calculations))
