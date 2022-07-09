
from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import Expenses, Savings

class ExpenseCreateSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        data= self.validated_data
        owner = self.context['request'].user
        title = data['title']
        amount=data['amount']
        created=data['created']
        expense = Expenses.objects.create(owner=owner, title=title,created=created,amount=amount)
        return expense.id

    class Meta:
        model = Expenses
        fields = ('id', 'title','created','amount',)


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ('id', 'title','created','amount')


class SavingCreateSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        data= self.validated_data
        owner = self.context['request'].user
        title = data['title']
        amount=data['amount']
        created=data['created']
        saving = Savings.objects.create(owner=owner, title=title,created=created,amount=amount)
        return saving.id

    class Meta:
        model = Savings
        fields = ('id', 'title','created','amount',)


class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields = ('id', 'title','created','amount')