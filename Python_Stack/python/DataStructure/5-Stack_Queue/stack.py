class Stack:
    """Stack data structure with a maximum capacity."""
    
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity

    def push(self, item):
        if len(self.data) >= self.capacity:
            print("Stack Overflow: Stack is full!")
        else:
            self.data.append(item)

    def pop(self):
        if len(self.data) == 0:
            print("Pop from empty stack")
            return None
        return self.data.pop()
 
    def peek(self):
        if len(self.data) == 0:
            print("Peek at empty stack")
            return None
        return self.data[-1]
    

    
# s = Stack(capacity=5)
# s.push("sara")
# s.push("test")
# print(s.peek())


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if len(self.data) == 0:
            print("empty Queue")
        return self.data.pop(0)

    def peek(self):
        if len(self.data) == 0:
            print("empty Queue")
        return self.data[0]

    def rear(self):
        if len(self.data) == 0:
            print("empty Queue")
        return self.data[-1]
    
# q = Queue()

# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)

# print( q.peek())       
# print(q.dequeue())    
# print( q.dequeue())    
# print( q.peek())      


#1. Reverse a String Using a Stack

def reverse_string(str):
    stack = Stack(capacity=len(str))
    for char in str:
        stack.push(char)
    
    reversed =""
    while len(stack.data) > 0:
        reversed+=stack.pop()

    return reversed

print (reverse_string("Hello"))


# 2. For each temperature find how many days until a warmer temperature.
def days_until_warmer(temps):
    stack = Stack(capacity=len(temps)) 
    result = [0] * len(temps)

    for i in range(len(temps)):
        current_temp = temps[i]
        
        # While stack is not empty and current temp is warmer than the temp at stack's top index
        while len(stack.data) > 0 and temps[stack.peek()] < current_temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
            
        stack.push(i)

    return result

# Example: 
print(days_until_warmer([22, 18, 28, 32, 25, 20, 23])) # out: [2, 1, 1, 0, 0, 1, 0]


#3. First Non-Repeating Character in a Stream. As characters arrive return the first non-repeating one
def non_repeating_character(stream):
    queue = Queue()
    count = {}

    for char in stream:
        count[char] = count.get(char, 0) + 1

        if count[char] == 1:
            queue.enqueue(char)

        while len(queue.data) > 0 and count[queue.peek()] > 1:
            queue.dequeue()

        if len(queue.data) > 0:
            print(queue.peek(), end=" ")
        else:
            print("#", end=" ")

non_repeating_character("AABCD")

