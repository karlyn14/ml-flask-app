"""
SILENT CUSTOMER CHURN PREDICTOR - SETUP GUIDE
==============================================

This guide will walk you through setting up and running the project.
"""

import subprocess
import sys
import os

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def check_python_version():
    print_header("Checking Python Version")
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("⚠️  Warning: Python 3.8+ recommended")
    else:
        print("✓ Python version is compatible")

def install_requirements():
    print_header("Installing Dependencies")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ All dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Error installing dependencies")
        print("Try manually: pip install -r requirements.txt")

def check_files():
    print_header("Checking Project Files")
    required_files = [
        "app.py",
        "customer_churn_data.csv",
        "templates/index.html",
        "static/style.css",
        "static/script.js",
        "requirements.txt"
    ]

    all_present = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"❌ {file} - MISSING")
            all_present = False

    return all_present

def run_application():
    print_header("Starting Application")
    print("\nThe application will start on http://127.0.0.1:5000")
    print("Press Ctrl+C to stop the server\n")
    print("Opening browser automatically...")
    print("-"*60)

    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n\nApplication stopped by user")

def main():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     SILENT CUSTOMER CHURN PREDICTOR - SETUP WIZARD        ║
    ║                                                           ║
    ║  Detect behavioral disengagement before customers leave   ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)

    check_python_version()

    if not check_files():
        print("\n❌ Some files are missing. Please ensure all project files are present.")
        return

    response = input("\n📦 Install dependencies? (y/n): ").lower()
    if response == 'y':
        install_requirements()

    print("\n" + "="*60)
    print("  SETUP COMPLETE!")
    print("="*60)
    print("\nNext steps:")
    print("  1. The app will automatically train the model on first run")
    print("  2. Use the web interface to predict churn")
    print("  3. Try the batch analysis feature")
    print("  4. Review the README.md for detailed documentation")

    response = input("\n🚀 Start the application now? (y/n): ").lower()
    if response == 'y':
        run_application()
    else:
        print("\nTo start later, run: python app.py")
        print("Then open: http://127.0.0.1:5000")

if __name__ == "__main__":
    main()
