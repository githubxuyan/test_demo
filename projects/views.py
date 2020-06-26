from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import json

from .models import Projects
from django.db import connection

def index_page(request):
    if request.method == 'GET':
        return HttpResponse('<h1>GET 杰克克真帅</h1>')
    elif request.method == 'POST':
        return HttpResponse('<h1>POST 杰克克真帅</h1>')


# 类视图 类模型
class IndexPage(View):
    def get(self, request):
        # 一、创建（C）
        # 1、使用模型类对象来创建
        # 会创建一个Projects模型类对象，但是还未提交
        # project_obj = Projects(name='哈哈哈', leader='噢嚯')
        # 需要调用模型对象的save()方法，去提交
        # project_obj.save()
        # 2、可以使用查询集的create方法
        # objects是manager对象，用于对数据进行操作
        # 使用模型类.objects.create()方法，无需调用save方法
        # project_obj = Projects.objects.create(name='杰克克天下第一', leader='噢嚯1')

        # 二、更新（U）
        # 1、先获取模型类对象，然后修改某些字段，再调用save方法保存
        # project_obj = Projects.objects.get(id=1)
        # project_obj.name = '杰克克天下第一'
        # project_obj.save()

        # 2、可以使用模型类名.objects.filter(字段名=值).update(字段名=修改的值)
        # one = Projects.objects.filter(id=1).update(name='杰克克天下第111')

        # 三、删除（D）
        # 1、使用模型对象.delete()
        # project_obj = Projects.objects.get(id=4)
        # one = project_obj.delete()

        # 四、查询（C）
        # 使用objects管理器来查询
        # 1、get方法
        # a.一般只能使用主键或者唯一键作为查询条件
        # b.get方法如果查询的记录为空和多条记录，那么会抛出异常
        # c.返回的模型类对象，会自动提交
        # project_obj = Projects.objects.get(id=8)

        # Projects.objects.filter(name='杰克克天下第一')
        # Projects.objects.filter()
        # Projects.objects.exclude()
        return HttpResponse('<h1>GET 别说了！花姐最美</h1>'.format('pk'))

    def post(self, request):
        data = json.loads(request.body, encoding='utf-8')
        return HttpResponse('<h1>post {}真帅</h1>'.format(data['name']))

    def put(self, request):
        a_dict = '{"name":"杰克克","msg":"长得很帅"}'
        return HttpResponse(a_dict, content_type='application/json', status=500)
