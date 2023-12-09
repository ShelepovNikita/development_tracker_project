from rest_framework import mixins, viewsets


class ListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Viewset for get response with many objects"""

    pass
