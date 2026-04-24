# from flask import Flask , render_template

# app = Flask(__name__)

# app.route("/play")
# def play():
#     return render_template("index.html")


# if __name__ == "__main__":
#     app.run(debug=True)

# class Node():
#     def __init__(self , key = -1 , value = -1 , next =None):
#         self.key = key 
#         self.value = value
#         self.next = next

# class MyHashMap:
#     def __init__(self):
#         """Initialize Hash data structure here"""
#         self.size =1000
#         self.hash_table = [ Node() for i in range(self.size)]
        
#     def my_hash(self , key):
#         return key % self.size

#     def put(self, key: int, value: int) -> None:
#         index = self.my_hash(key)
#         current = self.hash_table[index]
#         while current.next:
#             if current.next.key == key:
#                 current.next.value = value
#                 return 
#             current = current.next
#         current.next = Node(key , value)

        
#     def get(self, key: int) -> int:
#         index = self.my_hash(key)
#         current = self.hash_table[index].next
#         while current:
#             if current.key == key:
#                 return current.value
#             current = current.next
#         return -1


#     def remove(self, key: int) -> None:
#         index = self.my_hash(key)
#         current = self.hash_table[index]
#         while current and current.next:
#             if current.next.key == key:
#                 current.next = current.next.next
#                 return
#             current =current.next





class MyHashMap:
    """
    A custom implementation of a HashMap without using built-in dictionary libraries.
    It uses a Hash Table with Chaining (lists of [key, value] pairs) to handle collisions.
    """

    def __init__(self):
        """
        Initialize the data structure.
        - self.size: The number of buckets (1000).
        - self.hash_table: A list of size 1000, initially filled with None.
        """
        self.size = 1000
        self.hash_table = [None] * self.size
        
    def my_hash(self, key: int) -> int:
        """
        Hash function to determine the bucket index for a given key.
        The formula is: key modulo self.size.
        """
        return key % self.size

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates a (key, value) pair.
        1. Calculate the bucket index using the hash function.
        2. If the bucket is empty (None), create a new list with the pair.
        3. If the bucket has data, iterate through it to see if the key exists.
        4. If the key is found, update its value and exit (return).
        5. If the loop finishes and the key isn't found, append the new pair.
        """
        hash_value = self.my_hash(key)
        values = self.hash_table[hash_value]
        
        # Case 1: Bucket is completely empty
        if values is None:
            self.hash_table[hash_value] = [[key, value]]
            return
        
        # Case 2: Bucket has items, check for an existing key to update
        for pairs in values:
            if pairs[0] == key:
                pairs[1] = value  # Update existing value
                return  # Exit to prevent adding a duplicate below
        
        # Case 3: Key does not exist in the bucket, add it as a new entry
        self.hash_table[hash_value].append([key, value])
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if not found.
        1. Go to the correct bucket index.
        2. Iterate through the pairs in that bucket.
        3. If pair[0] matches the key, return the value in pair[1].
        """
        hash_value = self.my_hash(key)
        values = self.hash_table[hash_value]
        
        # If the bucket is None, the key definitely doesn't exist
        if values is None:
            return -1

        # Look for the key in the bucket list
        for pairs in values:
            if pairs[0] == key:
                return pairs[1]

        # Key not found after checking the whole bucket
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains it.
        1. Locate the bucket.
        2. Iterate through the bucket to find the matching pair.
        3. Remove the entire [key, value] pair from the list.
        """
        hash_value = self.my_hash(key)
        values = self.hash_table[hash_value]
        
        if values is None:
            return

        for pairs in values:
            if pairs[0] == key:
                # Remove the actual object 'pairs' from the bucket list
                values.remove(pairs)
                return # Exit immediately after the first removal


# Your MyHashMap object will be instantiated and called as such:

obj = MyHashMap()

#print("1. إضافة المفتاح 2 بقيمة 2")
obj.put(2, 2) 

#print("\n2. إضافة نفس المفتاح 2 بقيمة 1 (تحديث)")
obj.put(2, 1) # هنا الـ return بتمنع التكرار

#print("\n3. إضافة المفتاح 1002 (بيروح لنفس صندوق رقم 2 - تصادم)")
obj.put(1002, 99) 

obj.put(1020, 9) 
#print("\n4. محاولة الحصول على قيمة المفتاح 2")
print(obj.get(2))

#print("\n5. مسح المفتاح 2")
#obj.remove(2)

#print("\n6. هل المفتاح 2 لسه موجود؟")
print( obj.get(2))

print(obj.hash_table)