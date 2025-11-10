class Node:
    def __init__(self, x: int, next: 'Node' = None, prev: 'Node' = None, key: int = 0):
        self.val = int(x)
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        print("init")
        # map to nodes
        self.key_to_list: [int, Node] = {}

        self.cap: int = capacity
        self.len: int = 0

        self.start: Node = Node(-1)        
        self.end: Node = Node(-1)

        # two dummy nodes to make del ez
        self.start.next = self.end
        self.end.prev = self.start


    def del_node(self, to_delete: Node):
        print("del")
        prev, next = to_delete.prev, to_delete.next
        prev.next = next
        next.prev = prev

    def add_node_to_end(self, to_add: Node):
        print("add")
        prev, next = self.end.prev, self.end 
        prev.next = to_add
        self.end.prev = to_add
        to_add.prev = prev
        to_add.next = next

        
    def get(self, key: int) -> int:
        print("get")
        if key in self.key_to_list:
            found_node = self.key_to_list[key]             
            # move found node to the end of the list
            self.del_node(found_node)
            self.add_node_to_end(found_node)
            # return the val of the found node
            return found_node.val
        else:
            # not found
            return -1
        

    def put(self, key: int, value: int) -> None:
        print("put")
        if key in self.key_to_list:
            found_node: Node = self.key_to_list[key]             
            # move found node to the end of the list
            self.del_node(found_node)
            self.add_node_to_end(found_node)
            # change val of node 
            found_node.val = value
        else:
            # create a new node
            to_insert: Node = Node(value, key=key) 
            if self.len == self.cap:
                # we need to shift out a val and get rid of
                # its entry in dict
                self.key_to_list.pop(self.start.next.key)
                self.del_node(self.start.next)
                self.add_node_to_end(to_insert)
            else:
                self.add_node_to_end(to_insert)
                self.len += 1

            # put it in dict
            self.key_to_list[key] = to_insert


