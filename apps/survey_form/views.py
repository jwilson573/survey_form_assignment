from django.shortcuts import render, redirect

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
        request.session['name'] = ''
        request.session['language'] = ''
        request.session['dojo'] = ''
        request.session['comment'] = ''
    elif 'count' in request.session:
        request.session['count'] = request.session['count'] + 1
    return render(request, "survey_form/index.html")

def results(request):
    contents = {
        'name': request.session['name'],
        'language': request.session['lang'],
        'dojo': request.session['dojo'],
        'comment': request.session['comment'],
        'count': request.session['count'],
        
    }
    return render(request, "survey_form/results.html",contents)

def create_user(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['lang'] = request.POST['lang']
        request.session['dojo'] = request.POST['dojo']
        request.session['comment'] = request.POST['comment']
        print request.session['name']
        print request.session['lang']
        print request.session['dojo']
        print request.session['comment']
        return redirect('/results')
    else:
        return redirect('/')

def reset(request):
    request.session['name'] = ''
    request.session['lang'] = ''
    request.session['dojo'] = ''
    request.session['comment'] = ''
    request.session['count'] = 0

    return redirect('/')
    

