class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None # الإضافة الجديدة هون

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node # النود القديم صار يرجع للجديد
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        new_node.prev = current # النود الجديد صار يرجع للي كان أخير


    def remove_val(self, val):
        if self.head is None:
            return "List is empty"

        current = self.head
        
        # البحث عن النود المطلوب
        while current:
            if current.data == val:
                # إذا كان النود هو الـ Head
                if current == self.head:
                    self.head = current.next
                    if self.head: # لو لسه في نودات بعده
                        self.head.prev = None
                    return val
                
                # إذا كان في المنتصف أو الأخير
                if current.next: # لو مش الأخير
                    current.next.prev = current.prev
                
                if current.prev: # لو مش الأول (وهي الحالة الطبيعية هون)
                    current.prev.next = current.next
                
                return val
            current = current.next
        
        return "Value not found"
    
    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0

        # الوصول للنود الموجود حالياً في هذا الموقع
        while current and count < index:
            current = current.next
            count += 1

        # إذا وصلنا لنهاية القائمة، نستخدم الإضافة في الآخر
        if current is None:
            self.insert_at_end(data)
            return

        # عملية الربط الرباعية (بين نودين)
        new_node.next = current
        new_node.prev = current.prev

        if current.prev:
            current.prev.next = new_node
        
        current.prev = new_node

    def insert_before_value(self, target_val, data):
        if not self.head:
            return "List is empty"

        current = self.head
        while current:
            if current.data == target_val:
                # إذا كان هو الـ Head، نستخدم دالة الإضافة في البداية
                if current == self.head:
                    self.insert_at_beginning(data)
                    return
                
                new_node = Node(data)
                # الربط الرباعي
                new_node.next = current
                new_node.prev = current.prev
                
                current.prev.next = new_node
                current.prev = new_node
                return
            current = current.next
        return "Value not found"