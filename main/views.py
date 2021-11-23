from django.shortcuts import render

def animal_view(request, animal_id):
    return render(request, 'animal.html', {'id': animal_id})

def all_animal_view(request):
    print(request)
    return render(request, 'animals.html')


# Create your views here.
