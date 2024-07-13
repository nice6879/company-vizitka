from django.shortcuts import render, redirect

from .models import Company, Hodimlar, Portfolio, Murojaat
from .forms import MurojaatForm

def home(request):
    company = Company.objects.all()
    portfolio = Portfolio.objects.all()
    hodimlar = Hodimlar.objects.all()
    return render(request, 'base.html', context={"company":company, "portfolio":portfolio, "hodimlar":hodimlar})


def murojaat(request):
    if request.method == 'POST':
        form = MurojaatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  
    form = MurojaatForm()
    return render(request, 'murojaat.html', {'form': form})