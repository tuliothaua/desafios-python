# Leitor de tabuada

//Creating the Entry
n1 = int(input("Diga um número:  "))

//Creating the Process
m0 = n1 * 0
m1 = n1 * 1
m2 = n1 * 2
m3 = n1 * 3
m4 = n1 * 4
m5 = n1 * 5
m6 = n1 * 6
m7 = n1 * 7
m8 = n1 * 8
m9 = n1 * 9
m10 = n1 * 10

//Creating the Exit
print("Aqui está a tabuada desse valor que você digitou abaixo \n")
print(" 0 - {}X0={}\n 1 - {}X1={}\n 2 - {}X2={}\n 3 - {}X3={}\n 4 - {}X4={}\n 5 - {}X5={}\n" .format(n1,m0,n1,m1,n1,m2,n1,m3,n1,m4,n1,m5), end="")
print(" 6 - {}X6={}\n 7 - {}X7={}\n 8 - {}X8={}\n 9 - {}X9={}\n 10 - {}X10={}"   .format(n1,m6,n1,m7,n1,m8,n1,m9,n1,m10))
