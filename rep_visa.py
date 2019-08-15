# -*- coding: utf-8 -*-
import csv
import datetime
from os import listdir
import os.path, time
import os

def csv_writer(data, path):
    """
    Функция для записи данных в CSV
    """
    with open(path, "w", newline='') as csv_file:
        '''
        csv_file - объект с данными
        delimiter - разделитель
        '''
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerow(line)


if __name__ == "__main__":

files = listdir(".")
mytxt = filter(lambda x: x.endswith('.txt'), files)

    data = [['name','name_last','lang',],
            ['Ivan', 'Ivanov', 'PHP', ],
            ['Anton', 'Antonov', 'Javascript', ],
            ['Egor', 'Egorov', 'Python', ]]
			
			
		t1 = os.path.getmtime(file) # дата последнего изменения файла
        t2 = os.path.getctime(file) # дата создания файла
		
		name = os.path.basename(r'C:\python3\file.txt ')  #имя файла

# напечатать дату в строковом формате:
print time.ctime(t1)
print time.ctime(t2)
			

    path = "visa_files"+now.day+".csv"
    csv_writer(data, path)