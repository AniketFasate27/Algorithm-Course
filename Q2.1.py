class DirectAddressTable:
    def __init__(self, table_size):
        self.table = [None] * table_size  # Initialize an empty array

    def insert(self, key, element):
        self.table[key] = element

    def search(self, key):
        return self.table[key]

    def delete(self, key):
        self.table[key] = None  # Simply set the element at the index specified by the key to None

# Usage example:
table = DirectAddressTable(1000)
table.insert(42, "Alice")
table.delete(42)



# Create a structure to hold key, element, and a reference to the next element
Structure Node:
    key
    element
    next

# Create a direct-address table with an array of linked lists
Create DirectAddressTable with size table_size:
    table = Array of size table_size
    for each index in table:
        table[index] = None

# Hash function that maps keys to indices
Function hash(key, table_size):
    return key % table_size

# Insert a key-element pair into the direct-address table
Function insert(table, key, element):
    index = hash(key, table_size)
    new_node = Create Node with key and element
    new_node.next = table[index]
    table[index] = new_node

# Search for an element based on the key
Function search(table, key):
    index = hash(key, table_size)
    current = table[index]
    while current is not None:
        if current.key == key:
            return current.element
        current = current.next
    return None

# Delete an element based on a pointer to the object to be deleted
Function delete(table, key, element_pointer):
    index = hash(key, table_size)
    current = table[index]
    previous = None
    while current is not None:
        if current.key == key:
            if previous is None:
                table[index] = current.next
            else:
                previous.next = current.next
            return  # Element found and deleted
        previous = current
        current = current.next

# Usage example:
table_size = 1000
table = Create DirectAddressTable with size table_size
insert(table, 42, "Alice")
insert(table, 17, "Bob")
result = search(table, 42)
delete(table, 42)

#fgfkjvbiufbdfubvkjbv
#dbfjsbhjbgrebvksbdf vmbjhfbsdkbvrbb