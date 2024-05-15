from rest_framework import serializers
from .models import Blog,Category

class BlogSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField('get_category_name')
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'category','category_name']

    def get_category_name(self, obj):
        return obj.category.name
