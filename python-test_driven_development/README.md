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



0. Integers addition  
1. Divide a matrix  
2. Say my name  
3. Print square  
4. Text indentation  
5. Max integer - Unittest  



