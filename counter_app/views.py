from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    return render(request,'index.html')

def destroy(request):
    request.session.clear()
    return redirect('/')

def plus_two(request):
    request.session['counter'] += 1
    return redirect('/')

def num(request):
    num_from_form = request.POST['num']
    num = num_from_form
    request.session['counter'] += int(num)-1

    return redirect('/')