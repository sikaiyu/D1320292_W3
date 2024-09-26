decimal= int(input("請輸入一個十進制數字: "))
binary = bin(decimal)[2:]  
octal = oct(decimal)[2:]  
hexadecimal = hex(decimal)[2:].upper()
print("二進制:",binary )
print("八進制:", octal)
print("十六進制:", hexadecimal)
