from django.shortcuts import render
from django.http import HttpResponse

def tasklist(request):
    task = Task.objects.all().order_by('create_at')
    return render(request, 'task/list.html', {'task':tasks})