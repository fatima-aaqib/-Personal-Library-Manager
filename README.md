
# 📚 Personal Library Manager

Welcome to the **Personal Library Manager**, a web-based application built with Python and Streamlit that helps you manage your book collection effortlessly. Whether you're an avid reader or just starting your reading journey, this app allows you to add, remove, search, and track your books with ease.

---

## 🌟 Features

- **Add Books**: Add new books to your library with details like title, author, publication year, genre, and read status.
- **Remove Books**: Remove books from your library with just a few clicks.
- **Search Books**: Search for books by title or author.
- **Display All Books**: View all books in your library in a clean and organized format.
- **Library Statistics**: Get insights into your reading habits with statistics like total books and percentage read.
- **Save and Load Library**: Automatically save your library to a file and load it when you restart the app.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Streamlit library

### Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/your-username/personal-library-manager.git
   cd personal-library-manager
   ```

2. **Install the required libraries**:
   ```bash
   pip install streamlit
   ```

3. **Run the app**:
   ```bash
   streamlit run library_manager_web.py
   ```

4. **Access the app**:
   - Open your browser and go to `http://localhost:8501`.
   - Start managing your library!

---

## 🖥️ How to Use

1. **Add a Book**:
   - Fill in the book details (title, author, year, genre, and read status).
   - Click "Add Book" to save it to your library.

2. **Remove a Book**:
   - Select a book from the dropdown menu.
   - Click "Remove Book" to delete it from your library.

3. **Search for a Book**:
   - Choose to search by title or author.
   - Enter the search term and click "Search" to find matching books.

4. **Display All Books**:
   - View all books in your library in a neatly formatted list.

5. **Display Statistics**:
   - Check the total number of books and the percentage of books you've read.

6. **Save and Exit**:
   - Click "Exit" in the sidebar to save your library and close the app.

---

## 🛠️ File Structure

```
personal-library-manager/
│
├── library_manager_web.py  # Main Streamlit app file
├── library.txt             # File to store library data
├── README.md               # Project documentation
└── requirements.txt        # List of dependencies
```

---

## 📂 File Handling

- The app automatically saves your library to a file named `library.txt` when you exit.
- The library is loaded from the same file when you restart the app.

---

## 🧑‍💻 Technologies Used

- **Python**: The core programming language used for the app.
- **Streamlit**: A powerful library for building web apps with Python.
- **File Handling**: Used to save and load library data.

---


## 🙏 Acknowledgments

- Thanks to **Streamlit** for making it easy to build web apps with Python.
- Inspired by book lovers everywhere who want to organize their reading journey.

---

