#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Post

# Establish connection: 
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to check if username already exists
def username_exists(username):
    return session.query(User).filter_by(username=username).first() is not None

# Example: Creating a user
new_username = "Prider"
if not username_exists(new_username):
    try:
        new_user = User(username=new_username, email='Rayan@Kamouch.com')
        session.add(new_user)
        # Commit the transaction to persist the user
        session.commit()
    except Exception as e:
        print(f"Error creating user: {e}")
        # Rollbacl the transaction in case of an error
        session.rollback()
else:
     print(f"Username '{new_username}' already exists. Choose a different username.")

# close session
session.close()
# Updating Records:
# user = session.query(User).filter_by(username='FatimaZahra').first()
# user.username = 'Wafa'
# user.email = 'wafa@marouani.com'
# session.commit()

# Deleting a Record:
# user = session.query(User).filter_by(username='john_doe').first()
# session.delete(user)
# session.commit()

# Create a user with posts
# new_user = User(username='john_doe', email='john@example.com')
# new_post1 = Post(title='Post 1', content='Content 1')
# new_post2 = Post(title='Post 2', content='Content 2')

# Associate the posts with the user
# new_user.posts = [new_post1, new_post2]

# Add the user to the session and commit
# session.add(new_user)
# session.commit()

# Example: Querying users
all_users = session.query(User).all()
for user in all_users:
    print(f'User ID: {user.id}, Username: {user.username}, Email: {user.email}')
