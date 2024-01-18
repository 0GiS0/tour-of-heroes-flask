# Run all tests
bandit -r .

# Run the same tests that Microsoft Security DevOps extension runs
bandit --tests=B102,B110,B112,B303,B304,B312,B321,B324,B413,B501,B502,B503,B504,B505 model.py
bandit --tests=B102,B110,B112,B303,B304,B312,B321,B324,B413,B501,B502,B503,B504,B505 app.py
