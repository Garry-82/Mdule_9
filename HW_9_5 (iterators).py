class StepValueError(ValueError):
    print('шаг не может быть равен 0')
class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.pointer = start
        if step == 0:
            raise StepValueError
#        if (step < 0 and self.start < self.stop) or (step > 0 and self.start > self.stop):
#            return None

        else:
            self.step = step

    def __iter__(self):
        self.pointer = self.start
        return self
    def __next__(self):
        if self.step > 0:  #  -  число шага с положительным знаком!!!
            while self.pointer <= self.stop:
                self.pointer += self.step
                return self.pointer - self.step
        else:  #  -  число шага с отрицательным знаком!!!
            while self.pointer >= self.stop:
                self.pointer += self.step
                return self.pointer - self.step
        raise StopIteration()

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except: StepValueError()

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
    print()
for i in iter3:
    print(i, end=' ')
    print()
for i in iter4:
    print(i, end=' ')
    print()
for i in iter5:
    print(i, end=' ')
    print()
