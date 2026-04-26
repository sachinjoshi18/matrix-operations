import numpy as np
def inp_mat(prompt):
    print(prompt)
    rows= int(input("Enter the number of rows: "))

    cols= int(input("Enter the number of cols: "))
    print("Enter the values of matrix  row by row: ")
    matrix = []
    for i in range(rows):
        row=list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) !=cols:
            print("Error: Number of columns must match the input.")
            return None
        matrix.append(row)

    return np.array(matrix)
def operations():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multplication")
        print("4. Transpose (A)")
        print("5. Determinant (A)")
        print("6. Exit")
        choice=input("Enter your operation(1-6): ")
        if choice =="6":
            break

        mat1=inp_mat("Matrix 1: ")
        mat2=inp_mat("Matrix 2: ")
        if choice =="1":
            if mat1.shape==mat2.shape:
                print("Result: \n",mat1+mat2)
            else:
                print("Matrix must have the same size: ")

        elif choice =="2":
            if mat1.shape==mat2.shape:
                print("Result: \n",mat1-mat2)
            else:
                print("Matrix must have the same size: ")

        elif choice =="3":
            if mat1.shape[1]==mat2.shape[0]:
                print("Result: \n",np.dot(mat1,mat2))
            else:
                print(" Invalid Matrix size for  multiplication")

        elif choice =="4":
            print("Tranpose of A: \n",mat1.T)

        elif choice=="5":
            if mat1.shape[0]==mat1.shape[1]:
                print("Determinant :",np.linalg.det(mat1))
            else:
                print("Determinant for square matrix!")
        elif choice=="6":
            print("Existing...")
            break


        else:
            print("Invalid")

if __name__=="__main__":
    operations()

            
            
            

        
