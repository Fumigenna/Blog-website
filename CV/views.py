from django.http import HttpResponse
from django.template import loader



def pdf_view(request):
    with open('CV/static/cv/CV - Irina Orzan.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
    pdf.closed