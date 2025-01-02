import pytest
from app import add_product, get_products, edit_product, update_product, delete_product, reset_store

def setup_function():
    reset_store()  # Clear store_list before each test

def test_add_product():
    product = add_product("P001", "Product A", 10, 5.0)
    assert product["product_code"] == "P001"
    assert product["product_name"] == "Product A"
    assert product["quantity"] == 10
    assert product["price_per_item"] == 5.0
    assert len(get_products()) == 1

def test_edit_product():
    add_product("P001", "Product A", 10, 5.0)
    product = edit_product("P001")
    assert product["product_code"] == "P001"
    assert product["product_name"] == "Product A"

def test_update_product():
    add_product("P001", "Product A", 10, 5.0)
    updated_product = update_product("P001", "Updated Product A", 20, 10.0)
    assert updated_product["product_name"] == "Updated Product A"
    assert updated_product["quantity"] == 20
    assert updated_product["price_per_item"] == 10.0

def test_delete_product():
    add_product("P001", "Product A", 10, 5.0)
    delete_product("P001")
    assert len(get_products()) == 0

def test_reset_store():
    add_product("P001", "Product A", 10, 5.0)
    reset_store()
    assert len(get_products()) == 0
