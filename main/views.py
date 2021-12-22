from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        masuk1= int(request.POST['Tabungan Awal'])
        masuk2= int(request.POST['Bunga'])
        masuk3= int(request.POST['Lama'])
        keluar=((masuk2/100)*(masuk3/12)*masuk1)+masuk1
        context = {'keluar': keluar,
                   }
        return render(request, 'main/home.html', context)

    else:
        return render(request, 'main/home.html', {})

