from django.shortcuts import render


# Create your views here.
def exam3(request):
    context = {'number': 5}
    return render(request, 'exam3.html', context)

def homework2(request):
    return render(request, 'homework2.html')

def main(request):
    return render(request,'main.html')

def exam15(request):
    return render(request, 'exam15.html')
