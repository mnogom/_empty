"""Views."""

import random

from rest_framework.views import APIView
from rest_framework.response import Response


class RandomSequenceView(APIView):
    """Random sequence View."""

    def get(self, request, *args, **kwargs):
        """This is test function. Returns random sequence. Max length - 10."""

        count = int(request.GET.get('count', 10))
        count = 10 if count > 10 else count
        random_range = {i: random.randint(0, 100) for i in range(1, count + 1)}
        return Response(random_range)
