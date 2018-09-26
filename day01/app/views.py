from django.core.paginator import Paginator
from django.db.models import Q, F
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from rest_framework import mixins, viewsets

from app.filters import StudentFilter
from app.models import Grade, Student
from app.serializer import StudentSerializer


class api_student(mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_class = StudentFilter

    def get_queryset(self):
    #     query = self.queryset
    #     s_name = self.request.query_params.get('s_name')
    #     return query.filter(s_name__contains=s_name)
        return self.queryset

    def perform_destroy(self, instance):
        instance.delete = True
        instance.save()


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


"""
头部页面
"""


def head(request):
    if request.method == 'GET':
        return render(request, 'head.html')


def left(request):
    if request.method == 'GET':
        return render(request, 'left.html')


# def grade(request):
#     if request.method == 'GET':
#         ctx ={'grade':Grade.objects.all()}
#         return render(request, 'grade.html', ctx)


"""
显示班级信息
"""


def student(request):
    # if request.method == 'GET':
    #     page_num = request.GET.get('page_num', 1)
    #     stu_list=Student.objects.all().filter(delete=False)
    #     paginator = Paginator(stu_list, 3)
    #     pages = paginator.page(int(page_num))
    #     return render(request, 'student.html',{'stu_list':stu_list,'pages':pages})
    return render(request, 'student_ajax.html')


"""添加班级信息"""


def addgrade(request):
    if request.method == 'GET':
        return render(request, 'addgrade.html')
    if request.method == 'POST':
        g_name = request.POST['grade_name']
        Grade.objects.create(g_name=g_name)
        return HttpResponseRedirect(reverse('app:grade'))


"""添加学生"""

def addstu(request):
    if request.method == 'GET':
        ctx = {'grades': Grade.objects.all()}
        return render(request, 'addstu.html', ctx)
    if request.method == 'POST':
        s_name = request.POST.get('s_name')
        g_id = request.POST.get('g_id')
        s_img = request.FILES.get('s_img')
        grade = Grade.objects.filter(id=g_id).first()
        Student.objects.create(s_name=s_name, g_id=grade.id, s_img=s_img)
        return HttpResponseRedirect(reverse('app:student'))

def grade(request):
    if request.method == 'GET':
        page_num = request.GET.get('page_num', 1)
        grades = Grade.objects.all()
        paginator = Paginator(grades, 3)
        pages = paginator.page(int(page_num))
        return render(request, 'grade.html', {'grades':grades, 'pages':pages})


def delstu(request):
    if request.method == 'GET':
        id = request.GET.get('s_id')
        Student.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('app:student'))

def edgrade(request):
    if request.method =='GET':
        grade_id = request.GET.get('grade')
        return render(request, 'addgrade.html',{'grade_id':grade_id})

    if request.method =='POST':
        grade_id = request.POST.get('grade_id')
        grade_name = request.POST.get('grade_name')
        g = Grade.objects.filter(pk=grade_id).first()
        g.g_name = grade_name
        g.save()
        return HttpResponseRedirect(reverse('app:grade'))



"""查询学生成绩信息"""
def query(request):
    if request.method == 'GET':
        grade = Grade.objects.filter(g_name='python').first()
        students = grade.student_set.all()
        stu1 = students.filter(sy__gte=F('ss') + 10)
        stu = students.filter(Q(sy__gte=80) | Q(ss__lte=80))
        # for i in stu:
        #     print(i.s_name)
        for i in stu1:
            print(i.s_name)

    return HttpResponse('123')
