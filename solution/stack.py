class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def __print__(self):
        if len(self.items) == 0:
            print = ''
            return print
        else:
            print = ""
            for item in self.items:
                print += f"{item} -> "
                if item == self.items[-1]:
                    print = print[:-4]
            return print
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise StackPopException("Cannot pop from an empty stack.")
    
    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

class StackPopException(Exception):
    pass

class StackPrintException(Exception):
    pass
