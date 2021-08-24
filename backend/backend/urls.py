from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

import accounts.views
import tasks.views

router = routers.SimpleRouter()
router.register(r"accounts", accounts.views.AccountViewSet, "Accounts")
router.register(r"tasks", tasks.views.TaskModelView, "Tasks")

answer_router = routers.NestedSimpleRouter(router, r"tasks", lookup="task")
answer_router.register(r"answers", tasks.views.AnswerModelView, "Answers")

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/0.1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/0.1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("api/0.1/", include(router.urls)),
    path("api/0.1/", include(answer_router.urls)),
]
