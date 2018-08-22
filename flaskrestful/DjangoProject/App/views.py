from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView

from App.models import Student


def hello(request):
    return HttpResponse("Hello")


class StudentView(View):

    msg = None

    def get(self, request):
        print(self.msg)
        return render(request, "Student.html")

    def post(self, request):
        return HttpResponse("Post Ok")


class StudentTemplateView(TemplateView):
    # template_name = 'Student.html'
    pass


class StudentListView(ListView):

    template_name = 'StudentList.html'

    model = Student


@csrf_exempt
def login(request):

    if request.method == "GET":

        return render(request, 'login.html')
    elif request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        return HttpResponse(username + password)


def do_login(request):

    username = request.POST.get("username")

    password = request.POST.get("password")

    return HttpResponse(username + password)