import time

#The matrix that the user currently has
#The 3rd column in the user matrix is the answer column, the other two columns are the 3x3 matrix
matrix = [[0.0, 0.0, 0.0, 0.0],
					[0.0, 0.0, 0.0, 0.0],
					[0.0, 0.0, 0.0, 0.0]]
#The identity matrix that we want after the calculations are done	
identity = [[1.0, 0.0, 0.0],
						[0.0, 1.0, 0.0],
						[0.0, 0.0, 1.0]]

cr = 0 #The current row that is being worked on
cc = 0 #The current column that is being worked on

def main():
	#Welcome the user with the program header
	print("\nx=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x")
	print("Gauss-Jordan Elimination Calculator")
	print("x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x")
	print("\t   [3x3 EDITION]\n")

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
	while(j < 3):
		k = 0
		#While the current column is not the last
		while(k < 4):
			m[j][k] = float(input("Enter the data value at [" + str(j) + "," + str(k) + "]: "))
			k += 1
		j += 1	
	#Show the user their matrix
	j = 0
	print("")
	while(j < 3):
		print("[" + str(m[j][0]) + "|" + str(m[j][1]) + "|" + str(m[j][2]) + "][" + str(m[j][3]) + "]")
		j += 1
	print("This is your matrix.\n")
	CheckMatrix(m, identity)
#Check if the array is equal to the identity matrix, has infinite or no solutions, or needs a row switched
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
	while(r < 3):
		c = 0
		while(c < 3):
			if(m[r][c] == i[r][c]):
				correct_num_of_indexes += 1
			c += 1
		r += 1
	#If the correct number of indexes equals 9
	if(correct_num_of_indexes == 9):
		time.sleep(2)
		solution_found = True;
		print("SOLUTION FOUND!")
		print("===============")
		print("X₁ ==>", round(m[0][3], 3))
		print("X₂ ==>", round(m[1][3], 3))
		print("X₃ ==>", round(m[2][3], 3), "\n")
		time.sleep(2)
		#Ask user if they would like to solve another matrix
		choice = input("Calculate another matrix? (Y/N): ")
		if(choice.lower() == "y"):
			print("")
			EnterMatrixValues(m)
	else:
		#(2.) Check if no solutions are found (Three zeroes in [2][0], [2][1], and [2][2])
		if((round(m[1][0], 3) == 0 and round(m[1][1], 3) == 0 and round(m[1][2], 3) == 0 and round(m[1][3], 3) != 0) or
				(round(m[2][0], 3) == 0 and round(m[2][1], 3) == 0 and round(m[2][2], 3) == 0 and round(m[2][3], 3) != 0)):
			no_solutions = True
			time.sleep(2)
			print("There are NO SOLUTIONS in your systems matrix.\n")
			time.sleep(2)
			#Ask user if they would like to solve another matrix
			choice = input("Would you like to calculate another matrix? (Y/N): ")
			if(choice.lower() == "y"):
				EnterMatrixValues(m)
		#(3.) Check if there are infinite solutions in row 3 (Four zeroes in [2][0], [2][1], [2][2], and [2][3])
		elif(round(m[2][0], 3) == 0 and round(m[2][1], 3) == 0 and round(m[2][2], 3) == 0 and round(m[2][3], 3) == 0):
			if(round(m[0][1], 3) == 0):
				infinite_solutions = True
				time.sleep(2)
				print("Your matrix has INFINITE SOLUTIONS.\n")
				print("X₁ ==>", str(round(m[0][3], 3)) + " + " + str(round(-m[0][2], 3)) + "t")
				print("X₂ ==>", str(round(m[1][3], 3)) + " + " + str(round(-m[1][2], 3)) + "t")
				print("X₃ ==> t")
				time.sleep(2)
				#Ask user if they would like to solve another matrix
				choice = input("Would you like to calculate another matrix? (Y/N): ")
				if(choice.lower() == "y"):
					EnterMatrixValues(m)
			else:
				time.sleep(2.5)
				MultiplyRow(m, cr, cc)
		#(4.) If there is a zero in the identity index diagonal, switch the rows
		elif(m[cr][cc] == 0):
			time.sleep(3.5)
			SwitchRows(m, cr, cc, cc)
		#If a solution has not been found yet, keep calculating
		if(not solution_found and not no_solutions and not infinite_solutions):
			DivideRow(matrix, cr, cc)

