#!/usr/bin/env python3
import os
import re

def fix_settings_auth_user_model():
    """Fix the AUTH_USER_MODEL in settings.py"""
    print("🔧 Fixing AUTH_USER_MODEL in settings.py...")
    
    settings_path = 'config/settings.py'
    
    if os.path.exists(settings_path):
        with open(settings_path, 'r') as f:
            content = f.read()
        
        # Fix AUTH_USER_MODEL
        old_content = content
        content = re.sub(
            r"AUTH_USER_MODEL\s*=\s*['\"]apps\.users\.User['\"]",
            "AUTH_USER_MODEL = 'users.User'",
            content
        )
        
        # Also fix any other model references in settings
        content = re.sub(
            r"['\"]apps\.([a-z]+)\.([A-Z][a-zA-Z]+)['\"]",
            r"'\1.\2'",
            content
        )
        
        if old_content != content:
            with open(settings_path, 'w') as f:
                f.write(content)
            print("✅ Fixed AUTH_USER_MODEL in settings.py")
        else:
            print("✅ AUTH_USER_MODEL already correct")
    else:
        print("❌ settings.py not found")

def fix_installed_apps():
    """Fix INSTALLED_APPS to remove apps. prefix"""
    print("🔧 Fixing INSTALLED_APPS...")
    
    settings_path = 'config/settings.py'
    
    if os.path.exists(settings_path):
        with open(settings_path, 'r') as f:
            content = f.read()
        
        # Remove apps. prefix from installed apps
        old_content = content
        content = re.sub(
            r"['\"]apps\.(users|products|cart|orders|reviews)['\"]",
            r"'\1'",
            content
        )
        
        if old_content != content:
            with open(settings_path, 'w') as f:
                f.write(content)
            print("✅ Fixed INSTALLED_APPS")
        else:
            print("✅ INSTALLED_APPS already correct")

def check_current_settings():
    """Check what the current settings look like"""
    print("\n🔍 Checking current settings...")
    
    settings_path = 'config/settings.py'
    
    if os.path.exists(settings_path):
        with open(settings_path, 'r') as f:
            content = f.read()
        
        # Find AUTH_USER_MODEL
        auth_match = re.search(r"AUTH_USER_MODEL\s*=\s*['\"]([^'\"]+)['\"]", content)
        if auth_match:
            print(f"📋 Current AUTH_USER_MODEL: '{auth_match.group(1)}'")
        
        # Find installed apps
        installed_apps_match = re.findall(r"['\"](apps\.\w+)['\"]", content)
        if installed_apps_match:
            print(f"📋 Found apps with 'apps.' prefix: {installed_apps_match}")

def run_quick_test():
    """Run a quick test to see if it works"""
    print("\n🚀 Testing Django setup...")
    
    # Create a minimal test script
    test_script = """
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
try:
    django.setup()
    print("✅ Django setup successful!")
    
    # Test if we can import the user model
    from django.contrib.auth import get_user_model
    User = get_user_model()
    print(f"✅ User model imported: {User}")
    
except Exception as e:
    print(f"❌ Error: {e}")
"""
    
    with open('test_django.py', 'w') as f:
        f.write(test_script)
    
    try:
        import subprocess
        result = subprocess.run(['python3', 'test_django.py'], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Stderr:", result.stderr)
    except Exception as e:
        print(f"❌ Test failed: {e}")
    finally:
        # Clean up
        if os.path.exists('test_django.py'):
            os.remove('test_django.py')

if __name__ == "__main__":
    print("🛠️ Fixing Django settings configuration...")
    
    # Check current state
    check_current_settings()
    
    # Fix the issues
    fix_installed_apps()
    fix_settings_auth_user_model()
    
    # Check again
    check_current_settings()
    
    # Test
    run_quick_test()
    
    print("\n🎉 Settings fix complete!")
    print("\n📋 If issues persist, manually check config/settings.py for:")
    print("1. AUTH_USER_MODEL = 'users.User'")
    print("2. INSTALLED_APPS should have 'users', not 'apps.users'")
    print("3. No other 'apps.' prefixes in model references")