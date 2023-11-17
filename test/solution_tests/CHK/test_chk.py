from lib.solutions.CHK import checkout_solution

class TestSum():
    def test_basic(self):
        assert checkout_solution.checkout("AB") == 80
    
    def test_offer(self):
        assert checkout_solution.checkout("AAA") == 150
    
    def test_offer_incomplete(self):
        assert checkout_solution.checkout("AAAA") == 200
    
    def test_large(self):
        assert checkout_solution.checkout("AAAAAAAAAAAABBBBCD") == 725
        


