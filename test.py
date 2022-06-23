import unittest
from rangedict import RangeDic


dict_test = {"a": "a", "b": "b", "<3":"Less than 3", 
                "other_dict":{"0-5": "Between 0 and 5", 
                "5-10": "Between 5 and 10", 
                ">10": "Bigger than 10"}}
range_dict = RangeDic(dict_test)

class TestRangeDict(unittest.TestCase):
    def test_normal_dict(self):
        self.assertEqual(range_dict["a"], dict_test["a"])
    
    def test_first_level_range(self):
        self.assertEqual(range_dict[2], dict_test["<3"])

    def test_second_level_range_first_range(self):
        self.assertEqual(range_dict["other_dict"][0], dict_test["other_dict"]["0-5"])  
        self.assertEqual(range_dict["other_dict"][1], dict_test["other_dict"]["0-5"])  
        self.assertEqual(range_dict["other_dict"][2], dict_test["other_dict"]["0-5"])  
        self.assertEqual(range_dict["other_dict"][3], dict_test["other_dict"]["0-5"]) 
        self.assertEqual(range_dict["other_dict"][4], dict_test["other_dict"]["0-5"]) 

    def test_second_level_range_second_range(self):
        self.assertEqual(range_dict["other_dict"][5], dict_test["other_dict"]["5-10"])  
        self.assertEqual(range_dict["other_dict"][6], dict_test["other_dict"]["5-10"]) 
        self.assertEqual(range_dict["other_dict"][7], dict_test["other_dict"]["5-10"]) 
        self.assertEqual(range_dict["other_dict"][8], dict_test["other_dict"]["5-10"]) 
        self.assertEqual(range_dict["other_dict"][9], dict_test["other_dict"]["5-10"])

    def test_second_level_bigger_than(self):
        self.assertEqual(range_dict["other_dict"][10.0001], dict_test["other_dict"][">10"])  
        self.assertEqual(range_dict["other_dict"][11], dict_test["other_dict"][">10"])  
        self.assertEqual(range_dict["other_dict"][20], dict_test["other_dict"][">10"])  
        self.assertEqual(range_dict["other_dict"][345664], dict_test["other_dict"][">10"])  
        
         