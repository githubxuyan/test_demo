from django.http import HttpResponse, JsonResponse
from django.db import connection
from django.views import View
from .models import Projects
from interface.models import Interface
import json


class IndexPage(View):
    # 需要能获取到项目的列数数据（获取多条项目数据或者所有数据）
    def get(self, request):
        from django.forms.models import model_to_dict
        data_list = []
        project_obj = Projects.objects.all()
        for item in project_obj:
            data_list.append(model_to_dict(item))
        return JsonResponse({"code": "200", "msg": "success", "data": data_list})

    # 能够创建项目（创建一个项目）
    def post(self, request):
        request_data = json.loads(request.body)
        Projects.objects.create(**request_data)
        return JsonResponse({"code": "200", "msg": "success"})

    # 能够更新项目（只更新某一个项目）
    def put(self, request):
        request_data = json.loads(request.body)
        # Projects.objects.filter(id=request_data['id']).update(name='某某优秀的项目')
        project_obj = Projects.objects.get(id=request_data['id'])
        project_obj.name = request_data['name']
        project_obj.leader = request_data['leader']
        project_obj.save()
        return JsonResponse({"code": "200", "msg": "success"})

    # 能够删除项目（只删除某一个项目）
    def delete(self, request):
        request_data = json.loads(request.body)
        Projects.objects.get(id=request_data['id']).delete()
        return JsonResponse({"code": "200", "msg": "删除成功"})

class GetPage(View):
    # 需要能获取到项目的详情数据（获取前端指定某一条数据）
    def get(self, request, pk):
        if type(pk) == type(1):
            if Projects.objects.filter(id=pk).exists():
                project_obj = Projects.objects.values().get(id=pk)
                data = json.dumps(project_obj)
                return HttpResponse(data, content_type="application/json,charset=utf-8")
            else:
                return JsonResponse({"code": 201, "msg": "项目不存在"})
        else:
            return JsonResponse({"code": 202, "msg": "请输入整数"})