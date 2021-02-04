from django.urls import path

from Products.views import AllProduct, ProductDetails, AddtoCart, AddProduct, AddtoCartView

urlpatterns = [
    path('product/',AllProduct.as_view()),
    path('product/<int:pk>/',ProductDetails.as_view()),
    path('addtocart/',AddtoCart.as_view()),
    path('addproduct/',AddProduct.as_view()),
    path('viewcart/',AddtoCartView.as_view()),

]