# coffee-machine

Steps:
1. cd to downloaded local directory

2. python -m pip install .\lib\apsw-3.34.0-cp39-cp39-win_amd64.whl
 // install apsw using provided whl file for windows, or use ref: https://rogerbinns.github.io/apsw/download.html

3. pip install nose
4. pip install coverage
5. coverage run --source=machine -m nose .\machine\test_machine.py --debug=machine //for running integration test
6. coverage report // for seeing coverage


input payload for running tests: payload/input1.json
Make changes to this payload for different coffee-machine configuratiosn

sample test output for payload:
![Screenshot (20)](https://user-images.githubusercontent.com/29044806/113516740-8f33be80-9599-11eb-8224-bf0468567b96.png)

coverage:
![Screenshot (22)](https://user-images.githubusercontent.com/29044806/113516793-e20d7600-9599-11eb-9d61-cd999b7810f8.png)

