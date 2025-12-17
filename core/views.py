from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.utils import timezone
from django.utils.timezone import localtime
from .models import WorkRecord, Task
from django.utils.dateparse import parse_datetime

# --------------------
# ログアウト
# --------------------
def logout_view(request):
    logout(request)
    messages.success(request, "ログアウトしました。")
    return redirect('login')


# --------------------
# ダッシュボード
# --------------------
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')

    today_record = WorkRecord.objects.filter(
        user=request.user,
        start_time__date=timezone.now().date()
    ).first()

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'today_record': today_record,
    })


# --------------------
# 出勤
# --------------------
@login_required
def clock_in(request):
    WorkRecord.objects.create(
        user=request.user,
        start_time=timezone.now()
    )
    return redirect('dashboard')


# --------------------
# 退勤
# --------------------
@login_required
def clock_out(request):
    record = WorkRecord.objects.filter(
         user=request.user,
         start_time__date=timezone.now().date()
    ).first()

    if record and not record.end_time:
        record.end_time = timezone.now()
        record.save()

    return redirect('dashboard')


# --------------------
# タスク追加
# --------------------
@login_required
def add_task(request):
    title = request.POST.get('title')
    if title:
        Task.objects.create(user=request.user, title=title)
    return redirect('dashboard')


# --------------------
# タスク完了
# --------------------
@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.is_done = True
    task.save()
    return redirect('dashboard')


# --------------------
# 勤務編集
# --------------------
@login_required
def edit_attendance(request, pk):
    record = get_object_or_404(WorkRecord, pk=pk, user=request.user)

    if request.method == 'POST':
        start = request.POST.get('start_time')
        end = request.POST.get('end_time')

        if start:
            record.start_time = parse_datetime(start)
        if end:
            record.end_time = parse_datetime(end)

        record.save()
        return redirect('attendance_history')

    return render(request, 'core/edit_attendance.html', {
        'record': record,
    })


# --------------------
# 勤務履歴
# --------------------
@login_required
def attendance_history(request):
    records = WorkRecord.objects.filter(
        user=request.user
    ).order_by('-created_at')

    history_list = []
    for r in records:
        start = r.start_time
        end = r.end_time
        work_duration = None

        if start and end:
            work_duration = localtime(end) - localtime(start)

        history_list.append({
            'record': r,
            'start': localtime(start) if start else None,
            'end': localtime(end) if end else None,
            'duration': work_duration,
        })

    return render(request, 'core/attendance_history.html', {
        'history': history_list,
    })
