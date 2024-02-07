# zad 1

from mrjob.job import MRJob

class MRCounter(MRJob):

    def mapper(self, _, line):
        customer_id, _, val = line.split(',')
        yield customer_id, float(val)

    def reducer(self, customer_id, val):
        total_val = 0
        for v in val:
            total_val += v
        yield customer_id, round(total_val, 2)
    
if __name__ == '__main__':
    MRCounter.run()

# zad 2

from mrjob.job import MRJob
from mrjob.step import MRStep

class MRCounter(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_values,
                   reducer=self.reducer_values),
            MRStep(mapper=self.mapper_swap,
                   reducer=self.reducer_sort)]
    
    def mapper_values(self, _, line):
        customer_id, _, val = line.split(',')
        yield customer_id, float(val)

    def reducer_values(self, customer_id, val):
        total_val = 0
        for v in val:
            total_val += v
        yield customer_id, round(total_val, 2)

    def mapper_swap(self, customer_id, total_val):
        yield None, (total_val, customer_id)

    def reducer_sort(self, _, valu):
        for total_val, customer_id in sorted(valu):
            yield total_val, customer_id
    
if __name__ == '__main__':
    MRCounter.run()