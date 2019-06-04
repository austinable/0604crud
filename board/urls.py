from board import views
from django.urls import path

urlpatterns = [
    path('post/', views.post, name='post'), #글쓰기
    path('<int:board_id>/', views.detail, name='detail'), #글 상세보기
    path('show/', views.show, name='show'), #전체 글 보기
    path('<int:pk>/edit/', views.edit, name='edit'), #폼수정
    path('<int:pk>/delete/', views.delete, name='delete'), #삭제
]