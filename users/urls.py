from django.urls import path
from .views import UserRegistrationView,UserLoginView,UserWithProfile,AuthUserView,RegisterAdmin
from rest_framework.routers import SimpleRouter

router  = SimpleRouter()
router.register('users',UserWithProfile)

delete__detail = UserWithProfile.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

list_all = UserWithProfile.as_view({
    'get':'list'
})

# router.register('admin_user',RegisterAdmin)

urlpatterns = [

     path('register',UserRegistrationView.as_view()),
     path('login',UserLoginView.as_view()),
     path('me',AuthUserView.as_view()),
     path('register_admin',RegisterAdmin.as_view()),
 ]
urlpatterns += router.urls
 