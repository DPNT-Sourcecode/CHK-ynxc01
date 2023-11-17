from lib.solutions.SUM import sum_solution

class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
        
    def test_sumTwo(self):
        assert sum_solution.compute(1,43) == 44
        
    def test_sumThree(self):
        assert sum_solution.compute(-11,43) == 32
    
    def test_sumFour(self):
        assert sum_solution.compute(-11,-20) == -31
        
