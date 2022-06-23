import unittest
from rangedict import RangeDic


dict_test = {"a": "a", 
            "b": "b", 
            "<-3":"Less than 3", 
            "[-2--1)":"Bigger than -2 (included) smaller than -1 (not included)",
            ">=5": "Bigger or equal than 5",

                "other_dict":{
                "<=1": "Equal or smaller than 1",
                "2-5": "Between 1 and 5 (1 included, 5 not included", 
                "(5-10)": "Between 5 and 10 (not included)", 
                "[10-15]": "Between 10 and 15 (both included)", 
                "(15-20]": "Between 15 and 20 (15 not included. 20 included)", 
                ">20": "Bigger than 10"}}
range_dict = RangeDic(dict_test)

class TestRangeDict(unittest.TestCase):
    def test_normal_dict(self):
        self.assertEqual(range_dict["a"], dict_test["a"])
        self.assertEqual(range_dict["b"], dict_test["b"])
        self.assertEqual(range_dict["other_dict"], dict_test["other_dict"])
        self.assertEqual(range_dict["other_dict"]["(5-10)"], dict_test["other_dict"]["(5-10)"])
    
    def test_first_level_less_than(self):
        self.assertNotEqual(range_dict[-3.00], dict_test["<-3"])
        self.assertEqual(range_dict[-3.001], dict_test["<-3"])
        self.assertEqual(range_dict[-3.5], dict_test["<-3"])
        self.assertEqual(range_dict[-5], dict_test["<-3"])
        self.assertEqual(range_dict[-10], dict_test["<-3"])

    def test_first_level_first_range(self):
        self.assertNotEqual(range_dict[-3.1], dict_test["[-2--1)"])
        self.assertEqual(range_dict[-2], dict_test["[-2--1)"])
        self.assertEqual(range_dict[-1.5], dict_test["[-2--1)"])
        self.assertNotEqual(range_dict[-1], dict_test["[-2--1)"])

    def test_first_level_bigger_or_equal_than(self):
        self.assertEqual(range_dict[5], dict_test[">=5"])
        self.assertEqual(range_dict[5.0], dict_test[">=5"])
        self.assertEqual(range_dict[5.1], dict_test[">=5"])
        self.assertEqual(range_dict[1561], dict_test[">=5"])

    def test_second_level_range_smaller_or_equal(self):
        self.assertEqual(range_dict["other_dict"][0], dict_test["other_dict"]["<=1"])  
        self.assertEqual(range_dict["other_dict"][-125.25], dict_test["other_dict"]["<=1"]) 
        self.assertEqual(range_dict["other_dict"][-25], dict_test["other_dict"]["<=1"]) 
        self.assertEqual(range_dict["other_dict"][1], dict_test["other_dict"]["<=1"])  

    def test_second_level_range_first_range(self):
        self.assertEqual(range_dict["other_dict"][2], dict_test["other_dict"]["2-5"])  
        self.assertEqual(range_dict["other_dict"][3], dict_test["other_dict"]["2-5"]) 
        self.assertEqual(range_dict["other_dict"][4], dict_test["other_dict"]["2-5"]) 

    def test_second_level_range_second_range(self):
        self.assertNotEqual(range_dict["other_dict"][5], dict_test["other_dict"]["(5-10)"])  
        self.assertEqual(range_dict["other_dict"][6], dict_test["other_dict"]["(5-10)"]) 
        self.assertEqual(range_dict["other_dict"][7], dict_test["other_dict"]["(5-10)"]) 
        self.assertEqual(range_dict["other_dict"][8], dict_test["other_dict"]["(5-10)"]) 
        self.assertEqual(range_dict["other_dict"][9], dict_test["other_dict"]["(5-10)"])
        self.assertNotEqual(range_dict["other_dict"][10], dict_test["other_dict"]["(5-10)"])
 
    def test_second_level_range_third_range(self):
        self.assertEqual(range_dict["other_dict"][10], dict_test["other_dict"]["[10-15]"])  
        self.assertEqual(range_dict["other_dict"][11], dict_test["other_dict"]["[10-15]"]) 
        self.assertEqual(range_dict["other_dict"][12], dict_test["other_dict"]["[10-15]"]) 
        self.assertEqual(range_dict["other_dict"][13], dict_test["other_dict"]["[10-15]"]) 
        self.assertEqual(range_dict["other_dict"][14], dict_test["other_dict"]["[10-15]"])
        self.assertEqual(range_dict["other_dict"][15], dict_test["other_dict"]["[10-15]"])

    def test_second_level_range_fourth_range(self):
        self.assertNotEqual(range_dict["other_dict"][15], dict_test["other_dict"]["(15-20]"])  
        self.assertEqual(range_dict["other_dict"][16], dict_test["other_dict"]["(15-20]"]) 
        self.assertEqual(range_dict["other_dict"][17], dict_test["other_dict"]["(15-20]"]) 
        self.assertEqual(range_dict["other_dict"][18], dict_test["other_dict"]["(15-20]"]) 
        self.assertEqual(range_dict["other_dict"][19], dict_test["other_dict"]["(15-20]"])
        self.assertEqual(range_dict["other_dict"][20], dict_test["other_dict"]["(15-20]"])

    def test_second_level_bigger_than(self):
        self.assertNotEqual(range_dict["other_dict"][20], dict_test["other_dict"][">20"])  
        self.assertEqual(range_dict["other_dict"][20.0001], dict_test["other_dict"][">20"])  
        self.assertEqual(range_dict["other_dict"][121], dict_test["other_dict"][">20"])  
        self.assertEqual(range_dict["other_dict"][50], dict_test["other_dict"][">20"])  
        self.assertEqual(range_dict["other_dict"][345664], dict_test["other_dict"][">20"])  
        
         