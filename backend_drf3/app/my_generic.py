from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


class MyGenericRetrieveUpdateDestroy(views.APIView):
    model=None
    serializer_class=None

    def get_object(self,pk):
        return get_object_or_404(self.model,pk=pk)

    def get(self,request,pk,*args,**kwargs):
        serializer=self.serializer_class(instance=self.get_object(pk))
        return Response(serializer.data)

    def put(self,request,pk,*args,**kwargs):
        serializer=self.serializer_class(instance=self.get_object(pk),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)

    def delete(self,request,pk,*args,**kwargs):
        self.get_object(pk).delete()
        return Response(status=204)
