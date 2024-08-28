#N<-Names, c_n<-contact_numbers, n<-number of names
N=[]
c_n=[]
n=int(input("Enter the number of contacts we need to save :"))
for i in range(n):
  Na=input("Name: ")
  C_N=int(input("Contact Number: "))
  N.append(Na)
  c_n.append(C_N)
print("\nName\t\t\tContact_number")
for i in range(n):
  print(N[i],"\t\t\t",c_n[i])

