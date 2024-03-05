from rest_framework import serializers
from some_models import ExampleModel


class ExampleSerializer(serializers.ModelSerializer):

    """
    Example Serializer
    """

    class Meta:
        model = ExampleModel
        fields = '__all__'
