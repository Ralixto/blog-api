from rest_framework import serializers
from .models import Category, Post, Comment, User

class CategorySerialiser(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'post_count']

class PostSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'category', 'created_at', 'updated_at', 'published']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

class CommentSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', "password2"]