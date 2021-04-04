# coffee-machine

Steps:
1. cd to downloaded local directory
2. python -m pip install .\lib\apsw-3.34.0-cp39-cp39-win_amd64.whl #install apsw using whl file, or use ref: https://rogerbinns.github.io/apsw/download.html
3. pip install nose
4. pip install coverage
5. coverage run --source=machine -m nose .\machine\test_machine.py --debug=machine #for running integration test
6. coverage report // for seeing coverage


input payload for running tests: payload/input1.json
sample test output for payload:

machine.test_machine: INFO: available ingredients: {'hot_water': 500, 'hot_milk': 500, 'ginger_syrup': 100, 'sugar_syrup': 100, 'tea_leaves_syrup': 100}
machine.test_machine: INFO: no. of possible outputs : 3
machine.test_machine: INFO: #0 status:
machine.test_machine: INFO: hot_tea is prepared
machine.test_machine: INFO: hot_coffee cannot be prepared because sugar_syrup is not sufficient
machine.test_machine: INFO: black_tea is prepared
machine.test_machine: INFO: green_tea cannot be prepared because green_mixture is not avaialble
machine.test_machine: INFO: left ingredients: {'hot_water': 0, 'hot_milk': 400, 'ginger_syrup': 60, 'sugar_syrup': 40, 'tea_leaves_syrup': 40}
machine.test_machine: INFO: #1 status:
machine.test_machine: INFO: hot_tea is prepared   
machine.test_machine: INFO: hot_coffee is prepared
machine.test_machine: INFO: black_tea cannot be prepared because sugar_syrup is not sufficient
machine.test_machine: INFO: green_tea cannot be prepared because sugar_syrup is not sufficient
machine.test_machine: INFO: left ingredients: {'hot_water': 200, 'hot_milk': 0, 'ginger_syrup': 60, 'sugar_syrup': 40, 'tea_leaves_syrup': 40}
.....

