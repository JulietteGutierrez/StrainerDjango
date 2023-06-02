def importe_total_carrito(request):
    total=0
    # if request.user.is_authenticated:

    # mientras terminamos la autenticacion, le ponemos un try / except para que no explote
    # despues cuando ande el if de is_authenticated volamos el try / except
    try:
        for key, value in request.session["carrito"].items():
            total=total+float(value["precio"])
    except:
        total=0

    return{"importe_total_carrito": total}