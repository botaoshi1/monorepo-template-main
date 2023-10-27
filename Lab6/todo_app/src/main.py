# Install fastapi, uvicorn, pytest, pytest-cov
from fastapi import FastAPI, Body

app = FastAPI()

# Create a GET ReST API
@app.get("/api")
def get_msg():
    return {"msg": "hello_world"}

# Create a GET ReST API with path parameters
@app.get("/books/{path_param}")
def get_path(path_param: str):
    return {"msg": path_param}

# Create a GET ReST API with query parameters
@app.get("/books/")
def get_para(title: str):
    return {"msg": title}

# Create a GET ReST API with path parameters AND query parameters
@app.get("/books/{path_param}/")
def get_path_para(path_param: str, title: str = None):
    return{"msg1": path_param, "msg2": title}

# Create a POST ReST API
@app.post("/books/create_book")
def post_book(new_book=Body()):
    return {"msg": new_book}

books = {
    1: {"name": "Book1", "author": "Author1"},
    2: {"name": "Book2", "author": "Author2"}
}

# Create a PUT ReST API
@app.put("/books/update_book")
def update_book(id: int, book=Body()):
    if id in books:
        books[id] = book
        return {'msg': book}
    else:
        return {'msg': "Not found"}

# Create a DELETE ReST API
@app.delete("/books/delete_book")
def delete_book(id: int):
    if id in books:
        del books[id]
        return {'msg': 'Deleted'}
    else:
        return {'msg': "Not found"}
    