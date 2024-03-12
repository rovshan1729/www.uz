from rest_framework import serializers 
from .models import Category, SubCategory, ScoreBoard

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
        )


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = SubCategory
        fields = (
            'id',
            'title',
            'created_at',
            'updated_at',
            'category',

        )

class ScoreBoardSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer()

    class Meta:
        model = ScoreBoard
        fields = (
            'subcategory',
            'id',
            'title',
            'is_tasix',
            'visitors',
            'views',
            'rating',
            'created_at',
            'updated_at',
        )
        
class RecentlyAddedSerializer(serializers.ModelSerializer):
    subcategory = serializers.StringRelatedField()
    class Meta:
        model = ScoreBoard
        fields = (
            'subcategory',
            'id',
            'title',
            'created_at',
            'updated_at',
        )
