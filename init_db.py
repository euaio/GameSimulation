"""
Database initialization script for PythonAnywhere
Run this ONCE after uploading your files:
    python3 init_db.py
"""
from app import app, db, create_admin

with app.app_context():
    # Create all database tables
    db.create_all()
    print("✅ Database tables created successfully!")
    
    # Create default admin user
    create_admin()
    print("✅ Setup complete!")
    print("\nDefault Admin Credentials:")
    print("  Username: admin")
    print("  Password: administration")
    print("\n⚠️  Remember to change the admin password after first login!")
