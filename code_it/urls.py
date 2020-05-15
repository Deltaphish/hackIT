from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='code_it'),
	path('<slug:id>/', views.detail, name='code_it_detail'),
	path('answer',views.validate_answer, name="code_it_validate"),
	path('reset',views.reset, name='code_it_reset'),
]