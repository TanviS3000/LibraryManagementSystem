import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LibraryManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        # Create a list to store book details
        self.books = []

        # Widgets
        label = ttk.Label(root, text="Library Management System")
        label.pack(pady=10)

        self.book_name = ttk.Entry(root, width=20)
        self.book_name.pack(pady=10)

        self.add_button = ttk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.pack(pady=10)

        self.del_button = ttk.Button(root, text="Delete Book", command=self.delete_book)
        self.del_button.pack(pady=10)

        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=20)

        self.listbox.bind("<<ListboxSelect>>", self.show_book)

        self.update_button = ttk.Button(root, text="Update Book Name", command=self.update_book)
        self.update_button.pack(pady=10)

    def add_book(self):
        book_name = self.book_name.get()
        if book_name:
            self.books.append(book_name)
            self.listbox.insert(tk.END, book_name)
            self.book_name.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a book name.")

    def delete_book(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
            self.books.pop(index)
        except:
            messagebox.showwarning("Warning", "Please select a book to delete.")

    def show_book(self, event):
        try:
            index = self.listbox.curselection()[0]
            selected_book = self.listbox.get(index)
            self.book_name.delete(0, tk.END)
            self.book_name.insert(tk.END, selected_book)
        except:
            pass

    def update_book(self):
        try:
            index = self.listbox.curselection()[0]
            new_name = self.book_name.get()
            self.books[index] = new_name
            self.listbox.delete(index)
            self.listbox.insert(index, new_name)
        except:
            messagebox.showwarning("Warning", "Please select a book to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagement(root)
    root.mainloop()
