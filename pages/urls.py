from django.urls import path
from . import views

urlpatterns=[
    path('',views.Homepage.as_view(),name='home'),
    path('about/',views.About.as_view(),name='about'),
    path('blog_signal/',views.Blog_signal.as_view(),name='blog_signal'),
    path('blog/',views.Blog.as_view(),name='blog'),
    path('contact/',views.Contact.as_view(),name='contact'),
    path('courses/',views.Courses.as_view(),name='courses'),
    path('pricing/',views.Pricing.as_view(),name='pricing'),
    path('teacher/',views.Teacher.as_view(),name='teacher'),
]