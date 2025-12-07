# Ex.05 Design a Website for Server Side Processing
## Date: 8.12.2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<!DOCTYPE html>
<html>
<head>
    <title>Area of Rectangle</title>
    <style>
        body{
            font-size: 20px;
            background-color: blue;
        }
        .formelt{
            color: orange;
            text-align: center;
            margin-top: 7px;
            margin-bottom: 6px;
        }
        h1{
            color: rgb(255, 0, 179);
            text-align: center;
            padding-top: 20px;
        }
        .box{
            width: 400px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
</head>

<body>
    <div class="box">
        <h1>Area of a Rectangle</h1>

        <form method="POST">
            {% csrf_token %}

            <div class="formelt">
                Length : <input type="text" name="length" value="{{ l }}"> (in m)
            </div>

            <div class="formelt">
                Breadth : <input type="text" name="breadth" value="{{ b }}"> (in m)
            </div>

            <div class="formelt">
                <input type="submit" value="Calculate">
            </div>

            <div class="formelt">
                Area : <input type="text" name="area" value="{{ area }}"> m<sup>2</sup>
            </div>

        </form>
    </div>
</body>
</html>

views.py

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

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL to open the rectangle area page
    path('areaofrectangle/', views.rectarea, name='areaofrectangle'),

    # Root URL for the same function (optional)
    path('', views.rectarea, name='areaofrectangle_root'),
]
```
## SERVER SIDE PROCESSING:
![alt text](<vinaya/vinaya/Screenshot 2025-12-07 230143.png>)


## HOMEPAGE:
![alt text](<vinaya/vinaya/Screenshot 2025-12-07 225758.png>)


## RESULT:
The program for performing server side processing is completed successfully.
