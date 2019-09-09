from django.views.generic import DetailView
from django.http import HttpResponse

from issue_page.models import Issue


class IssueView(DetailView):
    context_object_name = 'issue'
    model = Issue
    pk_url_kwarg = 'issue_slug'
    template_name = 'issue_detail.html'


def get_info(request):
    html = "<html>helloworld</html>"
    return HttpResponse(html)


def send_message(request):
    html = "<html>helloworld</html>"
    return HttpResponse(html)