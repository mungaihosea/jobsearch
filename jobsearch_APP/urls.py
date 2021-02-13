from django.urls import path
from .views import homepage, contact, admin_dashboard, dashboard, logout, profile, resume, skills, interests, education, experience, projects

urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('contact/', contact, name = 'contact'),
    path('admin_dash/', admin_dashboard, name = "admin_dash"),
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', logout, name="logout"),
    path('profile/', profile, name="profile"),
    path('resume/<slug:user_id>/', resume, name="resume"),
    path('skills/', skills, name="skills"),
    path('interests/', interests, name="interests"),
    path('education/', education, name="education"),
    path('experience/', experience, name="experience"),
    path('projects/', projects, name="projects"),
]