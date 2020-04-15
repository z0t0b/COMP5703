import unittest
import Assignment.makeChange as mc

class MakeChangeTest(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_nominalInputs(self):
        self.assertEquals([1, 1, 1, 1, 1, 1, 1, 1], mc.makeChange(36.41))
        self.assertEquals([0, 0, 1, 0, 0, 0, 0, 0], mc.makeChange(5))
        self.assertEquals([0, 0, 0, 3, 1, 0, 0, 1], mc.makeChange(3.26))
        self.assertEquals([3, 1, 1, 3, 2, 0, 0, 3], mc.makeChange(78.53))
        pass

    def test_worstInputs(self):
        self.assertEquals(None, mc.makeChange("string"))
        self.assertEquals(None, mc.makeChange("1.00"))
        self.assertEquals(None, mc.makeChange())
        self.assertEquals(None, mc.makeChange([4, 8, 9]))
        self.assertEquals(None, mc.makeChange([]))
        self.assertEquals(None, mc.makeChange(99.995))
        self.assertEquals(None, mc.makeChange(-2))
        pass

    def test_boundaryInputs(self):
        self.assertEquals([0, 0, 0, 1, 0, 0, 0, 0], mc.makeChange(1.001))
        self.assertEquals([0, 0, 0, 1, 0, 0, 0, 1], mc.makeChange(1.005))
        self.assertEquals([0, 0, 0, 0, 0, 0, 0, 0], mc.makeChange(0))
        self.assertEquals([4, 1, 1, 4, 3, 2, 0, 4], mc.makeChange(99.994))
        pass
    
    def test_makingChange(self):
        self.assertEquals(10, mc.makingChange(90, 0, 20))
        self.assertEquals(3, mc.makingChange(8, 2, 5))
        self.assertEquals(19.995000000000005, mc.makingChange(99.995, 0, 20))
        self.assertEquals(0.19, mc.makingChange(0.94, 4, 0.25))