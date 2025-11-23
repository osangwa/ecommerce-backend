from rest_framework import serializers
from .models import Order, OrderItem, OrderStatusHistory
from apps.users.serializers import AddressSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'product_name', 'product_sku', 'quantity', 'unit_price', 'subtotal')

class OrderStatusHistorySerializer(serializers.ModelSerializer):
    created_by_email = serializers.EmailField(source='created_by.email', read_only=True)
    
    class Meta:
        model = OrderStatusHistory
        fields = ('id', 'status', 'notes', 'created_by_email', 'created_at')

class OrderListSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    can_cancel = serializers.ReadOnlyField()
    
    class Meta:
        model = Order
        fields = (
            'id', 'order_number', 'user_email', 'status', 'payment_status', 
            'total_amount', 'can_cancel', 'created_at'
        )

class OrderDetailSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    shipping_address = AddressSerializer(read_only=True)
    billing_address = AddressSerializer(read_only=True)
    status_history = OrderStatusHistorySerializer(many=True, read_only=True)
    can_cancel = serializers.ReadOnlyField()
    
    class Meta:
        model = Order
        fields = (
            'id', 'order_number', 'user_email', 'status', 'payment_status',
            'payment_method', 'subtotal', 'tax_amount', 'shipping_cost',
            'discount_amount', 'total_amount', 'shipping_address',
            'billing_address', 'items', 'status_history', 'notes',
            'tracking_number', 'shipped_at', 'delivered_at', 'cancelled_at',
            'cancellation_reason', 'can_cancel', 'created_at', 'updated_at'
        )

class CreateOrderSerializer(serializers.Serializer):
    shipping_address_id = serializers.IntegerField()
    billing_address_id = serializers.IntegerField()
    payment_method = serializers.CharField(max_length=50)
    notes = serializers.CharField(required=False, allow_blank=True)