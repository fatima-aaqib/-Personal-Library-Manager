import streamlit as st # type: ignore

# File to save and load library data
LIBRARY_FILE = "library.txt"

# Initialize session state to store the library
if 'library' not in st.session_state:
    st.session_state.library = []

# Function to load library from a file
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            for line in file:
                title, author, year, genre, read_status = line.strip().split(",")
                book = {
                    "title": title,
                    "author": author,
                    "year": int(year),
                    "genre": genre,
                    "read_status": read_status == "True"
                }
                st.session_state.library.append(book)
        st.success("Library loaded from file.")
    except FileNotFoundError:
        st.warning("No library file found. Starting with an empty library.")

# Function to save library to a file
def save_library():
    with open(LIBRARY_FILE, "w") as file:
        for book in st.session_state.library:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['genre']},{book['read_status']}\n")
    st.success("Library saved to file.")

# Function to add a book
def add_book():
    st.subheader("Add a Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, max_value=2023, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Have you read this book?")
    
    if st.button("Add Book"):
        if title and author and genre:
            book = {
                "title": title,
                "author": author,
                "year": year,
                "genre": genre,
                "read_status": read_status
            }
            st.session_state.library.append(book)
            st.success("Book added successfully!")
        else:
            st.error("Please fill in all fields.")

# Function to remove a book
def remove_book():
    st.subheader("Remove a Book")
    if st.session_state.library:
        titles = [book["title"] for book in st.session_state.library]
        title_to_remove = st.selectbox("Select a book to remove", titles)
        
        if st.button("Remove Book"):
            for book in st.session_state.library:
                if book["title"] == title_to_remove:
                    st.session_state.library.remove(book)
                    st.success(f"Removed '{title_to_remove}' successfully!")
                    break
    else:
        st.warning("No books in the library to remove.")

# Function to search for a book
def search_book():
    st.subheader("Search for a Book")
    search_by = st.radio("Search by", ["Title", "Author"])
    search_term = st.text_input(f"Enter {search_by}")
    
    if st.button("Search"):
        if search_term:
            matching_books = []
            for book in st.session_state.library:
                if search_by == "Title" and search_term.lower() in book["title"].lower():
                    matching_books.append(book)
                elif search_by == "Author" and search_term.lower() in book["author"].lower():
                    matching_books.append(book)
            
            if matching_books:
                st.write("Matching Books:")
                for book in matching_books:
                    status = "Read" if book["read_status"] else "Unread"
                    st.write(f"- **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
            else:
                st.warning("No matching books found.")
        else:
            st.warning("Please enter a search term.")

# Function to display all books
def display_all_books():
    st.subheader("Your Library")
    if st.session_state.library:
        for i, book in enumerate(st.session_state.library, 1):
            status = "Read" if book["read_status"] else "Unread"
            st.write(f"{i}. **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        st.warning("No books in the library.")

# Function to display statistics
def display_statistics():
    st.subheader("Library Statistics")
    total_books = len(st.session_state.library)
    read_books = sum(book["read_status"] for book in st.session_state.library)
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    st.write(f"Total books: {total_books}")
    st.write(f"Percentage read: {percentage_read:.1f}%")

# Main function to run the Streamlit app
def main():
    st.title("📚 Personal Library Manager")
    st.sidebar.title("Menu")
    
    # Load library at the start
    if not st.session_state.library:
        load_library()
    
    # Menu options
    menu_options = {
        "Add a Book": add_book,
        "Remove a Book": remove_book,
        "Search for a Book": search_book,
        "Display All Books": display_all_books,
        "Display Statistics": display_statistics,
        "Save Library": save_library
    }
    
    choice = st.sidebar.radio("Select an option", list(menu_options.keys()))
    menu_options[choice]()  # Call the selected function
    
    # Save library when the app is closed
    if st.sidebar.button("Exit"):
        save_library()
        st.success("Library saved. Goodbye!")
        st.stop()

# Run the app
if __name__ == "__main__":
    main()
    