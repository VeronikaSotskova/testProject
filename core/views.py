from django.db.models import Count, Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from core.models import Product, Lesson
from core.serializers import ChangeStatusSerializer, ProductSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()

    @action(detail=True, methods=['patch'])
    def change_status(self, request, *args, **kwargs):
        lesson = self.get_object()
        serializer = ChangeStatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.validated_data.get('user_id')

        exists_user_in_lesson = lesson.users.filter(id=user_id).exists()
        if not exists_user_in_lesson:
            lesson.users.add(user_id)
            return Response()

        raise APIException('')


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.annotate(
            lesson_count=Count(
                'lessons',
                filter=Q(lessons__users=self.request.user),
                distinct=True
            )
        )
