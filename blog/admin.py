from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status','created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
    
    
# Register your models here.

@admin.register(Comment)  # Replace your admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'body')
    actions = ['approve_comments', 'disapprove_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f'{queryset.count()} comments were approved successfully.')
    
    approve_comments.short_description = "Approve selected comments"
    
    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)
        self.message_user(request, f'{queryset.count()} comments were disapproved successfully.')
    
    disapprove_comments.short_description = "Disapprove selected comments"
