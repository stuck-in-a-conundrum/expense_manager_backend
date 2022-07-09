from django.db.models.fields import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework import mixins
from rest_framework import response
from rest_framework.response import Response
from .serializers import *
from .models import Expenses
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class ExpensesGetList(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Expenses.objects.all()
    def get(self, request):
        expenses=Expenses.objects.filter(owner=request.user)
        serializer=ExpenseSerializer(expenses,many=True)
        response=[]
        for i in serializer.data:
            expenses = Expenses.objects.get(id=i['id'])
            response.append({
                'id': expenses.id,
                'title': expenses.title,
                'creator': expenses.owner.username,
                'created':expenses.created,
                'amount': expenses.amount,
            })
        return Response(response,status=status.HTTP_200_OK)

class ExpenseDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ExpenseSerializer
    queryset = Expenses.objects.all()
    lookup_field = 'id'
    def put(self, request, id=None):
        try:
            expenses = Expenses.objects.get(id__exact=id)
        except:
            return Response({"Expenses with the following id does not exist"}, status=status.HTTP_404_NOT_FOUND)
        queryset = Expenses.objects.filter(Q(owner=request.user))
        x = False
        for expense in queryset:
            if expense == expenses:
                x = True
        if x:
            return self.update(request, id)
        else:
            return Response({"You dont have permission to edit/view this expenses"}, status=status.HTTP_403_FORBIDDEN)

    def get(self, request, id=None):
        try:
            expenses = Expenses.objects.get(id__exact=id)
        except:
            return Response({"Expenses with the following id does not exist"} , status=status.HTTP_404_NOT_FOUND)

        response=[]
        if expenses.owner==request.user:
            response.append({
                'id': expenses.id,
                'title': expenses.title,
                'created':expenses.createdTime,
                'amount': expenses.amount,
            })
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({"You dont have permission to view this expense"}, status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, id):
        try:
            expenses = Expenses.objects.get(id__exact=id)
        except:
            return Response({"Expenses with the following id does not exist"}, status=status.HTTP_404_NOT_FOUND)
        queryset = Expenses.objects.filter(Q(owner=request.user))
        x = False
        for expense in queryset:
            if expense == expenses:
                x = True
        if x:
            return self.destroy(request, id)
        else:
            return Response({"You dont have permission to delete this expense"}, status=status.HTTP_403_FORBIDDEN)


class ExpenseCreateView(generics.GenericAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # uncomment the above line to check in postman
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ExpenseCreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id = serializer.save()
        return Response({
            "id": id,
        }, status=status.HTTP_201_CREATED)



class SavingsGetList(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Savings.objects.all()
    def get(self, request):
        savings=Savings.objects.filter(owner=request.user)
        serializer=ExpenseSerializer(savings,many=True)
        response=[]
        for i in serializer.data:
            savings = Savings.objects.get(id=i['id'])
            response.append({
                'id': savings.id,
                'title': savings.title,
                'creator': savings.owner.username,
                'created':savings.created,
                'amount': savings.amount,
            })
        return Response(response,status=status.HTTP_200_OK)

class SavingDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = SavingSerializer
    queryset = Savings.objects.all()
    lookup_field = 'id'
    def put(self, request, id=None):
        try:
            savings = Savings.objects.get(id__exact=id)
        except:
            return Response({"Savings with the following id does not exist"}, status=status.HTTP_404_NOT_FOUND)
        queryset = Savings.objects.filter(Q(owner=request.user))
        x = False
        for saving in queryset:
            if saving == savings:
                x = True
        if x:
            return self.update(request, id)
        else:
            return Response({"You dont have permission to edit/view this saving"}, status=status.HTTP_403_FORBIDDEN)

    def get(self, request, id=None):
        try:
            savings = Savings.objects.get(id__exact=id)
        except:
            return Response({"Saving with the following id does not exist"} , status=status.HTTP_404_NOT_FOUND)

        response=[]
        if savings.owner==request.user:
            response.append({
                'id': savings.id,
                'title': savings.title,
                'created': savings.createdTime,
                'amount': savings.amount,
            })
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({"You dont have permission to view this saving"}, status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, id):
        try:
            savings = Savings.objects.get(id__exact=id)
        except:
            return Response({"saving with the following id does not exist"}, status=status.HTTP_404_NOT_FOUND)
        queryset = Savings.objects.filter(Q(owner=request.user))
        x = False
        for saving in queryset:
            if saving == savings:
                x = True
        if x:
            return self.destroy(request, id)
        else:
            return Response({"You dont have permission to delete this expense"}, status=status.HTTP_403_FORBIDDEN)


class SavingCreateView(generics.GenericAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # uncomment the above line to check in postman
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = SavingCreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id = serializer.save()
        return Response({
            "id": id,
        }, status=status.HTTP_201_CREATED)
        
        
        
        
