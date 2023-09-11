from django.shortcuts import render
from resume.models import Skills,SocialNetwork,Portfolio,CaseStudy
from resume.forms import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():

            contact_form.save()
            messages.success(request,'پیام شما ثبت شده بزودی با شما تماس خواهیم گرفت','success')
    else:
        contact_form = ContactForm()
        messages.error(request,' پیام شما ارسال نشد لطفا دوباره سعی کنید','danger')

    
    skills_5 = Skills.objects.all()[:5]
    skills_10 = Skills.objects.all()[5:10]

    social = SocialNetwork.objects.all()

    portfolio = Portfolio.objects.all()
    caseStudy = CaseStudy.objects.all()

    context = {
        'skills_5':skills_5,
        'skills_10':skills_10,
        'social':social,
        'portfolio':portfolio,

        "form":contact_form,
        "case":caseStudy,
    }
    return render(request,'resume/home.html',context)
