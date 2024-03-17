from datetime import timedelta
from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, User_schema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from psycopg2 import errorcodes

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route("/register", methods=["POST"])
def auth_register():
    try:
        #data that we get in the body of the request
        body_data = request.get_json()

        # create the user instance
        user = User(
            name=body_data.get('name'),
            email=body_data.get('email')
        )

        #password from the request body
        password = body_data.get('password')
        
        #if password exists hash the password
        if password:
            user.password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        #add to the session
        db.session.add(user)
        #commit to the session
        db.session.commit()

        #respond back to the client insomnia
        return User_schema.dump(user), 201
    
    except IntegrityError as err:
        print(err.orig.diag.column_name)
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The {err.orig.diag.column_name} is required"}
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Email address already in use"}, 409

    
@auth_bp.route("/login", methods=["POST"])
def auth_login():
    # get the request body
    body_data = request.get_json()
    #find the user with the email address
    stmt = db.select(User).filter_by(email=body_data.get("email"))
    user = db.session.scalar(stmt)
    # if user exists and apassowrd is correct
    if user and bcrypt.check_password_hash(user.password, body_data.get("password")):
        # create jwt
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        #return the token along with the user info
        user_data = User_schema.dump(user)
        user_data["token"] = token
        return user_data
        # return {**User_schema.dump(user), "token": token}, 201
        # return {"email": user.email, "token": token, "is_admin": user.is_admin}
    # else
    else:
        # return error
        return {"error": "Invalid email or password"}, 401