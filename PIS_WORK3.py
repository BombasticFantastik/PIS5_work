import abc
import re
import datetime


class ITransport(abc.ABC):

    @abc.abstractmethod
    def Show_data(self):
        pass


class Car(ITransport):
    def __init__(self, date, num):
        self.date = Chec_Corect_Date(date)
        self.num = Chec_Corect_Number(num)

    def Show_data(self):
        return self.date, self.num


class Train(ITransport):
    def __init__(self, date, num, lenght):
        self.date = Chec_Corect_Date(date)
        self.num = Chec_Corect_Number(num)
        self.lenght = Chec_Corect_Train_len(lenght)

    def Show_data(self):
        return self.date, self.num, self.lenght


class Bike(ITransport):
    def __init__(self, date, num, max_speed):
        self.date = Chec_Corect_Date(date)
        self.num = Chec_Corect_Number(num)
        self.max_speed = Chec_Corect_Bike_speed(max_speed)

    def Show_data(self):
        return self.date, self.num, self.max_speed


def Remove_quotes_for_list(list_of_line):
    list_of_line = [j.replace('"', '').replace("'", '') for j in list_of_line]
    return list_of_line


def Split_by_separator(line):
    line = line.split(';')
    return line


def Try_open_txt(line):
    try:
        line = open(line, encoding="utf-8").read()
    except:
        pass
    finally:
        return line


def String_to_list_of_classes(line):
    list_for_return = []
    line = Try_open_txt(line)
    lines = Split_by_separator(line)
    for transport in lines:
        transport = Line_to_normalize_list(transport)
        transport = Chec_Corect_Len_List(transport)
        transport = Chec_Corect_Class(transport)
        transport = Fabric(transport)
        list_for_return.append(transport)
    return list_for_return


def Fabric(list_transport):
    class_name = list_transport[0]
    if class_name == 'Car':
        transport = Car(list_transport[1], list_transport[2])
        return transport
    if class_name == 'Train':
        transport = Train(list_transport[1], list_transport[2], list_transport[3])
        return transport
    if class_name == 'Bike':
        transport = Bike(list_transport[1], list_transport[2], list_transport[3])
        return transport
    else:
        raise Exception("Получен некоректный класс")


def Line_to_normalize_list(line):
    list_of_line = line.strip().split()
    list_of_line = Remove_quotes_for_list(list_of_line)
    return list_of_line
def Chec_Corect_Number(line):
    result = re.search(r'[А-Я]{1}\d\d\d[А-Я]{2}\d\d\d',line)
    if result:
        if len(line)==len(result[0]):
            return line
    raise Exception("Получен некоректный номер транспорта")
def Chec_Corect_Date(date_time_str):
    try:
        datetime.datetime.strptime(date_time_str, '%Y.%m.%d')
        return date_time_str
    except:
        raise Exception("Получена некоректная дата проезда")


def Chec_Corect_Train_len(lenght):
    try:
        int(lenght)
        if 1 < int(lenght) < 50:
            return lenght
        else:
            raise Exception("Полученна некоректная длина поезда, которая должна быть от 1 до 50 вагонов")
    except:
        raise Exception("Полученна некоректная длина поезда, которая должна быть от 1 до 50 вагонов")


def Chec_Corect_Bike_speed(speed):
    try:
        int(speed)
        if 75 < int(speed) < 300:
            return speed
        else:
            raise Exception("Cкорость мотоцикла должна быть от 75 до 300 км в час")
    except:
        raise Exception("Cкорость мотоцикла должна быть от 75 до 300 км в час")


def Chec_Corect_Len_List(list):
    if len(list) > 2:
        return list
    else:
        # print(list[0],len(list))
        raise Exception("Длина строчки для преобразования в класс слишком мала ")

def Chec_Corect_Class(split_transport):
    if split_transport[0]=='Train':
        try:
            int(split_transport[3])
        except:
            raise Exception("Последнее вводимое значение для класса Train должно содержать длину состава и лежать в диапозоне от 2 до 50")
    if split_transport[0]=='Bike':
        try:
            int(split_transport[3])
        except:
            raise Exception("Последнее вводимое значение для класса Bike должно содержать максимальную скорость и должна лежать в диапозоне от 80 до 200")
    return split_transport