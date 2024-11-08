from django.conf import settings

def domain_name(request):
    domain = 'localhost:8000'
    return {'domain': domain}