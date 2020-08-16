
def main():
	#write your code here
	number1 = input("Enter the first number: ")
	number2 = input("Enter the second number: ")

	results = 0

	if number1.isdigit() == False or number2.isdigit() == False:
		print("The numbers were invalid")
	else:
		operation = input("Choose the operation (+, -, /, *): ")

		if operation == "+":
			results = int(number1) + int(number2)
		elif operation == "-":
			results = int(number1) - int(number2)
		elif operation == "/":
			results = int(number1) / int(number2)
		elif operation == "*":
			results = int(number1) * int(number2)
		else:
			print("The operation is not valid")


	print("The answer is %d" % (results))






if __name__ == '__main__':
	main()
