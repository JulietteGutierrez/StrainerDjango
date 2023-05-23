# def importe_total_carrito(request):
#     total=0
#     #if request.user.is_authenticated:
#     for key, value in request.session["carrito"].items():
#         total=total+float(value["precio"])
        
#     return {"importe_total_carrito": total}






def importe_total_carrito(request):
    total=0
    #if request.user.is_authenticated:
    for key, value in request.session["carrito"].items():
        total=total+float(value["precio"])

    return{"importe_total_carrito": total}


#  precio_convert = re.findall(r'\d+\.\d+', value["precio"])
#             total=total+float(precio_convert[0])

# def importe_total_carrito(request):
#     total=0
#     if request.user.is_authenticated:
#         for key, value in request.session["carrito"].items():
#             total=total+(float(value["precio"])*value["cantidad"])
#     return{"importe_total_carrito": total}
