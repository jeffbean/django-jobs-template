from celery.result import AsyncResult
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework import renderers
from rest_framework.response import Response

from boil_app.models import Node
from boil_app.serializers.models import NodeSerializer


class NodeAPIViewSet(viewsets.ModelViewSet):
    model = Node
    serializer_class = NodeSerializer
    queryset = Node.objects.all()
    renderer_classes = (renderers.JSONRenderer, renderers.BrowsableAPIRenderer, renderers.TemplateHTMLRenderer)


class TokenViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet that for listing or retrieving users.
    """
    model = Token
    lookup_field = 'user_id'


class JobsAPIViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        """ A view to report the progress to the user """
        # TODO: figure out a way to do group results. Same with Chain and such
        # if 'job_type' in request.query_params and request.query_params.get('job_type') == 'group':
        #     job = GroupResult(pk)
        #
        #     if job and job.ready():
        #         return Response(data=
        #                         {
        #                             'id': job.id,
        #                             'results': "{}".format(job.join()),
        #                             'completed_count': job.completed_count(),
        #                         })
        #     else:
        #         return Response(data=
        #                         {
        #                             'id': job.id,
        #                             'results': "",
        #                             'completed_count': job.completed_count(),
        #                         })
        # else:
        job = AsyncResult(pk)
        if job.ready():
            if job.failed():
                # TODO: just return the message of the last traceback exception
                formatted_lines = job.traceback.splitlines()[-1]
                return Response(
                    data={
                        'id': job.id,
                        'result': "{}".format(job.result),
                        'status': job.status,
                        'traceback': formatted_lines
                    }
                )
            else:
                result = job.get()
        else:
            result = None
        return Response(data={'id': job.id, 'result': result, 'status': job.status})


class NodeListView(ListView):
    model = Node


class NodeDetailView(DetailView):
    model = Node
