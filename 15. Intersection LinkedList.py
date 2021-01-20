class Node: 
    def __init__(self, data): 
		self.data = data 
		self.next = None

def intersect_node(head1, head2): 
	
	cur1 = head1 
	cur2 = head2 
	
	if (not cur1 or not cur2 ): 
		return -1
		
	while (cur1 and cur2 and cur1 != cur2): 
		cur1 = cur1.next
		cur2 = cur2.next
		
		if (cur1 == cur2): 
			return cur1.data 
			
		if (not cur1): 
			cur1 = head2 
		
		if (not cur2): 
			cur2 = head1 
			
	return cur1.data 


head1 = Node(10)
head2 = Node(3) 

newNode = Node(6) 
head2.next = newNode 

newNode = Node(9) 
head2.next.next = newNode 

newNode = Node(15) 
head1.next = newNode 
head2.next.next.next = newNode 

newNode = Node(30) 
head1.next.next = newNode 

head1.next.next.next = None

print(intersect_node(head1, head2)) 
