from typing import Any

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from ads.models import Advertisement, Category


# ----------------------------------------------------------------
# Category serializers
class CatListDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for ListView and RetrieveView
    """
    class Meta:
        model: Category = Category
        fields: list[str] = ['name']


class CatCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for CreateView
    """
    id: serializers.IntegerField = serializers.IntegerField(required=False)

    class Meta:
        model: Category = Category
        fields: str = '__all__'

    def create(self, validated_data) -> Any:
        return Category.objects.create(**validated_data)


class CatChangeSerializer(serializers.ModelSerializer):
    """
    Serializer for UpdateView(update and partial update), DeleteView
    """
    class Meta:
        model: Category = Category
        fields: str = '__all__'


# ----------------------------------------------------------------
# Advertisement serializers
class AdListDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for ListView and RetrieveView
    """
    author: serializers.SlugRelatedField = serializers.SlugRelatedField(read_only=True, slug_field='username')
    category: serializers.SlugRelatedField = serializers.SlugRelatedField(read_only=True, slug_field='name')
    locations: SerializerMethodField = SerializerMethodField()

    def get_locations(self, ad) -> list:
        """
        Method to make list of locations
        :param ad: object of advertisement
        :return: list of locations
        """
        return [loc.name for loc in ad.author.locations.all()]

    class Meta:
        model: Advertisement = Advertisement
        fields: list[str] = ['name', 'author', 'price', 'description', 'is_published', 'image', 'category', 'locations']


class AdCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for CreateView
    """
    id: serializers.IntegerField = serializers.IntegerField(required=False)
    image: serializers.ImageField = serializers.ImageField(required=False)
    locations: SerializerMethodField = SerializerMethodField()

    def get_locations(self, ad) -> list:
        """
        Method to make list of locations
        :param ad: object of advertisement
        :return: list of locations
        """
        return [loc.name for loc in ad.author.locations.all()]

    def create(self, validated_data) -> Any:
        """
        Method to create instance of advertisement
        :param validated_data: validated data taken from request.body
        :return:
        """
        return Advertisement.objects.create(**validated_data)

    class Meta:
        model: Advertisement = Advertisement
        fields: str = '__all__'


class AdChangeSerializer(serializers.ModelSerializer):
    """
    Serializer for UpdateView(update and partial update), DeleteView
    """
    class Meta:
        model: Advertisement = Advertisement
        exclude: list[str] = ['id', 'image']
