class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
    
    def get_item(self):
        return self.item
    
    def get_ref(self):
        return self.ref