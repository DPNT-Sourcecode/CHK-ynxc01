from solutions.TST import one
from solutions.SUM import compute

class TestSum():
    def test_sum(self):
        assert one.get() == 1
    
    def test_sumTwo(self):
        assert compute(1,43) == 44

