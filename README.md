## **TIM 172A Question #4 Extra Credit**

### **Project Directory**
- [Integer.py](./integer.py)
    - Main python code 
    - IntegerOptimization(cost, value, budget)
    - requires 3 parameters:
    ``` python
    IntegerOptimization(cost<list>, value<list>, budget<int>)
    ```
- [config.json](./config.json)
    - JSON dictionary that includes the cost list, value list, and budget value being used for this optimization test
    - Can be easily changed in the config.json


### **Note**
- integer.py reads the values in the config.json so all you need to do is change the config.json file

### **Run Instructions**
- ```
python integer.py
or 
python3 integer.py
```
- Depends on whether running windows or linux