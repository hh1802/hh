from django.conf.urls import url

from app import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register(r'^api/student',views.api_student)
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^head/', views.head, name='head'),
    url(r'^left/', views.left, name='left'),
    url(r'^grade', views.grade, name='grade'),
    url(r'^student/', views.student, name='student'),
    url(r'^addgrade/', views.addgrade, name='addgrade'),
    url(r'^addstu/', views.addstu, name='addstu'),
    url(r'^delstu/', views.delstu, name='delstu'),
    url(r'edgrade/', views.edgrade, name='edgrade'),
    url(r'^query/', views.query, name='query')
]

urlpatterns += router.urls