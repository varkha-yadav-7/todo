from django.shortcuts import render
from home.models import tasks
from django.http import HttpResponseRedirect

def home(request):
    c=tasks.objects.all()
    d=tasks.objects.all().count()
    incom=tasks.objects.filter(completed=False).count()
    if(d!=0):
        com=d-incom
        per=com/d
        per=per*100
    else:
        com=0
        per=0
        incom=0
    return render(request,'home.html',{'com':int(per),'task':c,'total':d,'complete':com,'incomplete':incom})

def adding(request):
    task=request.POST.get('task')
    s=tasks(taskname=task)
    s.save()
    return HttpResponseRedirect('/home/')

def updating(request):
    task=request.POST.getlist('tick')
    c=tasks.objects.all()
    for i in c:
        i.completed=False
        i.save()
    for i in task:
        s=tasks.objects.get(taskname=i)
        s.completed=True
        s.save()
    return HttpResponseRedirect('/home/')

def deleting(request):
    task=request.GET.get('del')
    c=tasks.objects.get(taskname=task)
    print(c)
    c.delete()
    return HttpResponseRedirect('/home/')

def reset(request):
    tasks.objects.all().delete()
    return HttpResponseRedirect('/home/')
    