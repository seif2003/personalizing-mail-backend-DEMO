from django.http import JsonResponse
from .models import EmailTemplate
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def save_template(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        subject = data.get('subject')
        body = data.get('body')
        template_pk = 1

        try:
            template = EmailTemplate.objects.get(pk=template_pk)
            template.subject = subject
            template.body = body
            template.save()
            return JsonResponse({'message': 'Template updated successfully'})
        except EmailTemplate.DoesNotExist:
            template = EmailTemplate(subject=subject, body=body)
            template.save()
            return JsonResponse({'error': 'Template saved successfully'})

    else:
        return JsonResponse({'error': 'Invalid request'})

@csrf_exempt
def get_template(request):
    template_pk = 1

    try:
        template = EmailTemplate.objects.get(pk=template_pk)
        return JsonResponse({'subject': template.subject, 'body': template.body})
    except EmailTemplate.DoesNotExist:
        return JsonResponse({'error': 'Template does not exist'})