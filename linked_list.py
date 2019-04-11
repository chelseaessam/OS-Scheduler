class Node:
 def __init__(self,name,burst_time,arrival_time):
  self.name= name
  self.burst_time=burst_time
  self.arrival_time=arrival_time
  self.next = None
 def getname(self):
  return self.name
 def getbursttime(self):
  return self.burst_time
 def getarrivaltime(self):
  return self.arrival_time
 def getNext(self):
  return self.next 
 def setname(self,name):
  self.name = name
 def setbursttime(self,time):
  self.burst_time=time
 def setarrivaltime(self,time):
  self.arrival_time=time
 def setNext(self,node):
  self.next=node
    

##class Node2:
## def __init__(self,name,burst_time):
##  self.name= name
##  self.burst_time=burst_time
##  self.next = None
## def getname(self):
##  return self.name
## def getbursttime(self):
##     return self.burst_time
## def getNext(self):
##  return self.next 
## def setname(self,name):
##  self.name = name
## def setbursttime(self,time):
##  self.burst_time=time
## def setNext(self,node):
##  self.next=node

class Node3:
 def __init__(self,name,burst_time,arrival_time,priority):
  self.name= name
  self.burst_time=burst_time
  self.arrival_time=arrival_time
  self.priority=priority
  self.next = None
 def getname(self):
  return self.name
 def getbursttime(self):
  return self.burst_time
 def getarrivaltime(self):
  return self.arrival_time
 def getNext(self):
  return self.next 
 def setname(self,name):
  self.name = name
 def setbursttime(self,time):
  self.burst_time=time
 def setarrivaltime(self,time):
  self.arrival_time=time
 def setpriority(self,priority):
  self.priority=priority
 def getpriority(self):
  return self.priority
 def setNext(self,node):
  self.next=node 


 



  #################linked list#############################
