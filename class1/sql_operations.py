import pymysql
from .models import  Bookinfo

def insert(book_id, book_name, book_author, book_price, book_house, book_number, book_type):
    conn = pymysql.Connect(host='localhost', user="root", passwd="123456", db="books", charset="utf8")
    cursor = conn.cursor()

    new_book = Bookinfo(
        book_id, book_name, book_author, book_price, book_house, book_number, book_type
    )
    new_book.save()
    return 0