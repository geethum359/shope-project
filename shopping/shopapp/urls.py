
from django.urls import path,include
from shopapp import views

urlpatterns = [

    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('product_details/<int:pk>',views.productDetails.as_view(),name='product_details'),
    path('category/<val>',views.categoryView.as_view(),name="category"),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/',views.cart, name='cart'),
    
    
]