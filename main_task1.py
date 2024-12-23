# сложность алгоритма O(n)
# класс устанавливает элементу значение и ссылку на следующий элемент
# так как список односвязный на предыдущий элемент нет ссылок.
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
# класс управляет добавление и реверсом данных      
class LinkedList:
    def __init__(self):
        # инициализация, ставим голову пустой
        self.head = None
        
    def append(self,value):
        additem = Node(value)
        # если голова пуста О(1)
        if not self.head:           # если голова не задана ставим первый элемент
            self.head = additem
            return                  # выходим 
        # если голова пуста О(n) т.к. надо проходить по всему массиву
        head = self.head             
        while(head.next):           # добираемся до последнего элемента в списке
           head = head.next
        head.next = additem         # указываем в последнем ссылку на новый
    # и перестановка элементов списка, и сбор результата в массив O(n)
    def revers(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Сохраняем следующий узел
            current.next = prev       # Перенаправляем текущий узел на предыдущий
            prev = current            # Двигаем prev на текущий узел
            current = next_node       # Переходим к следующему узлу
        self.head = prev              # Обновляем голову списка на последний узел
        # просто перебираем список и записывам в массив
        result = []
        linkedlist = self.head
        while linkedlist:
            result.append(linkedlist.value)
            linkedlist = linkedlist.next
        return result
# инициализируем список        
ResultList = LinkedList()
# Заполняем список
ResultList.append(1)
ResultList.append(23)
# балуюсь с типами данных, как я понял в функцию можно передавать какой угобно тип данных
ResultList.append(bool(0))
ResultList.append(bool(1))
ResultList.append('string'*2)
ResultList.append(3443.334)
ResultList.append(len('gnirts'))
RESULT = ResultList.revers()
print(RESULT)
