from rest_framework import serializers


class VideoDetailSerializer(serializers.Serializer):
    page = serializers.CharField(required=True)
    page_size = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'

class AddVideoSerializer(serializers.Serializer):

    class Meta:
        fields = '__all__'