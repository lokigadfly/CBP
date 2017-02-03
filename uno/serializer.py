from uno.models import Room
from rest_framework import serializers
from django.contrib.auth.models import User

class RoomSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Room
        fields = '__all__'
    # def restore_object(self, attrs, instance=None):
    #     if instance:
    #         instance.title = attrs['name']
    #         instance.name = attrs['name']
    #         instance.creator = attrs['creator']
    #         instance.discription=attrs['description']
    #         instance.choice = attrs['choice']
    #         instance.category = attrs['category']
    #         instance.getsrs = attrs['getsrs']
    #         return instance

    #     return Room(**attrs)   
    def create(self, validated_data):
        return Room(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.name = validated_data.get('name', instance.name)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.discription = validated_data.get('discription', instance.discription)
        instance.choice = validated_data.get('choice', instance.choice)
        instance.category = validated_data.get('category', instance.category)
        instance.getsrs = validated_data.get('getsrs', instance.getsrs)
        
        return instance

class UserSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'