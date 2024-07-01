from abc import ABC,abstractmethod
class pyatb(ABC):
    @abstractmethod
    def perf_task1(self):
        pass
    @abstractmethod
    def perf_task2(self):
        pass
class Vaishu(pyatb):
    def perf_task1(self):
        print('Done task1')
    def perf_task2(self):
        print('Done task2')

vaish=Vaishu()
vaish.perf_task1()
vaish.perf_task2()