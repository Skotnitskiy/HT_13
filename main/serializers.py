from rest_framework import serializers

from main.models import Category
from askstories.models import Askstories
from newstories.models import Newstories
from jobstories.models import Jobstories
from showstories.models import Showstories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class AskstoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Askstories
        fields = ('__all__')


class NewstoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newstories
        fields = ('__all__')


class JobstoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobstories
        fields = ('__all__')


class ShowstoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showstories
        fields = ('__all__')