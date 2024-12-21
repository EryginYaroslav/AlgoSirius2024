class Relevance:
    arr_priznak = []
    n_num = []
    
    def __init__(self):
        cnt_param = int(input())
        if cnt_param < 1 or cnt_param > 100:
            print('Не в промежутке 1 <= n <= 100')
            exit()
        n_num = input()
        n_num = n_num.split()
        self.n_num.append(n_num) 
        if len(n_num) < 0 or len(n_num) > (10**8):
            print('Не в промежутке 0 <= n <= 10^8')
            exit()
        #print(n_num)
        d_num = int(input())
        if (d_num < 1 or d_num > 100000) or ((d_num*len(n_num)) > 100000):
            print('err')
            exit()
        #print(d_num)
        #arr_priznak = []
        for x in range (0,d_num):
            priznak = input()
            priznak = priznak.split()
            if len(priznak) > cnt_param:
                print('err')
                exit()
            self.arr_priznak.append(priznak)
        #print(arr_priznak)
        cnt_query = int(input())
        if cnt_query < 1 or cnt_query>100000:
            exit()
        for x in range (0,cnt_query):
            query = input()
            query = query.split()
            if len(query) == 2:
                print('get')
                if int(query[1]) < 0 or int(query[1]) > 10 or int(query[0]) != 1:
                    print('err')
                    exit()
                
            elif len(query) == 4:
                print('update')
                if query[0] != 2 or query[1] < 1 or query[1] > d_num or query[2] < 1 or query[2] > n_num or query[3] < 0 or query[3] > (10**8):
                    print('err')
                    exit()
                
            else:
                print('err')
                exit()
    
    def calc(self):
        print(self.arr_priznak)
        print(self.n_num)
        n_num_int = [int(num) for num in self.n_num]
        for priznak in self.arr_priznak:
            res = (priznak[0] * n_num_int[0])+(priznak[1] * n_num_int[1])
            print(res)

            
relevance_instance = Relevance()
relevance_instance.calc()





