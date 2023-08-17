from django.shortcuts import render
from rest_framework import viewsets
from entities.serializer import ClientSerializer, ProductSerializer, InventorySerializer, BranchSerializer
from entities.models import Client, Branch, Product, Inventory

# Create your views here.


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer