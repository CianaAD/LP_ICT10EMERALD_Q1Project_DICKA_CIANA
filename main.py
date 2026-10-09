from pyscript import display, document # type: ignore

def SKU_generator(e):
    document.getElementById('sku_output').innerHTML = " "
    category = document.getElementById('category').value
    product_name = document.getElementById('product_name').value
    stock_qty = document.getElementById('quantity').value
    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)
    display("SKU: " + sku, target='sku_output')

def create_order(e):
    p1 = 200   # Truffle Pasta
    p2 = 180   # Alfredo Pasta
    p3 = 160   # Lasagna
    p4 = 140   # Carbonara
    p5 = 130   # Pesto Pasta
    p6 = 100   # Spaghetti with Meat Sauce
    p7 = 25    # Iced Tea
    p8 = 25    # Fanta
    p9 = 25    # Coca Cola
    p10 = 20   # Water
   
    q1 = float(document.getElementById("item1").value or 0)
    q2 = float(document.getElementById("item2").value or 0)
    q3 = float(document.getElementById("item3").value or 0)
    q4 = float(document.getElementById("item4").value or 0)
    q5 = float(document.getElementById("item5").value or 0)
    q6 = float(document.getElementById("item6").value or 0)
    q7 = float(document.getElementById("item7").value or 0)
    q8 = float(document.getElementById("item8").value or 0)
    q9 = float(document.getElementById("item9").value or 0)
    q10 = float(document.getElementById("item10").value or 0)

  
    subtotal = (p1q1 + p2q2 + p3q3 + p4q4 + p5q5 + p6q6 + p7q7 + p8q8 + p9q9 + p10q10) # type: ignore

    tax_rate = 0.12 # 12% VAT
    tax = subtotal * tax_rate
    total = subtotal + tax

    receipt = f"""==== Receipt ====
Subtotal: ₱{subtotal:.2f}
Tax: ₱{tax:.2f}
Total: ₱{total:.2f}
"""

    document.getElementById("show").innerText = receipt