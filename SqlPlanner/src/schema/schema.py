# schema/schema.py

SCHEMA = {
    "Brand": {
        "columns": ["brand_id", "brand_name", "category"],
        "primary_key": "brand_id"
    },
    "Product": {
        "columns": ["product_id", "brand_id", "product_name", "sku", "unit_price"],
        "primary_key": "product_id",
        "foreign_keys": {
            "brand_id": "Brand.brand_id"
        }
    },
    "Region": {
        "columns": ["region_id", "region_name", "country"],
        "primary_key": "region_id"
    },
    "Customer": {
        "columns": ["customer_id", "customer_name", "customer_type", "region_id"],
        "primary_key": "customer_id",
        "foreign_keys": {
            "region_id": "Region.region_id"
        }
    },
    "Sales": {
        "columns": [
            "sales_id", "product_id", "customer_id",
            "sale_date", "quantity", "revenue"
        ],
        "primary_key": "sales_id",
        "foreign_keys": {
            "product_id": "Product.product_id",
            "customer_id": "Customer.customer_id"
        }
    }
}
