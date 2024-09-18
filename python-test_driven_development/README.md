**Python - Test-driven development**  

**1. What is TDD?**  

TDD is a software development method in which tests are written before the code that is to be tested.  
The idea is first to define what the program should do in terms of expected results, and then to write the code that satisfies these requirements.  


The TDD cycle has three main stages:  
- Red: Write a test that fails.  
- Green: Write just enough code for the test to pass.  
- Refactor: Improve the code without breaking the test.  

**2. TDD steps**  

1. Write a test: Create a test to verify a specific behavior of the function or class.  
2. Run test: The test fails, because the functionality has not yet been implemented.  
3. Write code: Add the code required for the test to pass.  
4. Check test: Make sure the test passes.  
5. Refactor: Improve the code, keeping successful tests.  


**3. Installing the necessary tools**  

Python already includes a library for writing and executing tests, called unittest.  
If you want to use a more modern library, you can use pytest.  

    In your terminal -> pip install pytest  

**The benefits of TDD**

Increased confidence: Every new feature is covered by tests, so it's easier to spot bugs.  
- Easier refactoring: Testing ensures that your program's behavior doesn't change after modification.  
- Living documentation: Tests can serve as documentation of what each part of the code is supposed to do.  


**TDD best practices**  

Write tests for simple cases and then add more complex cases.  
- Handle errors and edge cases with tests.  
- Don't write code without an associated test.  



0. Integers addition            for test in local python3 -m doctest -v ./tests/0-add_integer.txt  
1. Divide a matrix              python3 -m doctest -v ./tests/2-matrix_divided.txt  
2. Say my name                  python3 -m doctest -v ./tests/3-say_my_name.txt  
3. Print square                 python3 -m doctest -v ./tests/4-print_square.txt
4. Text indentation             python3 -m doctest -v ./tests/5-text_indentation.txt
5. Max integer - Unittest       python3 -m unittest tests/6-max_integer_test.py



