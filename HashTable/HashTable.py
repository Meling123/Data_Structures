class ListOutOfSpaceError(Exception):
    pass

class NoDataInListError(Exception):
    pass


class Element:
    def __init__(self, key, val):
        self.key = key
        self.val = val
    def __str__(self):
        return f"{self.key} : {self.val}"

    def __repr__(self):
        return f"{self.key} : {self.val}"

class HashTable:

    def __init__(self, size, c1=1, c2=0):
        self.tab = [None]*size
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def modulo_n(self, key) -> int:
        if isinstance(key, str):
            key = sum([ord(i) for i in key])
        return key % self.size
    
    def colision(self, item) -> None:
        for i in range(1,self.size):
            index = self.modulo_n(self.modulo_n(item.key) + self.c1 * i + self.c2 * i**2)
            if self.tab[index] == None:
                self.tab[index] = item
                return
            if isinstance(self.tab[index], Element) and self.tab[index].key == item.key:
                self.tab[index] = item
                return
        print('Out of space')
        raise ListOutOfSpaceError

    def insert(self, item) -> None:        
            index = self.modulo_n(item.key)
            if self.tab[index] is None:
                self.tab[index] = item
                return
            if self.tab[index].key == item.key and isinstance(item, Element):
                self.tab[index] = item
                return           
            self.colision(item)
        
    def search(self, key) -> Element.val:
        index = self.modulo_n(key)
        data = self.tab[index]
        if data == None:
            print('Data not found')
            return None
        if data.key != key:
            for i in range(1,self.size):
                idx = self.modulo_n(index + self.c1 * i + self.c2 * i**2)
                if self.tab[idx].key == key:
                    return self.tab[idx].val
        return self.tab[index].val
       
    def remove(self, key) -> None:
        index = self.modulo_n(key)
        if self.tab[index] is None:
            print('Data not found')
            raise NoDataInListError
        self.tab[index] = None
            
    def __str__(self):
        s = '{'
        for i in self.tab:
            if i is not None:
                s += f'{i.key}: {i.val}, '
        return s[:-2] + '}'
    
def test_first(c1=1,c2=0):
        ht = HashTable(13,c1,c2)
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        for i in range(1, 16):
            try:
                if i == 6:
                    ht.insert(Element(18, "F"))
                    continue
                if i == 7:
                    ht.insert(Element(31, "G"))
                    continue
                ht.insert(Element(i, letters[i - 1]))
            except ListOutOfSpaceError:
                print(f"Not enough space, Element: {i} was not allocated")
        
        print(ht)
        print(ht.search(5))
        print(ht.search(14))
        ht.insert(Element(5, "Z"))
        print(ht.search(5))
        ht.remove(5)
        print(ht)
        print(ht.search(31))
        ht.insert(Element("W", "test"))
        print(ht)

def test_second(c1=1, c2=0):
    ht = HashTable(13, c1, c2)
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    for i in range(1, 14):
        try:
            ht.insert(Element(i * 13, letters[i - 1]))
        except ListOutOfSpaceError:
            print(f"Not enough space, Element: {i * 13} was not allocated")
    print(ht)

test_first(1, 0)
test_second(1, 0)  
test_second(0, 1) 
test_first(0, 1)  