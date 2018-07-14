from django.shortcuts import render
import pymysql
from .models import Bookinfo
from . import models
from django.http import HttpResponse
import json

# Create your views here.

def login(request):
    return render(request, 'login.html')

def main(request):
  msg = {}
  if request.POST:
      if request.is_ajax():
          username = request.POST['username']
          password = request.POST['password']
          user = models.Users.objects.filter(user_name=username,user_password=password)
          if user:
              msg = {'msg':'true'}
              return HttpResponse(status=200,content_type=json,content=json.dumps(msg))
  msg['msg'] = 'false'
  return HttpResponse(status=200, content_type=json, content=json.dumps(msg))







def index(request):
    return render(request,'class1/index.html')

def list_model(request):
    context = {}

    if request.POST:
        query = {}
        query['book_price__gte'] = request.POST['minPrice']
        query['book_price__lte'] = request.POST['maxPrice']

        if request.POST['bookName'] != '':
            query['book_name__contains'] = request.POST['bookName']
        if request.POST['author'] != '':
            query['book_author__icontains'] = request.POST['author']
        if request.POST['bookNum'] != '':
            query['book_number'] = request.POST['bookNum']  # 库存数量
        if request.POST['BookType'] != '':
            query['book_type'] = request.POST['BookType']  # 书籍类型
        if request.POST['BookHouse'] != '':
            query['book_house'] = request.POST['BookHouse']  # 出版社
        books = Bookinfo.objects.filter(**query)  # 查询获取所有的书籍信息
        context['books'] = books  # 传值给模板标签进行渲染

    return render(request,'class1/list.html',context=context)

def list_sql(request):
    conn = pymysql.Connect(host='localhost', user="root",passwd="123456", db="books", charset="utf8")
    cursor = conn.cursor()
    # 动态生成SQL语句
    sql = 'select * from bookinfo where '
    if request.POST :
        # 价位区间
        sql += "Book_Price > " + request.POST['minPrice'] + " AND Book_Price < " + request.POST['maxPrice']
        # 库存数量
        if request.POST['bookNum'] != '':
            sql += " AND Book_Number = " + request.POST['bookNum']
        # 书名关键字，是模糊查询
        if request.POST['bookName'] != '':
            sql += " AND Book_Name like '%" + request.POST['bookName'] + "%' "
        # 作者,模糊查询
        if request.POST['author'] != '':
            sql += " AND Book_Author like '%" + request.POST['author'] + "%' "
        # 书籍类型
        if request.POST['BookType'] != '':
            sql += " AND Book_Type = '" + request.POST['BookType'] + "' "
        # 出版社
        if request.POST['BookHouse'] != '':
            sql += " AND Book_House = '" + request.POST['BookHouse'] + "' "
        sql += ";"
        print('sql'.center(60,'-'))
        print(sql)  # 打印出拼接好的sql语句观察调试
        cursor.execute(sql)  # 执行查询语句
        books = []  # 准备一个图书对象的列表，存放数据库查询返回的所有条目
        books_object_tuple = cursor.fetchall()
        print(books_object_tuple)
        for book_object in books_object_tuple:
            book = Bookinfo(book_object[0],
                            book_object[1],
                            book_object[2],
                            book_object[3],
                            book_object[4],
                            book_object[5],
                            book_object[6],)
            books.append(book)  # 把每一个图书对象放到数组中
        context = {
            'books': books
        }
    return render(request, 'class1/list.html', context=context)



