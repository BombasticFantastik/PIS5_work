import pytest
from Test import sum2
from PIS_WORK3 import *

def test_Remove_quotes_for_list():
    assert Remove_quotes_for_list(["'BlaBla",'HoHoHO"',"'Hello'","Hey'"])==['BlaBla', 'HoHoHO', 'Hello', 'Hey']
def test_Fabric():
    assert Fabric(['Train', '2022.05.05', 'В412УУ623', '13']).Show_data() == ('2022.05.05', 'В412УУ623', '13')
def test_String_to_list_of_classes():
    assert String_to_list_of_classes('Bike 2022.05.05   "К500ПК633" 130')[0].Show_data() == ('2022.05.05', 'К500ПК633', '130')
    assert String_to_list_of_classes("Work2_txt_test.txt")[0].Show_data() == ('2022.05.05', 'А414БВ799', '15')
    assert String_to_list_of_classes('Train 2022.05.05  "В412УУ623" 13;Train 2000.01.01 "Ш414ЛЛ623" 23')[0].Show_data() == ('2022.05.05', 'В412УУ623', '13'),('2000.01.01', 'Ш414ЛЛ623', '23')



test_String_to_list_of_classes()