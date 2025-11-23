import random
import string
from datetime import datetime

def generate_sku(product_name, category=None):
    """Generate a unique SKU for a product"""
    prefix = category.slug[:3].upper() if category else 'PRO'
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    timestamp = datetime.now().strftime('%m%d')
    return f"{prefix}-{random_chars}-{timestamp}"

def calculate_discount_percentage(original_price, sale_price):
    """Calculate discount percentage"""
    if original_price and sale_price and original_price > sale_price:
        return int(((original_price - sale_price) / original_price) * 100)
    return 0