from django.urls import path
from .views import Error, Home, Login, Register, Logout, AddPhone, ListPhone, AboutUs, ContactUs, Privacy

urlpatterns = [
    
    # 404 ERROR PAGE
    path('ERROR', Error.as_view(), name="error"),

    # HOME PAGE
    path('', Home.as_view(), name="homepage"),

    # USER AUTHENTICATION & REGISTRATION
    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register"),
    path('logout/', Logout.as_view(), name="logout"),

    path('addphone/', AddPhone.as_view(), name="add_phone"),
    path('listphone/', ListPhone.as_view(), name="list_phone"),

    path('aboutus/', AboutUs.as_view(), name="about_us"),
    path('contactus/', ContactUs.as_view(), name="contact_us"),
    path('privacy/', Privacy.as_view(), name="privacy"),

]
