from django.http import HttpResponse
from django.template import loader


def index(request):
    from .models import BlogEntry

    all_entries = BlogEntry.objects.all()
    print all_entries
    template = loader.get_template('blog/index.html')
    context = {
        'all_entries': all_entries
    }
    return HttpResponse(template.render(context, request))



