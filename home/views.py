from django.shortcuts import render

def search(request):
    category = request.GET.get("query")
    if category:
        return redirect("searchresults", category=category)
    print(category)


def searchresults(request, category):

    return 
# Create your views here.
def home(request):
    return render(request, 'home/index.html')