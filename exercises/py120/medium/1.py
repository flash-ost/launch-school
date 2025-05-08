"""
Circular Buffer
A circular buffer is a collection of objects stored in a buffer that is treated as though it is connected end-to-end in a circle. When an object is added to this circular buffer, it is added to the position that immediately follows the most recently added object, while removing an object always removes the object that has been in the buffer the longest.

This works as long as there are empty spots in the buffer. If the buffer becomes full, adding a new object to the buffer requires getting rid of an existing object; with a circular buffer, the object that has been in the buffer the longest is discarded and replaced by the new object.

Assuming we have a circular buffer with room for 3 objects, the circular buffer looks and acts like this:

P1	P2	P3	Comments
All positions are initially empty
1			Add 1 to the buffer
1	2		Add 2 to the buffer
2		    Remove oldest item from the buffer (1)
2	3	    Add 3 to the buffer
4	2	3	Add 4 to the buffer, buffer is now full
4		3	Remove oldest item from the buffer (2)
4	5	3	Add 5 to the buffer, buffer is full again
4	5	6	Add 6 to the buffer, replaces oldest element (3)
7	5	6	Add 7 to the buffer, replaces oldest element (4)
7		6	Remove oldest item from the buffer (5)
7			Remove oldest item from the buffer (6)
            Remove oldest item from the buffer (7)
            Remove non-existent item from the buffer (nil)
Your task is to write a CircularBuffer class in Python that implements a circular buffer for arbitrary objects. The class should be initialized with the buffer size and provide the following methods:

put: Add an object to the buffer
get: Remove (and return) the oldest object in the buffer. Return None if the buffer is empty.
You may assume that none of the values stored in the buffer are None (however, None may be used to designate empty spots in the buffer).

Examples
buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True
The above code should display True 15 times.
"""
class CircularBuffer:
    def __init__(self, size=1):
        self._size = size
        self._buffer = []

    def put(self, value):
        if len(self._buffer) == self._size:
            self._buffer.pop(0)
        self._buffer.append(value)

    def get(self):
        return self._buffer.pop(0) if self._buffer else None

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True  