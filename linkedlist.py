class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
<<<<<<< HEAD
class linkedlist:
  def __init__(self):
    self.head=None 
    self.size=0 
=======

class linkedlist:
  def __init__(self):
    self.head=None
    self.size=0

>>>>>>> b4f2595f23c8d399ee428d27d9fff88008a0c15a
  def add(self,data):
    if self.head==None:
      self.head=Node(data)
      self.size+=1
      return

    cN=self.head
    while cN.next is not None:
      cN=cN.next

    cN.next=Node(data)
    self.size+=1

  def traverse(self):
    if self.head==None:
      print("empty")
      return

    cN=self.head
    while cN.next is not None:
      print(cN.data,end="->")
      cN=cN.next
<<<<<<< HEAD
    print(cN.data,cN.next)
  def search(self,data):
    cN=self.head
    i=0
    while cN.next is not None:
      if cN.data==data:
        print(f"data is at {i} found")
        return
      i=i+1
      cN=cN.next
      if cN.data==data:
        print(f"data is at {i} found")
        return
    print("data is not found")
  def delete(self,data):
    cN=self.head
    if self.head==None:
      return False
    if cN.data==data:
      self.head=cN.next
      self.size-=1
=======
    print(cN.data)

  def search(self,data):
    cN=self.head
    i=0

    while cN is not None:
      if cN.data==data:
        print("data found at",i)
        return
      i+=1
      cN=cN.next

    print("data not found")

  def delete(self,data):
    if self.head==None:
      return

    if self.head.data==data:
      self.head=self.head.next
      self.size-=1
      return

    cN=self.head
>>>>>>> b4f2595f23c8d399ee428d27d9fff88008a0c15a
    while cN.next is not None:
      if cN.next.data==data:
        cN.next=cN.next.next
        self.size-=1
<<<<<<< HEAD
        return True 
      cN=cN.next
    self.traverse()
  def length(self):
    print(self.size)
=======
        return
      cN=cN.next

    print("data not found")

  def length(self):
    print(self.size)

>>>>>>> b4f2595f23c8d399ee428d27d9fff88008a0c15a
  def insertatbeg(self,data):
    obj=Node(data)
    obj.next=self.head
    self.head=obj
<<<<<<< HEAD
    self.traverse()
  def deletelast(self):
    cN = self.head
    while cN.next.next is not None:
        cN = cN.next
    cN.next = None
    self.size -= 1
    self.traverse()
  def insertatposition(self,data,position):
    if self.head is None:
      return
    if position<0 and position>self.length():
      print("invalid position")
      return
    if position ==0:
      self.insertatbeg(data)
      return
    if position==self.length():
      self.add(data)
      return
    cn=self.head
    ind=0
    while cn.next.next is not None:
      if ind+1==position:
        break
      cn=cn.next
=======
    self.size+=1

  def insertatposition(self,data,position):
    if position<0 or position>self.size:
      print("invalid position")
      return

    if position==0:
      self.insertatbeg(data)
      return

    if position==self.size:
      self.add(data)
      return

    cn=self.head
    ind=0

    while ind<position-1:
      cn=cn.next
      ind+=1

>>>>>>> b4f2595f23c8d399ee428d27d9fff88008a0c15a
    obj=Node(data)
    obj.next=cn.next
    cn.next=obj
    self.size+=1
<<<<<<< HEAD
    self.traverse()
  def insertafter(self,data,targetdata):
    if self.head is None:
      return
    cn=self.head
    while cn.next.next is not None:
      if cn.data==data:
        break
      cn=cn.next
    obj=Node(targetdata)
    obj.next=cn.next
    cn.next=obj
    self.size+=1
    self.traverse()
  def deletebyvalue(self,data):
    if self.head is not None:
      return
    if self.head.next is None:
      if self.head.data==data:
        self.head=None
    cn=self.head
    while cn.next is not None:
      if cn.next.data==data:
        cn.next=cn.next.next
      cn=cn.next
=======

  def insertafter(self,data,targetdata):
    cn=self.head

    while cn is not None:
      if cn.data==data:
        obj=Node(targetdata)
        obj.next=cn.next
        cn.next=obj
        self.size+=1
        return
      cn=cn.next

    print("data not found")

  def deletelast(self):
    if self.head==None:
      return

    if self.head.next==None:
      self.head=None
      self.size-=1
      return

    cn=self.head
    while cn.next.next is not None:
      cn=cn.next

    cn.next=None
>>>>>>> b4f2595f23c8d399ee428d27d9fff88008a0c15a
    self.size-=1
    self.traverse()
  def delat(self,position):
    if self.head is None:
      return
    if position<0 and position>self.length():
      print("invalid position")
      return
    if position ==0:
      self.head=self.head.next

<<<<<<< HEAD
      return
    if position==self.length():
      self.add(data)
      return
    cn=self.head
    ind=0
    while cn.next.next is not None:
      if ind==position:
        break
      cn=cn.next
    cn.next=cn.next.next
    self.size-=1
    self.traverse()
    
ll=linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(44)
ll.add(7667)
ll.traverse()
ll.search(10)
ll.delete(10)
ll.length()
ll.insertatbeg(90)
ll.deletelast()
ll.insertatposition(100,3)
ll.insertafter(100,200)
ll.deletebyvalue(100)
ll.delat(3)
=======
  def delat(self,position):
    if self.head==None:
      return

    if position<0 or position>=self.size:
      print("invalid position")
      return

    if position==0:
      self.head=self.head.next
      self.size-=1
      return

    cn=self.head
    ind=0

    while ind<position-1:
      cn=cn.next
      ind+=1

    cn.next=cn.next.next
    self.size-=1

  def getfirst(self):
    if self.head==None:
      print("empty")
      return
    print(self.head.data)

  def getlast(self):
    if self.head==None:
      print("empty")
      return

    cn=self.head
    while cn.next is not None:
      cn=cn.next

    print(cn.data)

  def update(self,old,new):
    cn=self.head

    while cn is not None:
      if cn.data==old:
        cn.data=new
        return
      cn=cn.next

    print("data not found")

  def reverse(self):
    prev=None
    cn=self.head

    while cn is not None:
      temp=cn.next
      cn.next=prev
      prev=cn
      cn=temp

    self.head=prev

  def count(self,data):
    cn=self.head
    c=0

    while cn is not None:
      if cn.data==data:
        c+=1
      cn=cn.next

    print(c)

  def clear(self):
    self.head=None
    self.size=0


ll=linkedlist()

ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)

ll.traverse()

ll.search(30)

ll.insertatbeg(5)
ll.traverse()

ll.insertatposition(25,3)
ll.traverse()

ll.insertafter(30,35)
ll.traverse()

ll.delete(20)
ll.traverse()

ll.deletelast()
ll.traverse()

ll.delat(2)
ll.traverse()

ll.getfirst()
ll.getlast()

ll.update(30,300)
ll.traverse()

ll.count(300)

ll.reverse()
ll.traverse()

ll.length()

ll.clear()
ll.traverse()
>>>>>>> b4f2595f23c8d399ee428d27d9fff88008a0c15a
