class IndexlistQ:
    def __init__(self, __list = []):
        self.__list = __list

    def enqueue(self, item):
        self.__list.append(item)
    
    def dequeue(self):
        extracted = self.__list.pop(0)
        return extracted
    
    def isEmpty(self):
        if len(self.__list) == 0:
            return True
        return False
