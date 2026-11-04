class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Проверка на пустоту.Возвращает True или False."""
        if  not self.items:
           return True
        return False

    def push(self, item):
        """Добавление элемента в стек"""
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
    dict_brackets = {'(':')','[':']','{':'}'}
    for element in string:
        if element == '(' or element == '[' or element == '{':
          stack.push(element)
        elif element == ')' or element == ']' or element == '}':
            if stack.is_empty() or dict_brackets[stack.peek()] != element:
                return "Несбалансированно"
            else:
                stack.pop()
    if stack.size() == 0:
        return "Сбалансированно"
    return "Несбалансированно"


if __name__ == '__main__':
   print(balanser('(((([{}]))))'))
   print(balanser('[([])((([[[]]])))]{()}'))
   print(balanser('{{[()]}}'))
   print(balanser('}{}'))
   print(balanser('{{[(])]}}'))
   print(balanser('[[{())}'))


