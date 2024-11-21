# JavaScript DOM Manipulation

## Description

This project focuses on learning and practicing JavaScript to manipulate the Document Object Model (DOM). Through various tasks, we explore how to interact with HTML elements, modify their attributes and styles, and fetch data from APIs using JavaScript.

## Learning Objectives

At the end of this project, you will be able to:

- Select HTML elements in JavaScript using various selectors.
- Understand the differences between ID, class, and tag name selectors.
- Modify the style of HTML elements dynamically.
- Retrieve and update the content of HTML elements.
- Manipulate the DOM without reloading the page.
- Make requests using `XmlHTTPRequest` and the `Fetch API`.
- Bind event listeners to DOM and user actions.
- Handle user interactions in a web page.

## Requirements

- **Editors:** Any text editor of your choice.
- **Browser:** All scripts will be tested on Chrome (version 57.0 or later).
- All files must end with a new line.
- A `README.md` file with meaningful content must be present at the root of the project directory.
- Code must follow the **semistandard** style.
- `var` keyword is not allowed; use `let` or `const` instead.
- HTML must not reload for any action (e.g., DOM manipulation, data fetching).

---

## Tasks Overview

### 0. Color Me
Update the text color of the `<header>` element to red (`#FF0000`) using JavaScript.

- **File:** `0-script.js`
- **Selector:** Use `document.querySelector`.

---

### 1. Click and Turn Red
Change the `<header>` text color to red when the user clicks on the tag with ID `red_header`.

- **File:** `1-script.js`
- **Event Listener:** `click`.

---

### 2. Add `.red` Class
Add the class `red` to the `<header>` element when the user clicks on the tag with ID `red_header`.

- **File:** `2-script.js`
- **CSS Class:** `.red { color: #FF0000; }`.

---

### 3. Toggle Classes
Toggle the `<header>` class between `red` and `green` when the user clicks the tag with ID `toggle_header`.

- **File:** `3-script.js`
- Ensure only one class (`red` or `green`) is active at a time.

---

### 4. List of Elements
Add a new `<li>` element with the text `Item` to a `<ul>` element with the class `my_list` when the user clicks the tag with ID `add_item`.

- **File:** `4-script.js`.

---

### 5. Change the Text
Update the text of the `<header>` element to `New Header!!!` when the user clicks the tag with ID `update_header`.

- **File:** `5-script.js`.

---

### 6. Star Wars Character
Fetch and display the name of a Star Wars character using the API `https://swapi-api.hbtn.io/api/people/5/?format=json`.

- **File:** `6-script.js`.
- Use the Fetch API.
- Display the character name in the element with ID `character`.

---

### 7. Star Wars Movies
Fetch and list the titles of all Star Wars movies using the API `https://swapi-api.hbtn.io/api/films/?format=json`.

- **File:** `7-script.js`.
- Display the movie titles in the `<ul>` element with ID `list_movies`.

---

### 8. Say Hello!
Fetch and display the translation of "Hello" in French using the API `https://hellosalut.stefanbohacek.dev/?lang=fr`.

- **File:** `8-script.js`.
- Display the translation in the element with ID `hello`.

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/holbertonschool-higher_level_programming.git
