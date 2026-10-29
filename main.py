class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Проверка на пустоту.Возвращает True или False."""
        if self.items is None:
           return True
        return False

    def push(self,item):
        """"Добавление элемента в стек"""
        self.items.append(item)


    def pop(self):
        """Метод удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека"""
        return self.items.pop()

    def peek(self):
       """Метод возвращает верхний элемент стека, но не удаляет его. Стек не меняется"""
       return self.items[-1]

    def size(self):
        """Метод возвращает количество элементов в стеке"""
        return len(self.items)

def balanser(string):
    """Баланс скобок"""
    stack = Stack()
    for element in string:
        stack.push(element)
    if stack.size() % 2 == 0:
        return "Сбалансированно"
    return "Несбалансированно"

if __name__ == '__main__':
   print(balanser('(((([{}]))))'))
   print(balanser('[([])((([[[]]])))]{()}'))
   print(balanser('{{[()]}}'))
   print(balanser('}{}'))
   print(balanser('{{[(])]}}'))
   print(balanser('[[{())}'))


