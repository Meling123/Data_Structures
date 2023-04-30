class Element:
    def __init__(self,  __dane, __priorytet):
        self.__dane = __dane
        self.__priorytet = __priorytet

    def __str__(self):
        return f"{self.__priorytet} : {self.__dane}"

    def __lt__(self, other):
        return self.__priorytet < other.__priorytet

    def __gt__(self, other):
        return self.__priorytet > other.__priorytet



class Heap:
    def __init__(self):
        self.tab = []

    def left(self, i) -> int:
        return 2 * i + 1

    def right(self, i) -> int:
        return 2 * i + 2

    def parent(self, i) -> int:
        return (i - 1) // 2

    def is_empty(self) -> bool:
        return not self.tab

    def peek(self) -> int:
        return self.tab[0]

    def size(self) -> int:
        return len(self.tab)


    def dequeue(self) -> Element:
        if self.is_empty():
            return None
        node = self.tab[0]
        self.tab[0] = self.tab[-1] 
        self.tab = self.tab[:-1] 
        self.__heapif(0)
        return node


    def __heapif(self, start) -> None:
        left = self.left(start)
        right = self.right(start)
        largest = start

        if left <= self.size() - 1 and self.tab[left] > self.tab[largest]:
            largest = left

        if right <= self.size() - 1 and self.tab[right] > self.tab[largest]:
            largest = right

        if largest != start:
            self.tab[start], self.tab[largest] = self.tab[largest], self.tab[start]
            self.__heapif(largest)


    def enqueue(self, element: Element) -> None:
        self.tab.append(element)  
        current = self.size() - 1 

        while current > 0 and self.tab[current] > self.tab[self.parent(current)]:
            self.tab[current], self.tab[self.parent(current)] = self.tab[self.parent(current)], self.tab[current]
            current = self.parent(current)


    def print_tab(self) ->None:
        print ('{', end=' ')
        print(*self.tab[:self.size()], sep=', ', end = ' ')
        print( '}')


    def print_tree(self, idx, lvl) -> None:
        if idx < self.size():
            self.print_tree(self.right(idx),lvl+1)
            print(2*lvl*'  ',self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx),lvl+1)




h = Heap()
l = [7, 5, 1, 2, 5, 3, 4, 8, 9]
x = "GRYMOTYLA"
for i in range(len(l)):
    h.enqueue(Element(x[i], l[i]))
h.print_tree(0, 0)
h.print_tab()
data = h.dequeue()
print(h.peek())
h.print_tab()
print(data)
while True:
    el = h.dequeue()
    if el is None:
        break
    print(el)
h.print_tab()