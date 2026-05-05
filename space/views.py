from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SpacePost, Category

# 1. Bosh sahifa (home_view) - Mana shu funksiya senda yetishmayotgan edi
def home_view(request):
    assignments = SpacePost.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'assignments': assignments})

# 2. Profil sahifasi
@login_required
def s_dashboard(request):
    assignments = SpacePost.objects.all().order_by('-created_at')
    return render(request, 'dashboard.html', {'assignments': assignments})

# 3. Topshiriq qo'shish
@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        answer = request.POST.get('correct_answer')
        image = request.FILES.get('image')
        
        category, _ = Category.objects.get_or_create(name="Topshiriqlar")

        if title and content and answer:
            SpacePost.objects.create(
                author=request.user,
                title=title,
                content=content,
                correct_answer=answer,
                image=image,
                category=category
            )
            return redirect('student_dashboard')
            
    return render(request, 'create_post.html')

# 4. Topshiriqni yechish
@login_required
def solve_assignment(request, pk):
    assignment = get_object_or_404(SpacePost, pk=pk)
    message = None
    status = None 

    if request.method == "POST":
        user_answer = request.POST.get('user_answer', '')
        if user_answer.strip().lower() == assignment.correct_answer.strip().lower():
            message = "Topshiriq muvaffaqiyatli topshirildi!"
            status = "success"
        else:
            message = "Xato! Qaytatdan urinib ko'ring."
            status = "danger"

    return render(request, 'solve.html', {
        'assignment': assignment, 
        'message': message, 
        'status': status
    })