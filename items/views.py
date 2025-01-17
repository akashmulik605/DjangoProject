
# items/views.py
from django.shortcuts import render, redirect
from django.db import connection
from .models import Item



# Create an Item (using raw SQL query)
def create_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO items_item (name, description, price) VALUES (%s, %s, %s)", 
                [name, description, price]
            )
        return redirect('list_items')
    return render(request, 'items/create_item.html')

# Read all Items (using raw SQL query)
def list_items(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM items_item")
        items = cursor.fetchall()
    return render(request, 'items/list_items.html', {'items': items})

# Update an Item (using raw SQL query)
def update_item(request, item_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM items_item WHERE id = %s", [item_id])
        item = cursor.fetchone()

    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        
        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE items_item SET name = %s, description = %s, price = %s WHERE id = %s", 
                [name, description, price, item_id]
            )
        return redirect('list_items')
    
    return render(request, 'items/update_item.html', {'item': item})

# Delete an Item (using raw SQL query)
def delete_item(request, item_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM items_item WHERE id = %s", [item_id])
    return redirect('list_items')
