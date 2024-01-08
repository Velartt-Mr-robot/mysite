from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
# from django.shortcuts import render, redirect, get_object_or_404

class AdListView(OwnerListView):
    model = Ad
#    def get(self, request):
#        return render(request, 'ads/ad_list.html')


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'text', 'price']


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text', 'price']


class AdDeleteView(OwnerDeleteView):
    model = Ad