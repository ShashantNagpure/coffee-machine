# coffee-machine

Steps:
1. cd to downloaded local directory
2. python -m pip install .\lib\apsw-3.34.0-cp39-cp39-win_amd64.whl #install apsw using whl file, or ref: https://rogerbinns.github.io/apsw/download.html
3. pip install nose
4. pip install coverage
5. coverage run --source=machine -m nose .\machine\test_machine.py --debug=machine #for running integration test
6. coverage report // for seeing coverage
