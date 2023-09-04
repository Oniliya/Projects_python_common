# __
# Монады: Реализуйте класс IO (ввод-вывод), который будет представлять действие ввода-вывода. 
# Создайте функцию-редуктор, которая будет принимать список IO и последовательно выполнять каждое действие, сохраняя результаты в список.

class IO:
    def __init__(self, data):
        self.data=data

    def get_data(self):
        # ввод данных
        print("_input_  <- "+self.data)
        return self.data
    
    def process_data(self, data):
        # вывод данных, обработка данных
        processed_data = data+"###"
        print("_out_  -> "+processed_data)
        return processed_data
    
class Reducer:
    def reduce(self, io_list):
        result=[]
        for io in io_list:
            data = io.get_data()
            processed_data = io.process_data(data)
            result.append(processed_data)
        return result
    

# создаем объекты списка IO
io1=IO("data1")
io2=IO("data2")
io3=IO("data3")

io_list=[io1, io2, io3]

reducer = Reducer()
reduce_list = reducer.reduce(io_list)

print(reduce_list)