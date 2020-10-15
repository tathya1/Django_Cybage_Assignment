from rest_framework.routers import DefaultRouter
from django.urls import path, include
from employee_app import views

router = DefaultRouter()
router.register(r'department', views.DepartmentViewSet)
router.register(r'designation', views.DesignationViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'organization', views.OrganizationViewSet)
router.register(r'userprofile', views.UserProfileViewSet)

'''
url creation in backend when usig routers
path(r'department/', department_list, name='department-list'),
path(r'department/<int:pk>/', department_detail, name='department-detail'
'''

urlpatterns = [
    path('', include(router.urls)),
]
