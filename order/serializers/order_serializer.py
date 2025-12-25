from rest_framework import serializers
from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    produc_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total
    
    class Meta:
        model = Order
        fields = ['product', 'product_id', 'total', 'user']
        extra_kwargs ={'product' : {'require': False}}
    
    def create(self, validated_data):
        product_data = validated_data.pop('product_id', [])
        user_data = validated_data.pop('user', None)

        order = Order.object.create(user=user_data)
        for product in product_data:
            order.prduct.add(product)
        return order