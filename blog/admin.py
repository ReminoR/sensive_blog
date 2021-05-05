from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('likes', )


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', )
    list_display = ('author', 'text', )

admin.site.register(Comment, CommentAdmin)
