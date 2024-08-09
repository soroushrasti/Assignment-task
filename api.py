from fastapi import FastAPI, HTTPException

app = FastAPI()

books_db = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# TODO: Implement update_book function to update an existing book's details
# It should return the updated book, or raise a 404 if the book is not found
@app.put("/books/{book_id}")
async def update_book(book_id: int, book_data: dict):
    pass  # Implementation is missing

# TODO: Write a unit test for the update_book function
