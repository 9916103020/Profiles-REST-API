from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView (extract or inout selected data"""

    name = serializers.CharField(max_length=10)

