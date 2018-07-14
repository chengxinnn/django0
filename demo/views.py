from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import datetime
# Create your views here.
def index(request):
    context = {}
    string = "我是解鑫睿"
    context['string'] = string
    mylist = ['C++','Java','HTML','CSS','hello']
    context['alist'] = mylist
    dirc = {'name':'xxr','school':'shanxidaxue','age':'23'}
    context['dirc'] = dirc
    List = map(str, range(100))  # 一个长度为100的 List
    context['List'] = List
    return render(request, 'index.html', context=context)

def detail(reuqest, p_id):
    return HttpResponse('Detial  page {}'.format(p_id))

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    return HttpResponse('the num is {}'.format(int(a) + int(b)))

def add2(request,a=0, b=0):
    c = int(a) + int(b)
    return HttpResponse('the num is {}'.format(c))

def type(request):
    return render(request,'type_test.html')

def typetest(request):
    # request.encoding = 'utf-8'  # 设置请求的编码格式
    # print('-----------------html----------------')
    # print("request's path :" + request.path)  # 请求的路径
    # print("full path :" + request.get_full_path())  # 请求的全路径全路径，会包含url传值的内容,和get传值的内容
    # print("host name :" + request.get_host())  # 请求的主机名
    # print("is https? :" + request.is_secure().__str__())  # 是否是https连接？
    # print("is Ajax request? :" + request.is_ajax().__str__())  # 是否是Ajax请求？
    # print("port number :" + request.get_port())  # 请求的端口号
    # return HttpResponse(status=200)  # 返回一个响应成功的状态码
    print("all request post values:-------------------")
    for key in request.POST:
        print(key + "  " + request.POST[key])
    if request.POST:
        print("第一个文本输入框     :",request.POST["text_input1"])
        print("包含默认值的文本输入框:",request.POST['text_input2'])
        print("第三个文本输入框     :", request.POST['text_input3'])

        print('获取到的密码为       :',request.POST['password'])
        print('性别               :',request.POST['radiobtn'])
        print('数值的选择          :',request.POST['radiobtnn'])

        # check_box_list = request.POST['car']
        # if request.POST.has_key('car'):
        #     print('有car')
        # if check_box_list:
        #     print('拿到的复选框数据:    ')
        #     for value in check_box_list.split(','):
        #         print(value)
        print('学校               :',request.POST['school'])
    return HttpResponse(status=200)