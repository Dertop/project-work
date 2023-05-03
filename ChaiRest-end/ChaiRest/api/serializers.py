from rest_framework import serializers

from api.models import User, Category, Furniture, Order


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    email = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CategorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category

    def update(self, instance, validated_data):
        instance.id = instance.id
        instance.title = validated_data.get('title', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
