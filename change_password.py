from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    mentor = User.query.filter_by(
        email="binaryai0010@gmail.com"
    ).first()

    if mentor:
        mentor.set_password("narayan22")
        db.session.commit()

        # Verify immediately
        print("Password updated")
        print("Check:", mentor.check_password("narayan22"))
    else:
        print("Mentor not found")