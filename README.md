# RangeDict

RangeDict extends a dictionary class to use numbers as values interpreted with ranges defined as keys.

Examples


<code>
dict_test = {"a": "a", 
             
            "b": "b",
  
            "<-3":"Less than 3",
              
            "[-2--1)":"Bigger than -2 (included) smaller than -1 (not included)",
              
              ">=5": "Bigger or equal than 5"}
  </code>
  
  
A RangeDict instance is obtained by coding RangeDict(dict_test)  
  
- If a string key is intoduced, RangeDict will look for the input key in the keys list as an usual dictionary 
- When a number is introduced, RangeDict will parse the keys list to decide what fits.
 
The parsed rules are the following:
- >5: Bigger than 5
- >=-5: Equals or bigger than -5
- <5: Smaller than 5
- <=5: Equals or smaller than 5
- -1-4: A number between -1 (included) and 4 (not included) 
- [-1-4): A number between -1 (included) and 4 (not included) 
- (-1-4]: A number between -1 (not included) and 4 (included) 
- (-10--4): A number between -10 (not included) and -4 (included) 
- [-10--4]: A number between -10 (included) and -4 (included) 
  
  Examples
  
- dict_test["a"] = "a"
-  dict_test["b"] = "b". 
- dict_test[-5] = "Less than 3"
- dict_test[-3] = None
- dict_test[-2] = "Bigger than -2 (included) smaller than -1 (not included)"
- dict_test[-1.5] = "Bigger than -2 (included) smaller than -1 (not included)"
- dict_test[150] = "Bigger or equal than 5"
  
  
    
    
