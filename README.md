# Library Management System (LMS) ReadMe

## Introduction:
The Library Management System (LMS) is a simple GUI application developed using the `tkinter` module in Python. This application allows you to add, delete, view, and update the names of books in a virtual library.

## Features:
1. **Add Book**: Users can add a new book name to the list.
2. **Delete Book**: Users can remove a book from the list.
3. **View Book**: Clicking on a book name displays it in the entry field.
4. **Update Book**: Users can modify the name of a selected book.

## Dependencies:
To run the Library Management System, ensure you have `tkinter` installed. If not, you can typically install it with the following:

```bash
pip install tk
```

(Note: `tkinter` is included with most standard Python installations.)

## How to Run:

1. Save the provided code in a file named `LibraryManagementSystem.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Run the following command:

```bash
python LibraryManagementSystem.py
```

## Usage:

1. **To Add a Book**:
    - Enter the book name in the entry field.
    - Click the "Add Book" button.

2. **To Delete a Book**:
    - Select a book name from the list.
    - Click the "Delete Book" button.

3. **To View a Book**:
    - Simply click on a book name in the list. The name will be displayed in the entry field.

4. **To Update a Book**:
    - Select a book from the list.
    - Modify the book name in the entry field.
    - Click the "Update Book Name" button.

## Error Handling:
The application provides warning prompts in case:
- A book name is not provided while trying to add.
- A book is not selected while attempting to delete or update.

## Conclusion:
The Library Management System offers a user-friendly interface for managing books in a library. It showcases basic CRUD (Create, Read, Update, Delete) operations using `tkinter`. The program can be extended to include additional features such as storing book author names, genres, etc.
