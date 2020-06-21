from django.http import HttpResponse


def index_page(request):

    return HttpResponse('<h1>杰克克真帅</h1>')

