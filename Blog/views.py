from django.http import HttpResponse
from django.template import loader

def index_blog(request):
    from .models import BlogEntry

    all_entries = BlogEntry.objects.all().order_by('-entryDate')
    count = BlogEntry.objects.count()
    template = loader.get_template('blog/index.html')
    context = {
        'all_entries': all_entries,
        'count': count
    }

    return HttpResponse(template.render(context, request))
