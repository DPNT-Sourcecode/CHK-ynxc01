from lib.solutions.CHK import checkout_solution

class TestSum():
    def test_basic(self):
        assert checkout_solution.checkout("AB") == 80
    
    def test_offer(self):
        assert checkout_solution.checkout("AAA") == 130
    
    def test_two(self):
        assert checkout_solution.checkout("AAAAA") == 200
    
    def test_offer_incomplete(self):
        assert checkout_solution.checkout("AAAA") == 180
    
    def test_large(self):
        assert checkout_solution.checkout("AAAAAAAAAAAABBBBCD") == 625
    
    def test_invalid(self):
        assert checkout_solution.checkout("aaa") == -1
        
    def test_invalidTwo(self):
        assert checkout_solution.checkout("AAAaaa") == -1
    
    def test_checkOfferE(self):
        assert checkout_solution.checkout("EEEE") == 220
        


