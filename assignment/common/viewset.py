from rest_framework.response import Response
from rest_framework import status, viewsets


def standard_response(data=[], status_code=200, error_message="", results=None, **kwargs, ):
    response_data = {
        'status_code': status_code,
        'error_message': error_message,
        'results': data,
    }
    if (results):
        response_data.update(results)
    return Response(response_data, status=status_code)


class StandardResponseViewSet(viewsets.ModelViewSet):
    """
    統一回應格式的基類視圖
    """

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return standard_response(response.data, status_code=response.status_code)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return standard_response(response.data, status_code=response.status_code)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        results = self.get_serializer(instance).data  # 序列化當前對象數據
        super().destroy(request, *args, **kwargs)
        kwargs_results = kwargs.get('results')
        if (kwargs_results):
            results = {**results, **kwargs_results}
        # 注意：如果使用 `destroy`，可能返回的內容是空的，需根據需求自定義
        return standard_response(results, status_code=status.HTTP_200_OK,)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return standard_response(response.data, status_code=response.status_code)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return standard_response(response.data, status_code=response.status_code)

    def response(self, request, data, status_code, **kwargs):
        return standard_response(data, status_code,)
