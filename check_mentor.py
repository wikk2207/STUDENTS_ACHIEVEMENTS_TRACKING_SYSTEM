from app import create_app
from app.models import User

app = create_app()

with app.app_context():
    user = User.query.filter_by(
        email="binaryai0010@gmail.com"
    ).first()

    print("Exists:", bool(user))

    if user:
        print("Role:", user.role)
        print("Verified:", user.is_verified)

        print("narayan22 =", user.check_password("narayan22"))
        print("NewStrongPassword123! =", user.check_password("NewStrongPassword123!"))