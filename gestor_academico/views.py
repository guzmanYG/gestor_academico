from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Student
from .algorithms import quicksort_students, binary_search_by_matricula
from .structures import Stack
from .utils import build_bst_from_queryset

# Historial en memoria (simple). Para producción se debería persistir.
history = Stack()

def index(request):
    students = Student.objects.all()
    return render(request, 'gestor_academico/index.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula', '').strip()
        nombre = request.POST.get('nombre', '').strip()
        if matricula and nombre:
            s = Student.objects.create(matricula=matricula, nombre=nombre)
            history.push(('add_student', s.matricula))
            return redirect(reverse('index'))
    return render(request, 'gestor_academico/add_student.html')

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'gestor_academico/student_detail.html', {'student': student})

def order_by_average(request):
    students = list(Student.objects.all())
    ordered = quicksort_students(students, key_fn=lambda x: x.promedio())
    return render(request, 'gestor_academico/student_list.html', {'students': ordered})

def search_student(request):
    query = request.GET.get('q', '').strip()
    result = None
    if query:
        sorted_by_mat = list(Student.objects.order_by('matricula'))
        result = binary_search_by_matricula(sorted_by_mat, query)
    return render(request, 'gestor_academico/search.html', {'result': result, 'query': query})

def add_grade(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        try:
            grade = float(request.POST.get('grade'))
            student.notas.append(grade)
            student.save()
            history.push(('add_grade', student.matricula, grade))
            return redirect('student_detail', pk=student.pk)
        except Exception:
            pass
    return render(request, 'gestor_academico/add_grade.html', {'student': student})

def undo_action(request):
    action = history.pop()
    if action:
        kind = action[0]
        if kind == 'add_student':
            _mat = action[1]
            Student.objects.filter(matricula=_mat).delete()
        elif kind == 'add_grade':
            mat = action[1]; grade = action[2]
            s = Student.objects.filter(matricula=mat).first()
            if s and s.notas and s.notas[-1] == grade:
                s.notas.pop()
                s.save()
    return redirect('index')
