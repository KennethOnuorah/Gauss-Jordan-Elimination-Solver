# Gauss Jordan Elimination Solver
A project that performs Gauss-Jordan elimination for 2x2 and 3x3 matrices.

## What is Gauss-Jordan elimination?
Gauss-Jordan elimination is a mathematical method of converting a regular matrix into what is called an ***identity matrix***. Basically, an identity matrix is a matrix that has a downward-sloping line containing 1's with zeroes filling the surrounding indices.

<img src="https://github.com/KennethOnuorah/Gauss-Jordan-Elimination-Solver/blob/main/src/images/img1.png" width="516" height="189"/>

The process of converting a matrix into an identity matrix involves three fundemental types of row operations:
1. Row swapping
2. Multiplying a row by a nonzero number
3. Adding a multiple of one row to another

These three steps are done repeatedly until the identity matrix has been found. The three numbers on the rightmost side of the identity matrix, as seen in the above image, are called the ***solutions*** to a system of equations. 

Solving for an identity matrix can have three outcomes:
1. **One solution**
2. **Infinite solutions**
3. **No solution**

<img src="https://github.com/KennethOnuorah/Gauss-Jordan-Elimination-Solver/blob/main/src/images/img2.png" width="516" height="189"/>

The process of attaining the identity matrix is rather long and tedious to accomplish by hand, so I made this bot that does all the work in a short amount of time.

## Languages used
* Python

## How to use
There are two python files, one for 2x2 matrices and one for 3x3 matrices. Run in the terminal by entering `python [file_name_here].py`

## Features
* Matrix setting
* Step-by-step calculations
* Captions
