class _DoubleLinkedBase:
    """ A base class providing a doubly linked list representation."""

    class _Node:
        """ Lightweight, nonpublic class for storing a doubly linked node"""
        __slots__ = '_element', '_prev', '_next'  # __slots are used to define fixed set of attributes that an object of a class should have

 # streamline memory
        def __init__(self, element, prev, next):  # initialize node's fields
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0  # number of elements

    # def length(self):
    #     """Return the number of elements in the list"""
    #     count = 0
    #     current = self._header
    #     while current._next != self._trailer:
    #         current = current._next
    #         count += 1
    #     return count

    def __len__(self):
        return self._size

    def is_empty(self):
        if self._header.next == self._trailer:
            return True
        else:
            return False

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node"""
        newest = self._Node(e, predecessor, successor)
        predecessor._next= newest
        successor._prev = newest
        self._size += 1;
        return newest
        

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its elements"""
        current_node = self._header
        while (current_node.next != node) and (current_node!= self._trailer) :
            current_node = current_node._next
        if current_node == self._trailer:
            return node
        else:
            current_node._next = (current_node._next)._next
            return node
