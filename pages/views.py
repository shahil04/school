from django.views.generic import TemplateView

class Homepage(TemplateView):
    template_name='index.html'

class About(TemplateView):
    template_name='about.html'

class Blog_signal(TemplateView):
    template_name='blog-single.html'

class Blog(TemplateView):
    template_name='blog.html'

class Contact(TemplateView):
    template_name='contact.html'

class Courses(TemplateView):
    template_name='courses.html'

class Pricing(TemplateView):
    template_name='pricing.html'

class Teacher(TemplateView):
    template_name='teacher.html'