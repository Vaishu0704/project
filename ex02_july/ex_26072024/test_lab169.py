import csv
import pytest


class Test_CRUD(object):
    def test_update(self):
        #Read the file
        with open (r"C:\Users\91915\PycharmProjects\project\ex02_july\ex_26072024\testdata.csv") as csvfile:
            reader=csv.reader(csvfile)
            for col in reader:
                print(col[0],col[1],col[2])