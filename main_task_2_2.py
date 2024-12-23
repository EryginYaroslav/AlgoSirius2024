class Relevance:
    def __init__(self):
        # Считываем количество параметров
        self.cnt_param = int(input())
        # Проверяем, что количество параметров в допустимом диапазоне
        if self.cnt_param < 1 or self.cnt_param > 100:
            print('Ошибка: число параметров вне диапазона 1 <= n <= 100')
            exit()

        # Считываем веса параметров
        self.weights = list(map(int, input().split()))
        # Проверяем корректность введенных весов
        if len(self.weights) != self.cnt_param or any(a < 0 or a > 10**8 for a in self.weights):
            print('Ошибка: веса параметров некорректны')
            exit()

        # Считываем количество объектов
        self.cnt_objects = int(input())
        # Проверяем, что количество объектов в допустимом диапазоне
        if self.cnt_objects < 1 or self.cnt_objects > 100000:
            print('Ошибка: число объектов вне диапазона 1 <= d <= 100000')
            exit()

        self.objects = []
        # Считываем объекты и проверяем их корректность
        for _ in range(self.cnt_objects):
            obj = list(map(int, input().split()))
            if len(obj) != self.cnt_param or any(f < 0 or f > 10**8 for f in obj):
                print('Ошибка: признаки объекта некорректны')
                exit()
            self.objects.append(obj)

        # Считываем количество запросов
        self.cnt_queries = int(input())
        # Проверяем, что количество запросов в допустимом диапазоне
        if self.cnt_queries < 1 or self.cnt_queries > 100000:
            print('Ошибка: число запросов вне диапазона 1 <= q <= 100000')
            exit()

        self.queries = []
        # Считываем запросы и проверяем их корректность
        for _ in range(self.cnt_queries):
            query = list(map(int, input().split()))
            if len(query) == 2 and query[0] == 1 and 1 <= query[1] <= 10:
                self.queries.append(query)  # Запрос на выдачу топ-K
            elif len(query) == 4 and query[0] == 2 and 1 <= query[1] <= self.cnt_objects \
                    and 1 <= query[2] <= self.cnt_param and 0 <= query[3] <= 10**8:
                self.queries.append(query)  # Запрос на изменение признака
            else:
                print('Ошибка: некорректный запрос')
                exit()

    def calc_relevance(self, obj):
        # Вычисляем релевантность объекта, умножая веса на параметры объекта и суммируя результаты
        return sum(a * f for a, f in zip(self.weights, obj))
    
    def calc(self):
        # Обрабатываем каждый запрос из списка
        for query in self.queries:
            if query[0] == 1:  # Запрос на выдачу топ-K
                k = query[1]  # Получаем значение K
                # Вычисляем релевантность для каждого объекта и создаем список кортежей (релевантность, индекс)
                relevances = [(self.calc_relevance(obj), i + 1) for i, obj in enumerate(self.objects)]
                # Сортируем список по релевантности (по убыванию) и по индексу (по возрастанию)
                relevances.sort(reverse=True, key=lambda x: (x[0], -x[1]))
                # Извлекаем индексы объектов с наивысшей релевантностью
                result = [idx for _, idx in relevances[:k]]
                print(*result)  # Печатаем индексы объектов
            elif query[0] == 2:  # Запрос на изменение признака
                obj_idx = query[1] - 1  # Индекс объекта (уменьшаем на 1 для доступа к списку)
                param_idx = query[2] - 1  # Индекс параметра (уменьшаем на 1 для доступа к списку)
                new_value = query[3]  # Новое значение для параметра
                self.objects[obj_idx][param_idx] = new_value  # Обновляем значение параметра объекта

# Создаем экземпляр класса и запускаем обработку запросов
relevance_instance = Relevance()
relevance_instance.calc()
