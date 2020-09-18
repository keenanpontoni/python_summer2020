##Start with what Patrick recommended we start with.


class Node:
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next
    def __str__(self):
        return str(self.value)

##per the assignment, we want to create a LinkedList class:

class LinkedList:
##define such that it takes a number and sets it as the value at the head of list    
    def __init__(self, _value):
        self.length = 0
        self.head = _value
        
##define such that it returns the length of the list
    def length(self):
        return self.length

##define such that it takes a number and adds it to the end of the list
##used help from Alper on the first couple and was able to apply the similar structure to the remaining ones:
##in particular, my original looked something like this:
    def addNode(self, new_value):
        new_node = Node(_value = new_value)
        prior_node = self.head
        while prior_node.next != None:
            prior_node = prior_node.next
        prior_node.next = new_node
        self.length += 1
##which didn't work, and changed to this:

    def addNode(self, new_value):
        new_node = Node(_value = new_value)
        prior_node = self.head
        if self.head == None:
            self.head = new_node
        else:
            while prior_node.next != None:
                prior_node = prior_node.next
            prior_node.next = new_node
        self.length += 1


##define such that it takes a number and adds it after the after_node
    def addNodeAfter(self, new_value, after_node):
        new_node = Node(_value = new_value, _next = after_node.next)
        after_node.next = new_node
        self.length += 1

##define such that it takes a value and adds before the before_node
    def addNodeBefore(self, new_value, before_node):
        new_node = Node(_value = new_value, _next = before_node)
        prior_node = self.head
        while prior_node.next != before_node:
            prior_node = prior_node.next
        prior_node.next = new_node 
        self.length += 1          

##define such that it emoves a node from the list
    def removeNode(self, node_to_remove):
        prior_node = self.head
        while prior_node.next != node_to_remove:
            prior_node = prior_node.next
        prior_node.next = node_to_remove.next  
        self.length -= 1


##had trouble with final three.
##to test things out:


TestList = LinkedList(None)
print(TestList)

##let's add some nodes:

TestList.addNode(new_value = 3)
TestList.addNode(new_value = 10)
TestList.addNode(new_value = 15)

##and print:

print(TestList)

##and check its length:

TestList.length

##appears to have worked.
##let's try removing nodes:

TestList.removeNode(node_to_remove = 10)
TestList.removeNode(node_to_remove = 15)

##and print:

print(TestList)

##and check its length:

TestList.length





