from app.api.v1.endpoints import student_routes
from app.api.v1.endpoints import auth_routes
from app.api.v1.endpoints import teacher_routes
from app.api.v1.endpoints import parents_routes
from app.api.v1.endpoints import notification_routes
from app.api.v1.endpoints import fee_routes
from app.api.v1.endpoints import exam_routes
from app.api.v1.endpoints import attendance_routes



__all__ = [
    "student_routes",
    "auth_routes",
    "teacher_routes",
    "parents_routes",
    notification_routes,
    fee_routes,
    exam_routes,
    attendance_routes

]
