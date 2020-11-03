from rest_framework.routers import DefaultRouter
from django.urls import path, include
from employee_app import views
from rest_framework_nested import routers


router1 = routers.SimpleRouter()
router1.register(r'organization', views.OrganizationViewSet)

organization_router = routers.NestedSimpleRouter(
    router1, r'organization', lookup='organization')
organization_router.register(
    r'department', views.DepartmentViewSet, basename='organization-department')


router = DefaultRouter()
# router.register(r'department', views.DepartmentViewSet)
router.register(r'designation', views.DesignationViewSet)
router.register(r'employee', views.EmployeeViewSet)
# router.register(r'organization', views.OrganizationViewSet)
router.register(r'userprofile', views.UserProfileViewSet)

'''
url creation in backend when usig routers
path(r'department/', department_list, name='department-list'),
path(r'department/<int:pk>/', department_detail, name='department-detail)'
'''

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router1.urls)),
    path('', include(organization_router.urls)),
]
