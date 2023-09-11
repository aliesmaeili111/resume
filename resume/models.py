from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.html import format_html


# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=50,unique=True,help_text='لطفا مهارت خود را اضافه کنید',verbose_name='نام مهارت')
    persent_skill = models.PositiveIntegerField(default=0,help_text='درصد مهارت خود راانتخاب کنید',verbose_name="درصد مهارت",validators=[MinValueValidator(0),MaxValueValidator(100)])


    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'
        ordering = ['-name']

    def __str__(self):
        return self.name
    
class Portfolio(models.Model):

    CHOICE_PROJECT = (
        ('app','اپ'),
        ('web','وبسایت'),
    )

    template = models.CharField(max_length = 10,blank=True,null=True,choices = CHOICE_PROJECT,verbose_name='قالب پروژه',help_text='لطفا یک قالب را انتخاب کنید')
    name_project = models.CharField(max_length=50,unique=True,help_text='لطفا اسم پروژه خود را اضافه کنید',verbose_name='نام پروژه')
    image_project = models.ImageField(upload_to='images_projects',verbose_name='تصویر پروژه',help_text='لطفا یک تصویر برای پروژه خود انتخاب کنید')
    description = models.TextField(verbose_name='توضیحات پروژه',help_text='درباره پروژه چیزی بنویسید')

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کار ها'
        ordering = ['-name_project']

    def __str__(self):
        return self.name_project
    
    def thumbnail_tag(self):
        return format_html("<img src='{}' width=70px hieght=70px style='border-radius:10px'; >".format(self.image_project.url))
    thumbnail_tag.short_description = "تصویر پروژه"
    

class Contact(models.Model):
    name = models.CharField(max_length=35,help_text="لطفا نام و نام خانوادگی خود را وارد کنید",verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل",help_text="ایمیل خود را وارد کنید")
    subject = models.CharField(max_length=35,help_text='لطفا موضوعی برای ارتباط با ما بنویسید',verbose_name='موضوع ارتباط')
    context = models.TextField(verbose_name='محتوا',help_text='متن مورد نظر خود را وارد کنید')
    
    class Meta:
        verbose_name = "مخاطب"
        verbose_name_plural = "مخاطبان"
        
    def __str__(self):
        return self.name
    


    

class SocialNetwork(models.Model):
    CHOICE_NAME = (
        ('telegram','تلگرام'),
        ('instagram','اینستاگرام'),
        ('linkedin','لینکدین'),
        ('whatsapp','واتساپ')
    )
    
    social_network = models.CharField(max_length = 10,choices = CHOICE_NAME,verbose_name='شبکه های اجتماعی',help_text="لطفا شبکه های اجتماعی خود را انتخاب کنید")
    link = models.URLField(unique=True,verbose_name='لینک شبکه های اجتماعی',help_text='لینک شبکه های خود را وارد کنید')

        
    class Meta:
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه اجتماعی من"

        
    def __str__(self):
        return self.social_network


class CaseStudy(models.Model):
    portfolio = models.OneToOneField(Portfolio,on_delete=models.CASCADE,verbose_name='کیس استادی نمونه کار',help_text='لطفا یک کیس استادی برای نمونه کار های خود انتخاب کنید')
    logo = models.ImageField(upload_to='image_logo_portfolio',verbose_name='لوگو پروژه',help_text='لطفا یک لوگو برای پروژه خود انتخاب کنید')
    title = models.CharField(max_length=35,help_text="لطفا عنوان کیس استادی خود را وارد کنید",verbose_name="عنوان کیس استادی")
    description = models.TextField(verbose_name='توضیحات پروژه',help_text='لطفا توضیحات کوتاهی درباره پروژه خود بنویسید')
    link_case_study =  models.URLField(null=True,blank=True,unique=True,verbose_name='لینک کیس استادی',help_text='لینک کیس استادی خود را وارد کنید')



    class Meta:
        verbose_name = " کیس استادی"
        verbose_name_plural = "کیس استادی های نمونه کار ها"

        
    def __str__(self):
        return self.title
    
    def thumbnail_logo(self):
        return format_html("<img src='{}' width=70px hieght=70px style='border-radius:10px'; >".format(self.logo.url))
    thumbnail_logo.short_description = "لوگو پروژه"
    