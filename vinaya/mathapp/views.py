from django.shortcuts import render

def rectarea(request):
    context = {
        'area': "0",
        'l': "0",
        'b': "0"
    }

    if request.method == 'POST':
        l = request.POST.get('length', '0')
        b = request.POST.get('breadth', '0')

        # Convert to integers and calculate area
        area = int(l) * int(b)

        # Update values in context
        context['area'] = area
        context['l'] = l
        context['b'] = b

    return render(request, 'mathapp/math.html', context)
