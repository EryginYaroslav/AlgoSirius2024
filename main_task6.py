from datetime import datetime, timedelta

def get_max_guest(self):
    day = []
    #перебираем массив
    for in_otel,out_otel in self:
        #прелобрахуем в тип дата
        in_otel = datetime.strptime(in_otel,"%Y-%m-%d")
        #прибалвяем 1 день так как считаем что в этот день гостя уже нет
        out_otel = datetime.strptime(out_otel,"%Y-%m-%d") + timedelta(days=1)
        #добавляем к списку дат количесвто гостей +-1 в зависимости от события
        day.append((in_otel,+1))
        day.append((out_otel,-1))
    #обязательно сортируем массив, что бы сохранить хронологию заезда/выезда
    day.sort()
    #устанавливаем счетчики
    cur_guest = 0
    max_guest = 0
    max_date = None
    #перебираем список и сравнивам даты 
    for date, guest in day:
        #устанавливаем количество гостей, на каждой итерации +- 1
        cur_guest += guest
        #проверяем количество гостей, если увеличилось устанавливаем максимальное количество и дату
        if cur_guest > max_guest:
            max_guest = cur_guest
            max_date = date
    #возвращаем результат, при этом оставляя Y-m-d от даты
    return f'max_date: {max_date.strftime("%Y-%m-%d")}, max_guest: {max_guest}'
    
date = [("2024-09-20", "2024-09-21"), ("2024-09-14", "2024-09-21"), ("2024-09-21","2024-09-25")]
res = get_max_guest(date)
print(res)