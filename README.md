# RangeDict

RangeDict extends a dictionary class to use numbers as values interpreted with ranges defined as keys at any level.

Examples


<code>
dict_test = {"a": "a", 
             
            "b": "b",
  
            "<-3":"Less than 3",
              
            "[-2--1)":"Bigger than -2 (included) smaller than -1 (not included)",
              
              ">=5": "Bigger or equal than 5"}
  </code>
  
  
A RangeDict instance is obtained by coding:

<code>
range_dict = RangeDict(dict_test)  
</code>

 ## Rules
 
- If a string key is introduced, RangeDict will look for the input key in the keys list as an usual dictionary 
- When a number is introduced, RangeDict will parse the keys list to decide what range is correct. If there are more than one, RangeDict will take the first one.
 
The parsed rules are the following:
- \>5: Bigger than 5
- \>=-5: Equals or bigger than -5
- <5: Smaller than 5
- <=5: Equals or smaller than 5
- -1-4: A number between -1 (included) and 4 (not included) 
- [-1-4): A number between -1 (included) and 4 (not included) 
- (-1-4]: A number between -1 (not included) and 4 (included) 
- (-10--4): A number between -10 (not included) and -4 (included) 
- [-10--4]: A number between -10 (included) and -4 (included) 
  
  ## Examples
  
- range_dict["a"] = "a"
-  range_dict["b"] = "b". 
- range_dict[-5] = "Less than 3"
- range_dict[-3] = None
- range_dict[-2] = "Bigger than -2 (included) smaller than -1 (not included)"
- range_dict[-1.5] = "Bigger than -2 (included) smaller than -1 (not included)"
- range_dict[150] = "Bigger or equal than 5"
  
  
    
    
