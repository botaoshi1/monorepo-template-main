import pytest
from fastapi.testclient import TestClient

from ..src.main import app

client = TestClient(app)

def test_get_msg():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello_world"}

def test_get_path():
    response = client.get("/books/book1")
    assert response.status_code == 200
    assert response.json() == {"msg": "book1"}

def test_get_para():
    response = client.get("/books/?title=book2")
    assert response.status_code == 200
    assert response.json() == {"msg": "book2"}

def test_get_path_para():
    response = client.get("/books/book3/?title=book4")
    assert response.status_code == 200
    assert response.json() == {"msg1": "book3", "msg2": "book4"}

def test_post_book():
    new_book = {"name": "New Book", "author": "Author Name"}
    response = client.post("/books/create_book", json=new_book)
    assert response.status_code == 200
    assert response.json() == {"msg": new_book}

def test_update_existing_book():
    book_id = 1
    updated_book = {"name": "Updated Book", "author": "New Author"}
    response = client.put(f"/books/update_book?id={book_id}", json=updated_book)
    assert response.status_code == 200
    assert response.json() == {"msg": updated_book}

def test_update_non_existent_book():
    book_id = 3
    updated_book = {"name": "Updated Book", "author": "New Author"}
    response = client.put(f"/books/update_book?id={book_id}", json=updated_book)
    assert response.status_code == 200
    assert response.json() == {"msg": "Not found"}

def test_delete_existing_book():
    book_id = 2
    response = client.delete(f"/books/delete_book?id={book_id}")
    assert response.status_code == 200
    assert response.json() == {"msg": "Deleted"}
 
def test_delete_non_existent_book():
    book_id = 3
    response = client.delete(f"/books/delete_book?id={book_id}")
    assert response.status_code == 200
    assert response.json() == {"msg": "Not found"}
