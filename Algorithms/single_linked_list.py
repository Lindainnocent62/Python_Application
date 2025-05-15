"""
    Data structure that stores data in a key value pair 
    Key and a data [key: data] 
    the first node is called a Head and the last is tail
"""

class  :
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "Node data: %s "self.data
        
# Single linked list
class LinkedList:
    def __init__(self):
        self.head = None
        #self.tail = None
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.next_node
    
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def search(self, key):
        """
        Search for the first node containing data matches the key
        return the node or 'None' if not found
        """
        current = self.head
        
        while current:
            if current.data == key:
                return current
            else: 
                current = current.next_node
        return None    
                
    def insert(data, index):
        """
        Insert a new node containing at index position
        insertion takes O(1) time but finding the next node at the insertion point takes O(n) time
        """
        
        if index == 0:
            self.add(data)
        
        if index >0:
            new = Node()
            
            position = index
            current = self.head
            
            while position > 1:
                current = node.next_node
                position -=1
                
            prev_node = current
            next_node = current.next_node
    # ToDo: remove_at_index(index) node_at_index(index)
    
    def remove(self, key):
        """
        Removes node containing data that matches key 
        returns the node or None if key doesnt exist
        Takes O(n) times
        """
        current = self.head
        previous = None
        found = False
        
        while current and not found
            if current.data = key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else: 
                previous = current
                current = current.next_node
        return current
        
                
            
    def __repr__(self):
        """
        Returns a string represantation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head
        
        while current: 
            if current is self.head:
                nodes.append("[Head: %s]"% current.data)
            elif current.next_node is None:
                nodes.append("[Tail %s]"% current.data)
            else:
                nodes.append("[%s]"% current.data)
            
            current = current.next_node
        return '->'.join(nodes)
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            