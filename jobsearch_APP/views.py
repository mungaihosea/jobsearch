from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout as logout_user
from .models import Skill, Project, Education, Interest, Experience
from django.db.models import Q

def homepage(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('re_password'):
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            re_password = request.POST.get('re_password')
            if password == re_password:
                user = User()
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                user.set_password(password)
                user.save()
        else:
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                user = User.objects.get(email = email)
                print("user found")
                if user.check_password(password):
                    login(request, user)
                    print("user logged in")
                    if user.is_superuser:
                        print("user is suuperuser")
                        return redirect('admin_dash')
                    else:
                        return redirect('dashboard')
                else:
                    context["error_msg"] = 'incorrect details entered'
            except:
                context["error_msg"] = 'incorrect details entered'
        
    return render(request, 'homepage.html', context)

def contact(request):
    return render(request, 'contact.html', {})

def admin_dashboard(request):
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query").split()
        search_results = []

        for x in search_query:
            for user in User.objects.all():
                if user.skill_set.filter(skill__contains = x).count() > 0:
                    search_results.append(user)
        search_queryset = list(set(search_results))
        return render(request, 'search_results.html', {"search_queryset": search_queryset})
    if request.method == 'POST':
        print(request.POST)
    context = {}
    return render(request, 'admin_dash.html', context)

def dashboard(request):
    context = {}
    return render(request, "dashboard.html", context)

def logout(request):
    logout_user(request)
    return redirect('homepage')

def profile(request):
    return render(request, 'profile.html', {})

def resume(request, user_id):
    user = User.objects.get(id = user_id)
    skill_queryset = user.skill_set.all()
    project_queryset = user.project_set.all()
    interest_queryset = user.interest_set.all()
    education_queryset = user.education_set.all()
    experience_queryset = user.experience_set.all()
    context = {
        "skill_queryset":skill_queryset,
        "project_queryset":project_queryset,
        "interest_queryset":interest_queryset,
        "education_queryset":education_queryset,
        "experience_queryset":experience_queryset,
    }
    return render(request, 'resume.html', context)

def skills(request):
    if request.GET.get("delete"):
        try:
            skill = Skill.objects.get(id = request.GET.get("delete"))
            skill.delete()
            return redirect('skills')
        except:
            return redirect('skills')
    if request.method == 'POST':
        if request.POST.get("skill"):
            print(request.POST)
            skill = Skill()
            skill.skill = request.POST.get("skill")
            skill.user = request.user
            skill.save()
            return redirect('skills')
    return render(request, 'cv/skills.html', {"skill_queryset" : request.user.skill_set.all()})

def interests(request):
    if request.GET.get("delete"):
        try:
            interest = Interest.objects.get(id = request.GET.get("delete"))
            interest.delete()
            return redirect('interests')
        except:
            return redirect('interests')
    if request.method == 'POST':
        if request.POST.get("interest"):
            print(request.POST)
            interest = Interest()
            interest.interest = request.POST.get("interest")
            interest.user = request.user
            interest.save()
            return redirect('interests')
    return render(request, 'cv/interests.html', {"interest_queryset" :request.user.interest_set.all()})

def education(request):
    if request.GET.get("delete"):
        try:
            education = Education.objects.get(id = request.GET.get("delete"))
            education.delete()
            return redirect('educations')
        except:
            return redirect('education')
    if request.method == 'POST':
        if request.POST.get("course"):
            print(request.POST)
            education = Education()
            education.course = request.POST.get("course")
            education.institution = request.POST.get("institution")
            education.since = request.POST.get("since")
            education.to = request.POST.get("till")
            education.user = request.user
            education.save()
            return redirect('education')
    return render(request, 'cv/education.html', {"education_queryset" : request.user.education_set.all()})

def experience(request):
    if request.GET.get("delete"):
        try:
            experience = Experience.objects.get(id = request.GET.get("delete"))
            experience.delete()
            return redirect('experience')
        except:
            return redirect('experience')
    if request.method == 'POST':
        if request.POST.get("company"):
            print(request.POST)
            experience = Experience()
            experience.company = request.POST.get("company")
            experience.job_title = request.POST.get("job_title")
            experience.since = request.POST.get("since")
            experience.to = request.POST.get("till")
            experience.user = request.user
            experience.save()
            return redirect('experience')
    return render(request, 'cv/experience.html', {"experience_queryset" : request.user.experience_set.all()})

def projects(request):
    if request.GET.get("delete"):
        try:
            project = Project.objects.get(id = request.GET.get("delete"))
            project.delete()
            return redirect('projects')
        except:
            return redirect('projects')
    if request.method == 'POST':
        if request.POST.get("project"):
            print(request.POST)
            project = Project()
            project.link = request.POST.get("project")
            project.user = request.user
            project.save()
            return redirect('projects')
    return render(request, 'cv/projects.html', {"project_queryset" : request.user.project_set.all()})