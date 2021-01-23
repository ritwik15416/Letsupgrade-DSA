# Q1. 
# Insertion at beginning
class node:
    def __init__(self,data):
        self.data = data
        self.loc = None
class ll:
    def __init__(self):
        self.head=None
    def insert_at_beg(self,data):
        new_node = node(data)
        new_node.loc = self.head
        self.head = new_node
# Deletion from end
class node:
    def __init__(self,data):
        self.data = data
        self.loc = None
class ll:
    def __init__(self):
        self.head=None
    def delete_at_end(self,data):
        if self.head==None:
            print("The list has no elements")
            return
        n = self.head
        if n.loc.loc is not None:
            n = n.loc
        n.loc = None
        
#Q2.
def binary_search(arr, key): 
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high: 

		mid = (high + low) // 2

		if arr[mid] < key: 
			low = mid + 1

		elif arr[mid] > key: 
			high = mid - 1

		 
		else: 
			return mid  
	return -1


# Test array 
arr = [ 2, 4, 14, 40, 10 ] 
key = 40

# Function call 
result = binary_search(arr, key) 

if result != -1: 
	print("Element is present at index", str(result)) 
else: 
	print("Element is not present in array") 
  

#Q3.
class Node: 

	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 

	def __init__(self): 
		self.head = None

	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	def printMiddle(self): 
		slow_ptr = self.head 
		fast_ptr = self.head 

		if self.head is not None: 
			while (fast_ptr is not None and fast_ptr.next is not None): 
				fast_ptr = fast_ptr.next.next
				slow_ptr = slow_ptr.next
			print("The middle element is: ", slow_ptr.data) 
