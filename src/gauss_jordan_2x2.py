import time

#The matrix that the user currently has
#The 3rd column in the user matrix is the answer column, the other two columns are the 2x2 matrix
matrix = [[0.0, 0.0, 0.0],
					[0.0, 0.0, 0.0]]
#The identity matrix that we want after the calculations are done	
identity = [[1.0, 0.0],
						[0.0, 1.0]]

cr = 0 #The current row that is being worked on
cc = 0 #The current column that is being worked on

def main():
	#Welcome the user with the program header
	print("\n●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●")
	print("Welcome to the Gauss-Jordan Elimination Calculator!")
	print("●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●=●")
	print("[2x2 EDITION]\n")

	#Enter user matrix values
	EnterMatrixValues(matrix)

#Prompt the user to enter data values into their systems matrix
def EnterMatrixValues(m):
	#Set current row and columns to 0
	global cr, cc
	cr = 0
	cc = 0

	#Ask for the data values in each cell of the matrix
	j = 0
	#While the current row is not the last
	while(j < 2):
		k = 0
		#While the current column is not the last
		while(k < 3):
			m[j][k] = float(input("Enter the data value at [" + str(j) + "," + str(k) + "]: "))
			k += 1
		j += 1	
	#Show the user their matrix
	j = 0
	print("")
	while(j < 2):
		print("[" + str(m[j][0]) + "|" + str(m[j][1]) + "][" + str(m[j][2]) + "]")
		j += 1
	print("This is your matrix.\n")
	CheckMatrix(m, identity)
#Check if the array is equal to the identity matrix, or has infinite or no solutions
def CheckMatrix(m, i):
	#The three possible results after checking the matrix
	solution_found = False
	no_solutions = False
	infinite_solutions = False

	#(1.) Check if the user matrix is equal to the identity matrix
	r = 0 #Rows
	c = 0 #Columns
	correct_num_of_indexes = 0 #The number of indexes in the user's matrix that are correct
	#Use while loop to check # of indices that are correct
	while(r < 2):
		c = 0
		while(c < 2):
			if(m[r][c] == i[r][c]):
				correct_num_of_indexes += 1
			c += 1
		r += 1
	#If the correct number of indexes equals 4
	if(correct_num_of_indexes == 4):
		time.sleep(2)
		solution_found = True;
		print("SOLUTION FOUND!")
		print("===============")
		print("X₁==>", round(m[0][2], 3))
		print("X₂==>", round(m[1][2], 3))
		time.sleep(2)
		#Ask user if they would like to solve another matrix
		choice = input("\nWould you like to calculate another matrix? (Y/N): ")
		if(choice.lower() == "y"):
			print("")
			EnterMatrixValues(m)
	else:
		#(2.) Check if no solutions are found (Two zeroes in [1][0] and [1][1])
		if(m[1][0] == 0 and m[1][1] == 0 and m[1][2] != 0):
			no_solutions = True
			time.sleep(2)
			print("There are NO SOLUTIONS in your systems matrix.")
			time.sleep(2)
			#Ask user if they would like to solve another matrix
			choice = input("\nWould you like to calculate another matrix? (Y/N): ")
			if(choice.lower() == "y"):
				EnterMatrixValues(m)
		#(3.) Check if there are infinite solutions (Three zeroes in [1][0], [1][1], and [1][2])
		elif(m[1][0] == 0 and m[1][1] == 0 and m[1][2] == 0):
			infinite_solutions = True
			time.sleep(2)
			print("Your matrix has INFINITE SOLUTIONS.")
			time.sleep(2)
			#Ask user if they would like to solve another matrix
			choice = input("\nWould you like to calculate another matrix? (Y/N): ")
			if(choice.lower() == "y"):
				EnterMatrixValues(m)
		#If a solution has not been found yet, keep calculating
		if(not solution_found):
			DivideRow(matrix, cr, cc)

#Divide entire row by the pivot index int to get 1 in a diagonal
def DivideRow(m, c_r, c_c):
	time.sleep(2.5)
	#First divide the entire row by the pivot index number
	#Store the number to divide by into a temporary int/float called divisor
	k = 0
	divisor = m[c_r][c_c]
	while(k < 3):
		m[c_r][k] /= divisor
		k += 1
	#Print out the matrix currently
	l = 0
	while(l < 2):
		print("[" + str(m[l][0]) + "|" + str(m[l][1]) + "][" + str(m[l][2]) + "]")
		l += 1
	print("Divide row " + str(c_r + 1) + " by " + str(divisor) + ".\n")

	MultiplyRow(m, c_r, c_c)
#Multiply a row
def MultiplyRow(m, c_r, c_c):
	time.sleep(3.5)

	#Calculate the int to multiply the entire row by to cancel the other row
	canceller = 1
	row_to_add_to = 0
	r = 0
	while(r < len(m)):
		if(r != c_r):
			row_to_add_to = r
			canceller *= -m[r][c_c] / m[c_r][c_c]
			c = 0
			while(c < len(m[0])):
				m[c_r][c] *= canceller
				c += 1
			AddToRow(m, canceller, row_to_add_to, c_r, c_c)
		r += 1
#Add the multiplied to a certain other row
def AddToRow(m, canceller, rtat, c_r, c_c):
	#Show Array
	l = 0
	while(l < 2):
		print("[" + str(m[l][0]) + "|" + str(m[l][1]) + "][" + str(m[l][2]) + "]")
		l += 1
	print("Multiply row " + str(c_r + 1) + " by " + str(canceller) + ".\n")

	time.sleep(3.5)

	#Add pivot row to other row
	for i in range(len(m[0])):
		m[rtat][i] += m[c_r][i]
		m[c_r][i] /= canceller

	#Show Array
	l = 0
	while(l < 2):
		print("[" + str(m[l][0]) + "|" + str(m[l][1]) + "][" + str(m[l][2]) + "]")
		l += 1
	print("Add row " + str(c_r + 1) + " to row " + str(rtat + 1) + " and turn row " + str(c_r + 1) + " to normal.\n")

	#Increment current row and current column
	global cr
	cr += 1
	global cc
	cc += 1

	CheckMatrix(m, identity)

#Call the main function
main()