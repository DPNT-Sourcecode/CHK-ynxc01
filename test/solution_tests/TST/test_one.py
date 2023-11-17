from lib.solutions.TST import one
from lib.solutions.SUM import sum_solution

class TestSum():
    def test_sum(self):
        assert one.get() == 1
    
    def test_sumTwo(self):
        assert sum_solution.compute(1,43) == 44


