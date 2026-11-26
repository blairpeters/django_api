from rest_framework import serializers
from myapp.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'#it gets all the fields but you can also specify eg ["id","name"]
        #you can also instead use exclude = ['created_at', 'updated_at']
        #TODO: add custom validations