class LinkedList:
 def __init__(self):
  self.head = None
  self.tail=None
  
 def isEmpty(self):
  """Check if the list is empty"""
  return self.head is None

 def add(self,name,burst_time,arrival_time):  #add at the beginnig
  """Add the item to the list"""
  new_node = Node(name,burst_time,arrival_time)
  new_node.setNext(self.head)
  self.head = new_node
 
  
 def swap_head_and_tail(self): #checked
  if(self.size()==1):
   return 
  else:
   temp1=self.head
   self.head=self.head.getNext()
   name=temp1.getname()
   burst_time=temp1.getbursttime()
   arrival_time=temp1.getarrivaltime()
   new_node=Node(name,burst_time,arrival_time)
   
   self.tail.setNext(new_node)
   self.tail=new_node
  
    
     
  
 def size(self):#checked
  """Return the length/size of the list"""
  count = 0
  current = self.head
  while current is not None:
   count += 1
   current = current.getNext()
  return count

 
 def remove(self, name):
  """Remove item from list. If item is not found in list, raise ValueError"""
  current = self.head
  previous = None
  found = False
  while current is not None and not found:
   if current.getname() is name:
    found = True
   else:
    previous = current
    current = current.getNext()
  if found:
    if previous is None:
     self.head = current.getNext()
    else:
     previous.setNext(current.getNext())
  else:
    #raise ValueError
    print ('Value not found.')
    
 
 def index(self, name):
  """
  Return the index where item is found.
  If item is not found, return None.
  """
  current = self.head
  pos = 0
  found = False
  while current is not None and not found:
   if current.getname() is name:
    found = True
   else:
    current = current.getNext()
    pos += 1
   if found:
    pass
   else:
    pos = None
  return pos

 
 
 def append(self,name,burst_time,arrival_time):#checked
  """Append item to the end of the list"""
  current = self.head
  previous = None
  pos = 0
  length = self.size()
  while pos < length:
   previous = current
   current = current.getNext()
   pos += 1
  new_node = Node(name,burst_time,arrival_time)
  if self.head is None:
   new_node.setNext(current)
   self.head = new_node
   self.tail=new_node
  else:
   previous.setNext(new_node)
   self.tail=new_node
   
 def append2(self,name,burst_time):#checked
  """Append item to the end of the list"""
  current = self.head
  previous = None
  pos = 0
  length = self.size()
  while pos < length:
   previous = current
   current = current.getNext()
   pos += 1
  new_node = Node2(name,burst_time)
  if self.head is None:
   new_node.setNext(current)
   self.head = new_node
   self.tail=current
  else:
   previous.setNext(new_node)
   self.tail=new_node

 def append3(self,name,burst_time,arrival_time,priority):#checked
  """Append item to the end of the list"""
  current = self.head
  previous = None
  pos = 0
  length = self.size()
  while pos < length:
   previous = current
   current = current.getNext()
   pos += 1
  new_node = Node3(name,burst_time,arrival_time,priority)
  if self.head is None:
   new_node.setNext(current)
   self.head = new_node
   self.tail=current
  else:
   previous.setNext(new_node)
   self.tail=new_node



   
 def printList(self):
  """Print the list"""
  current = self.head

  while current is not None:
   print (current.getname())
   print (current.getbursttime())
   print (current.getarrivaltime())
   current = current.getNext()
   
 def printList2(self):
  current = self.head
  while current is not None:
   print (current.getname())
   print (current.getbursttime())
   print(current.getarrivaltime())
   print(current.getpriority())
   current = current.getNext()
 def getHead(self):
   return self.head
 def bubble_sort(self):
  current=self.head
  i=0
  
  if(self.size()==1 or current is None):
   return 
  while i<self.size():
     this=current.getNext()
     before=current
     while this is not None:
         if(this.getbursttime()<before.getbursttime()):
          temp_name=this.getname()
          temp_bursttime=this.getbursttime()
          temp_arrivaltime=this.getarrivaltime()
          
          this.setname(before.getname())
          this.setbursttime(before.getbursttime())
          this.setarrivaltime(before.getarrivaltime())
          
          before.setname(temp_name)
          before.setbursttime(temp_bursttime)
          before.setarrivaltime(temp_arrivaltime)
         before=this
         this=this.getNext()
     i=i+1


 def bubble_sort_p(self):
  current=self.head
  i=0
  
  if(self.size()==0 or current is None):
   return 
  while i<self.size():
     this=current.getNext()
     before=current
     while this is not None:
         if(this.getpriority()<before.getpriority()):
          temp_name=this.getname()
          temp_bursttime=this.getbursttime()
          temp_arrivaltime=this.getarrivaltime()
          temp_pr=this.getpriority()
          
          this.setname(before.getname())
          this.setbursttime(before.getbursttime())
          this.setarrivaltime(before.getarrivaltime())
          this.setpriority(before.getpriority())
          
          before.setname(temp_name)
          before.setbursttime(temp_bursttime)
          before.setarrivaltime(temp_arrivaltime)
          before.setpriority(temp_pr)
         before=this
         this=this.getNext()
     i=i+1
 def search(self,name):
  """Search for item in list. If found, return True. If not found, return False"""
  current = self.head
  found = 0
  while current is not None and not found:
    if current.getname() is name:
     found = 1
     return current
    else:
     current = current.getNext()
  
  return found



 def bubble_sort_time(self):
  current=self.head
  i=0
  if(self.size()==1 or current is None):
   return 
  while i<self.size():
     this=current.getNext()
     before=current
     while this is not None:
         if(this.getarrivaltime()<before.getarrivaltime()):
          temp_name=this.getname()
          temp_bursttime=this.getbursttime()
          temp_arrivaltime=this.getarrivaltime()
          
          this.setname(before.getname())
          this.setbursttime(before.getbursttime())
          this.setarrivaltime(before.getarrivaltime())
          
          before.setname(temp_name)
          before.setbursttime(temp_bursttime)
          before.setarrivaltime(temp_arrivaltime)
         before=this
         this=this.getNext()
     i=i+1
 def bubble_sort_time2(self):
  current=self.head
  i=0
  
  if(self.size()==1 or current is None):
   return 
  while i<self.size():
     this=current.getNext()
     before=current
     while this is not None:
         if(this.getarrivaltime()<before.getarrivaltime()):
          temp_name=this.getname()
          temp_bursttime=this.getbursttime()
          temp_arrivaltime=this.getarrivaltime()
          temp_priority=this.getpriority()
          
          this.setname(before.getname())
          this.setbursttime(before.getbursttime())
          this.setarrivaltime(before.getarrivaltime())
          this.setpriority(before.getpriority())
          
          before.setname(temp_name)
          before.setbursttime(temp_bursttime)
          before.setarrivaltime(temp_arrivaltime)
          before.setpriority(temp_priority)
         before=this
         this=this.getNext()
     i=i+1



 
##
##ls=LinkedList()
##ls.append("p1",2,0)
####ls.bubble_sort()
####ls.printList()
####ls.printList()
####ls2=LinkedList()
##ls.append("p2",2,1)
##ls.append("p3",3,3)
####ls.swap_head_and_tail()
##ls.bubble_sort()
##ls.printList()
####print(ls.search("p2"))




