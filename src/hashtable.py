# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        
        new_node = LinkedPair(key, value)
        hash_key = self._hash_mod(key)
        head = self.storage[hash_key]
        node = head

        if head == None:
            self.storage[hash_key] = new_node
        else:
            if head.key == key:
                new_node.next = head.next
                self.storage[hash_key] = new_node
            else:
                while node:
                    if node.next == None:
                        node.next = new_node
                        break

                    elif node.next.key == key:
                        new_node.next = node.next.next
                        node.next = new_node
                        break
                    else: 
                        node = node.next



    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        hash_key = self._hash_mod(key)
        if self.storage[hash_key]:
            node = self.storage[hash_key]
            count = 0
            while node:
                if count == 0:
                    count += 1

                    if node.key == key:
                        self.storage[hash_key] = node.next
                        break

                elif count > 0:
                    if node.next:
                        if node.next.key == key:
                            node.next = node.next.next
                            break
                        else:
                            node = node.next
                    else:
                        return
            return


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        hash_key = self._hash_mod(key)
        if self.storage[hash_key]:
            node = self.storage[hash_key]
            while node:
                if node.key == key:
                    return node.value
                else:
                    node = node.next
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2
        new_ht = HashTable(self.capacity)
        for node in self.storage:
            while node:
                new_ht.insert(node.key, node.value)
                node = node.next
        self.storage = new_ht.storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")



ht = HashTable(8)

ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")
ht.insert("key-8", "val-8")
ht.insert("key-9", "val-9")

print(ht.retrieve("key-0"))
print(ht.retrieve("key-1"))
print(ht.retrieve("key-2"))
print(ht.retrieve("key-3"))
print(ht.retrieve("key-4"))
print(ht.retrieve("key-5"))
print(ht.retrieve("key-6"))
print(ht.retrieve("key-7"))
print(ht.retrieve("key-8"))
print(ht.retrieve("key-9"))
