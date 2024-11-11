from django.urls import path
from .views import RegisterView, VerifyOTPView, LoginView
from .views import HomePage
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import ProductView
from .views import ProductCreateView
from .views import AddToCartView, UpdateCartItemView, RemoveFromCartView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('VerifyOTP/', VerifyOTPView.as_view(), name='VerifyOTP'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Add this line
    path('homepage/', HomePage.as_view(), name='homepage'),
    path('products/', ProductView.as_view(), name='product_list'),  # For GET (all products) and POST (create new product)
    path('products/<int:pk>/', ProductView.as_view(), name='product_detail'),  # For GET (single product), PUT (update), DELETE
    path('products/', ProductCreateView.as_view(), name='product-create'),
    path("cart/add/", AddToCartView.as_view(), name="add-to-cart"),
    path("cart/update/<int:product_id>/", UpdateCartItemView.as_view(), name="update-cart-item"),
    path("cart/remove/<int:product_id>/", RemoveFromCartView.as_view(), name="remove-from-cart"),
]