#Divide entire row by the pivot index int to get 1 in a diagonal
def DivideRow(m, c_r, c_c):
	time.sleep(2.5)
	#First divide the entire row by the pivot index number
	#Store the number to divide by into a temporary int/float called divisor
	k = 0
	divisor = m[c_r][c_c]
	while(k < len(m[0])):
		m[c_r][k] /= divisor
		k += 1
	#Print out the matrix currently
	l = 0
	while(l < len(m)):
		print("[" + str(m[l][0]) + "|" + str(m[l][1]) + "|" + str(m[l][2]) + "][" + str(m[l][3]) + "]")
		l += 1
	print("Divide row " + str(c_r + 1) + " by " + str(divisor) + ".\n")
	MultiplyRow(m, c_r, c_c)
#Multiply a row
def MultiplyRow(m, c_r, c_c):
	time.sleep(3.5)

	#Calculate the int to multiply the entire row by to cancel the other row
	canceller = 1
	cleared = 0
	row_to_add_to = 0
	r = 0
	while(r < len(m)): #While row is not the last one
		if(r != c_r): #If the row is not equal to the identity row
			canceller = 1
			row_to_add_to = r
			canceller *= -m[r][c_c] / m[c_r][c_c]
			c = 0
			while(c < len(m[0])):
				if(canceller != 0):
					m[c_r][c] *= canceller
				c += 1
			cleared += 1
			AddToRow(m, canceller, row_to_add_to, c_r, c_c, cleared)
		r += 1
#Add the multiplied to a certain other row
def AddToRow(m, canceller, rtat, c_r, c_c, clear):
	global cr, cc

	#Show Array
	l = 0
	while(l < len(m)):
		print("[" + str(m[l][0]) + "|" + str(m[l][1]) + "|" + str(m[l][2]) + "][" + str(m[l][3]) + "]")
		l += 1
	print("Multiply row " + str(c_r + 1) + " by " + str(canceller) + ".\n")

	time.sleep(3.5)

	#Add pivot row to other row
	for i in range(len(m[0])):
		#If the row,column index to add to is not a zero, then go ahead and add
		if(m[rtat][i] != 0 and canceller != 0):
			m[rtat][i] += m[c_r][i]
		#If the row,column index to add to is a zero and the current row is past the identity row
		elif(m[rtat][i] == 0 and canceller != 0 and c_c >= cc):
			m[rtat][i] += m[c_r][i]

		if(canceller != 0):
			m[c_r][i] /= canceller

	#Show Array
	l = 0
	while(l < len(m)):
		print("[" + str(m[l][0]) + "|" + str(m[l][1]) + "|" + str(m[l][2]) + "][" + str(m[l][3]) + "]")
		l += 1
	print("Add row " + str(c_r + 1) + " to row " + str(rtat + 1) + " and turn row " + str(c_r + 1) + " to normal.\n")

	if(clear == len(m) - 1):
		#Increment current row and current column
		cr += 1
		cc += 1
		CheckMatrix(m, identity)
	else:
		time.sleep(3.5)
#Sometimes, we may need to switch a row if the switched row has a 0 in its identity index
def SwitchRows(m, c_r, c_c, column_to_search_in):
	old_row = [0] * len(m[0])
	new_row = [0] * len(m[0])
	row_to_switch = 0

	for i in range(len(m)):
		if(abs(m[i][column_to_search_in]) == 1):
			for j in range(len(m[0])):
				row_to_switch = i
				old_row[j] = m[c_r][j]
				new_row[j] = m[i][j]
	
	for k in range(len(m[0])):
		#Set the old row to the new row
		m[c_r][k] = new_row[k]
		#Set the new row to the old row
		m[row_to_switch][k] = old_row[k]
	
	#Print current array
	l = 0
	while(l < len(m)):
		print("[" + str(m[l][0]) + "|" + str(m[l][1]) + "|" + str(m[l][2]) + "][" + str(m[l][3]) + "]")
		l += 1
	print("Switch rows " + str(c_r + 1) + " and " + str(row_to_switch + 1) + ".\n")

	time.sleep(2.5)
	MultiplyRow(m, c_r, c_c)

#Call the main function
main()