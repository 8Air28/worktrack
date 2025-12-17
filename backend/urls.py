from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # 管理画面
    path('admin/', admin.site.urls),

    # ログイン（ホームもログインへ飛ばす）
    path('', auth_views.LoginView.as_view(
        template_name='core/login.html'
    ), name='login'),
    path('login/', auth_views.LoginView.as_view(
        template_name='core/login.html'
    ), name='login'),

    # ログアウト
    path('logout/', views.logout_view, name='logout'),

    # ダッシュボード
    path('dashboard/', views.dashboard, name='dashboard'),

    # 出退勤
    path('clock_in/', views.clock_in, name='clock_in'),
    path('clock_out/', views.clock_out, name='clock_out'),

    # 勤務履歴
    path('attendance_history/', views.attendance_history, name='attendance_history'),
    path('attendance/edit/<int:pk>/', views.edit_attendance, name='attendance_edit'),

    # タスク
    path('task/add/', views.add_task, name='add_task'),
    path('task/complete/<int:task_id>/', views.complete_task, name='complete_task'),
]
