from rest_framework import serializers

from core.models import User, Product


class ChangeStatusSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(write_only=True, required=True)

    def validate_id(self, value):
        if User.objects.filter(id=value).exists():
            return value
        raise serializers.ValidationError('User does not exist')


class ProductSerializer(serializers.ModelSerializer):
    lesson_count = serializers.IntegerField(read_only=True, default=0)

    class Meta:
        model = Product
        fields = '__all__'
