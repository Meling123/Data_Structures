class Element:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class List:
    def __init__(self):
        self.head = None


    def __repr__(self):
        if not self.is_empty():
            st = '['
            head = self.head
            while head.next is not None:
                st +=  str(head.data) + ', ' 
                head = head.next
            st += str(head.data) + ']'
            return st
        else:
            return '[]'

    def add(self, item) -> None:
        self.head = Element(item, self.head)


    def destroy(self) -> None:
        self.head = None


    def append(self, item) -> None:
        if not self.is_empty():    
            last = self.head
            head = self.head
            while head is not None:
                last = head
                head = head.next           
            last.next = Element(item, None)
        else:
            self.head = Element(item, None)
    
    
    def is_empty(self) -> bool:
        return self.head is None


    def get(self) -> Element.data:
        return self.head.data


    def lenght(self) -> int:
        if not self.is_empty():
            len = 1
            head = self.head
            while head.next is not None:
                len += 1
                head = head.next
            return len
        return 0


    def remove(self) -> None:
        if not self.is_empty():
            head = self.head
            self.head = head.next

    def remove_end(self) -> None:
        if not self.is_empty():
            if self.lenght() > 1:
                last = self.head
                head = self.head
                while head.next is not None:
                    last = head
                    head = head.next
                last.next = None
            else:
                self.head = None
def main():
    l = [('AGH', 'Kraków', 1919),
        ('UJ', 'Kraków', 1364),
        ('PW', 'Warszawa', 1915),
        ('UW', 'Warszawa', 1915),
        ('UP', 'Poznań', 1919),
        ('PG', 'Gdańsk', 1945)]

    unis = List()
    
    for i in range(3):
        unis.append(l[i])
    for i in range(3, 6):
        unis.add(l[i])
    
    print(unis)
    print(unis.lenght())
    unis.remove()
    print(unis.get())
    unis.remove_end()
    print(unis)
    unis.destroy()
    print(unis.is_empty())
    unis.remove()
    unis.append(l[0])
    unis.remove_end()
    print(unis)

main()