class Relevance:
    def __init__(self):
        self.cnt_param = int(input())
        if self.cnt_param < 1 or self.cnt_param > 100:
            print('Ошибка: число параметров вне диапазона 1 <= n <= 100')
            exit()

        self.weights = list(map(int, input().split()))
        if len(self.weights) != self.cnt_param or any(a < 0 or a > 10**8 for a in self.weights):
            print('Ошибка: веса параметров некорректны')
            exit()

        self.cnt_objects = int(input())
        if self.cnt_objects < 1 or self.cnt_objects > 100000:
            print('Ошибка: число объектов вне диапазона 1 <= d <= 100000')
            exit()

        self.objects = []
        for _ in range(self.cnt_objects):
            obj = list(map(int, input().split()))
            if len(obj) != self.cnt_param or any(f < 0 or f > 10**8 for f in obj):
                print('Ошибка: признаки объекта некорректны')
                exit()
            self.objects.append(obj)

        self.cnt_queries = int(input())
        if self.cnt_queries < 1 or self.cnt_queries > 100000:
            print('Ошибка: число запросов вне диапазона 1 <= q <= 100000')
            exit()

        self.queries = []
        for _ in range(self.cnt_queries):
            query = list(map(int, input().split()))
            if len(query) == 2 and query[0] == 1 and 1 <= query[1] <= 10:
                self.queries.append(query)
            elif len(query) == 4 and query[0] == 2 and 1 <= query[1] <= self.cnt_objects \
                    and 1 <= query[2] <= self.cnt_param and 0 <= query[3] <= 10**8:
                self.queries.append(query)
            else:
                print('Ошибка: некорректный запрос')
                exit()

    def calc_relevance(self, obj):
        return sum(a * f for a, f in zip(self.weights, obj))

    def calc(self):
        for query in self.queries:
            if query[0] == 1:  # Запрос на выдачу топ-K
                k = query[1]
                relevances = [(self.calc_relevance(obj), i + 1) for i, obj in enumerate(self.objects)]
                relevances.sort(reverse=True, key=lambda x: (x[0], -x[1]))
                result = [idx for _, idx in relevances[:k]]
                print(*result)
            elif query[0] == 2:  # Запрос на изменение признака
                obj_idx = query[1] - 1
                param_idx = query[2] - 1
                new_value = query[3]
                self.objects[obj_idx][param_idx] = new_value


relevance_instance = Relevance()
relevance_instance.calc()
