#Python code to demonstrate  
# call by value 
  
  
string = "Geeks"
  
  
def test(string): 
      
    string = "GeeksforGeeks"
    print("Inside Function:", string) 
      
# Driver's code 
test(string) 
print("Outside Function:", string) 

# Python code to demonstrate 
# call by reference 


def add_more(list): 
	list.append(50) 
	print("Inside Function", list) 

# Driver's code 
mylist = [10,20,30,40] 

add_more(mylist) 
print("Outside Function:", mylist) 

a = "first"
b = "first"

# Returns the actual location 
# where the variable is stored 
print(id(a)) 

# Returns the actual location 
# where the variable is stored 
print(id(b)) 

# Returns true if both the variables 
# are stored in same location 
print(a is b) 
