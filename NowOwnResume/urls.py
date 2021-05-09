from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='Home'),
    path('about',views.aboutus,name='About'),
    path('basictemplate',views.basictemplates,name='Basic'),
    path('sitemap.xml', views.sitemap,name='Sitemap'),
    path('contactus',views.contactus,name='ContactUs'),
    path('home',views.home,name='Home'),
    path('templates',views.templates,name='Templates'),
    path('customized',views.customized,name='Customized'),
    path('donate',views.donate,name='Donate'),
    path('basictemplates',views.basictemplates,name='Basic Template'),
    path('suggestions',views.suggestions,name='Suggestions'),
    path('attractive',views.attractive,name='Attractive Resume'),
    path('softwareEngg',views.softwareEngg,name='Software Engineer'),
    path('basicResume',views.basicResume,name='Basic Resume'),
    path('simpleResume',views.simpleResume,name='Simple Resume'),
    path('download',views.download,name='Download Resume'),
    path('simpleNew',views.simpleNew,name='Simple New Resume'),
    path('simpleNewest',views.simpleNewest,name='Simple Newest Resume'),
    path('preDesigned',views.preDesigned,name='PreDesigned Resume'),

    path('admin7223_login_access-only', views.admin,name='Admin Login'),
    path('admin_login', views.admin, name='Login'),
    path('admin_loggedin', views.admin_loggedin, name='Admin '),
    path('viewSuggesstion', views.admin_suggesstion, name='Admin suggesstion'),
    path('uploadTemplate', views.admin_template, name='Admin templates'),
    path('viewResumes', views.admin_viewresumes, name='Admin view resumes'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
