from app.api.v1 import student_routes, auth_routes, teacher_routes, parents_routes
from app.api.v1 import attendance_routes, exam_routes, fee_routes, notification_routes

__all__ = [
    "student_routes",
    "auth_routes",
    "teacher_routes",
    "parents_routes",
    attendance_routes,
    exam_routes,
    fee_routes,
    notification_routes
]
