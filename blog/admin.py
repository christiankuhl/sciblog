from django.contrib import admin
from blog.models import Post
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor_uploader.fields import RichTextUploadingField

class ExtendedPostForm(forms.ModelForm):
    content = RichTextUploadingField()
    class Meta:
        model = Post
        fields = "__all__"

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               	{'fields': ['title']}),
        ('Description',			{'fields':['meta_description']}),
        ('Keywords', 			{'fields':['keywords']}),
        ('Author(s)', 			{'fields':['authors']}),
        ('Date information', 	{'fields': ['pub_date']}),
        ('Abstract',			{'fields': ['abstract']}),
        ('Site', 				{'fields': ['site']}),
        ('Post with formulas',	{'fields': ['has_latex_formula']}),#if true, mathjax.js is included in template (better for SEO)
        ('Content',     		{'fields': ['content']}),
        ('Slug',                {'fields': ['slug']}),
    ]
    prepopulated_fields = {'slug': ('title',)} # new
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']
    form = ExtendedPostForm
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class ExtendedFlatPageForm(FlatpageForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = FlatPage
        fields = "__all__"

class ExtendedFlatPageAdmin(FlatPageAdmin):
    form = ExtendedFlatPageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites', )}),
    )

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, ExtendedFlatPageAdmin)
admin.site.register(Post, PostAdmin)
