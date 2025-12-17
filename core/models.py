

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class WorkCategory(models.Model):
    """作業分類（例：開発、調査、会議など）"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """タグ（例：優先、急ぎ、資料作成）"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class WorkLog(models.Model):
    """作業ログ本体"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # 作業分類（1つ選択）
    category = models.ForeignKey(WorkCategory, on_delete=models.SET_NULL, null=True)

    # タグ（複数つけられる）
    tags = models.ManyToManyField(Tag, blank=True)

    # 日付・時間
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    # 自動記録系
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"


# 出勤退勤の記録
class WorkRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.date()}"


# タスク管理
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

