# 1) Calculate the sum of all the elements in the list
Kanika=[4,8,1,9,6]
sum = 0
for element in Kanika:
    sum += element
print("sum:",sum)

# 2) Find the smallest number
smallest= min(Kanika)
print("smallest:" ,smallest)

# 3) Find the largest number
largest=max(Kanika)
print("Largest:",largest)

# 4) Display list in ascending order
ace=sorted(Kanika)
print("ascending:",ace)

# 5) Display list in descending order
dec=sorted(Kanika,reverse=True)
print("descending:",dec)

# 6) Convert list into tuple
t=tuple(Kanika)
print("list into tuple:",t)

# 7) Delete the list
# del Kanika
# print(Kanika)