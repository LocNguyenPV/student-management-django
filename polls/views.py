# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Student
from datetime import datetime
from .forms import InputForm
from django.urls import reverse
from django.http import HttpResponseRedirect
def index(request):
    list_student = Student.objects.filter(is_delete=False).order_by('-register_date')
    context = {'list_student': list_student}
    return render(request, 'polls/index.html', context)

def create(request):
    context ={}
    context['form']= InputForm()
    return render(request, "polls/create.html", context)

def detail(request, registration_number):
    context ={}
    student = get_object_or_404(Student, pk=registration_number)
    context['title'] =  "Edit " + student.name
    context['registration_number'] =  student.registration_number
    edit_form = InputForm(instance=student)
    edit_form.fields['registration_number'].widget.attrs['readonly'] = True
    context['form']= edit_form
    return render(request, 'polls/detail.html', context)

def preview(request, registration_number):
    context ={}
    student = get_object_or_404(Student, pk=registration_number)
    context["student"]=  student
    return render(request, 'polls/preview.html',context)

def edit(request, registration_number):
    try:
        model = get_object_or_404(Student, pk=registration_number)
        model.registration_number = request.POST['registration_number']
        model.name = request.POST['name']
        model.email = request.POST['email']
        model.home_town = request.POST['home_town']
        model.score = request.POST['score']
        model.date_of_birth = request.POST['date_of_birth']
        model.modify_date = datetime.now()
        model.save()
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
        'error_message': "This is not your fault, it is my fault!",
        })
    return HttpResponseRedirect(reverse('polls:index'))

def delete(request, registration_number):
    model = get_object_or_404(Student, pk=registration_number)
    model.is_delete = True
    model.modify_date = datetime.now()
    model.save()
    return HttpResponseRedirect(reverse('polls:index'))

def add(request):
        try:
            model = Student()
            model.registration_number = request.POST['registration_number']
            model.name = request.POST['name']
            model.email = request.POST['email']
            model.home_town = request.POST['home_town']
            model.score = request.POST['score']
            model.date_of_birth = request.POST['date_of_birth']
            model.register_date = datetime.now()
            model.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
        except (KeyError):
            # Redisplay the question voting form.
            return render(request, 'polls/create.html', {
            'error_message': "This is not your fault, it is my fault!",
            })
        return HttpResponseRedirect(reverse('polls:index'))
