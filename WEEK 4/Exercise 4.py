
## 4. Programa que pide tres números y muestra el mayor


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

largest = n3

if n1 >= n2 and n2 >= n3:
    largest = n1
elif n2 >= n1 and n1 >= n3:
    largest = n2

print(largest)


