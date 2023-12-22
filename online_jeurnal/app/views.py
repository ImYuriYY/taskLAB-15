from django.shortcuts import render, redirect
from .models import *
from .forms import *



def index(request):
    students = Student.objects.all()
    return render(request, 'app/index.html', context={"students": students})



def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            stud = Student()
            stud.name = form.cleaned_data['name']
            stud.surname = form.cleaned_data['surname']
            stud.subj_id = form.cleaned_data['subj']
            stud.score_id = form.cleaned_data['score']
            stud.gpa = form.cleaned_data['gpa']
            stud.save()
            return redirect('homepage')
    form = CreateForm()
    return render(request, 'app/create.html', context={'form': form})




def edit(request, id):
    stud = Student.objects.get(pk=id)
    return render(request, 'app/edit.html', context={'student': stud})




def delete(request, id):
    stud = Student.objects.get(pk=id)
    stud.delete()
    return redirect('homepage')


