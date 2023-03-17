from django.shortcuts import render,redirect
def leaderboard(request):
    from leaderboard.models import Person
    if request.method == 'POST':
        query = request.POST.get('search_query')
        if query:
            people = Person.objects.filter(name__icontains=query)
        else:
            people = Person.objects.all()
    else:        
        people = Person.objects.all()
    context = {'people': people}
    return render(request, 'leaderboard.html', context)

