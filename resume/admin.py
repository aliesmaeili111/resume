from django.contrib import admin
from resume.models import Skills,SocialNetwork,Portfolio,Contact,CaseStudy

# Register your models here.

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):

    
    list_display = ('name','persent_skill')
    list_display_links = ('name','persent_skill')
    list_filter = ('name','persent_skill')
    search_fields =  ['name']
    list_per_page = 10


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    
    list_display = ('name_project','thumbnail_tag','template')
    list_display_links = ('name_project','thumbnail_tag')
    list_filter = ('name_project','template')
    search_fields =  ['name_project']
    list_per_page = 10



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    
    list_display = ('name','email')
    list_display_links = ('name','email')
    list_filter = ('name','email')
    search_fields =  ['name','email','subject']
    list_per_page = 10

@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):

    
    list_display = ('social_network','link')
    list_display_links = ('social_network','link')
    list_filter = ('social_network','link')
    search_fields =  ['social_network']
    list_per_page = 10

@admin.register(CaseStudy)
class CaseStudykAdmin(admin.ModelAdmin):
    list_display = ('title','portfolio','thumbnail_logo')
    list_display_links = ('title','portfolio')
    list_filter = ('title','portfolio')
    search_fields =  ['title']
    list_per_page = 10

