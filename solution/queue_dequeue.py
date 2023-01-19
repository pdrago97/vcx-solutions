class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise QueueDequeueException("Cannot dequeue from an empty queue.")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __len__(self):
        return len(self.items)

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


class QueueDequeueException(Exception):
    pass
  