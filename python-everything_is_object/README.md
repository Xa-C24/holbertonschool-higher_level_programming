# Python - Everything is Object 🐍🧠

## Description 📜

This project dives into the fundamental concepts of Python's object model. It explains how Python treats everything as an object and explores the differences between mutable and immutable types, variable references, and assignments. By completing this project, you'll enhance your understanding of Python's internal mechanics, which is essential for writing efficient and bug-free code.

---

## Learning Objectives 🎯

By the end of this project, you should be able to:

- 📦 Understand what an object is in Python.
- 🔍 Distinguish between a class and an instance of a class.
- 🔄 Differentiate between mutable and immutable objects.
- 🔗 Explain variable references and assignments.
- 🆔 Use Python's built-in functions to explore object identifiers.
- ⚙️ Describe how Python handles variable passing to functions.
- 🧩 Identify built-in mutable and immutable types.
- 🛠 Apply these concepts to solve Python-related interview questions.

---

## Resources 📚

Before you begin, make sure to check out these resources:

- [Objects and Values](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
- [Aliasing in Python](https://realpython.com/python-variables/)
- [Mutable vs Immutable Types](https://medium.com/swlh/mutable-and-immutable-in-python-2e6d9effebc6)
- [Cloning Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Tuples](https://docs.python.org/3/library/stdtypes.html#tuple)

---

## Tasks 📝

### Mandatory Tasks

1. **Who am I?**  
   - 🛠 Function to print the type of an object.

2. **Where are you?**  
   - 🛠 Function to get the memory address (identifier) of an object.

3. **Right count**  
   - ✅ Analyze whether variables point to the same object.

4. **List manipulations**  
   - 🔄 Explore how Python handles lists, references, and changes.

5. **Integer incrementation**  
   - ➕ Understand how immutable types like integers behave in functions.

6. **Copy a list**  
   - 🖨 Create a function to copy a list without importing any module.

7. **Tuples: Mutable or Not?**  
   - 🔗 Discover the behaviors of tuples and their special cases.

### Advanced Tasks

- **Blog Post**  
  - ✍️ Write a detailed blog post summarizing everything you've learned.

---

## Examples 💻

### Mutable vs Immutable Objects

```python
# Mutable example
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)  # Output: [1, 2, 3, 4]

# Immutable example
a = 10
b = a
a += 5
print(b)  # Output: 10
