from rest_framework import serializers
from .models import Blogs, Comments

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class BlogSerializers(serializers.ModelSerializer):
    comments = CommentSerializers(many=True, read_only=True)
    class Meta:
        model = Blogs
        fields = '__all__'