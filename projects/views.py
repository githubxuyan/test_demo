from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import json


def index_page(request):
    if request.method == 'GET':
        return HttpResponse('<h1>GET 杰克克真帅</h1>')
    elif request.method == 'POST':
        return HttpResponse('<h1>POST 杰克克真帅</h1>')


class IndexPage(View):
    def get(self, request):
        return HttpResponse('<h1>GET 杰克克真帅</h1>')

    def post(self, request):
        data = json.loads(request.body, encoding='utf-8')
        return HttpResponse('<h1>post {}真帅</h1>'.format(data['name']))

    def put(self, request):
        return HttpResponse('<h1>put 杰克克真帅</h1>')
