#!/usr/bin/env python3
import notification_app
import time
import sys

def test_notifications():
    print("Testing Claude Code Notification App...")
    print("=" * 50)
    
    # Test waiting notification
    print("\n1. Testing notify_waiting()...")
    try:
        success = notification_app.notify_waiting("Test: Claude Code is waiting for input")
        if success:
            print("✓ notify_waiting() sent successfully")
        else:
            print("✗ notify_waiting() failed")
    except Exception as e:
        print(f"✗ notify_waiting() error: {e}")
    
    # Wait a moment between notifications
    time.sleep(2)
    
    # Test completion notification
    print("\n2. Testing notify_done()...")
    try:
        success = notification_app.notify_done("Test: Claude Code task completed successfully")
        if success:
            print("✓ notify_done() sent successfully")
        else:
            print("✗ notify_done() failed")
    except Exception as e:
        print(f"✗ notify_done() error: {e}")
    
    # Test class-based usage
    print("\n3. Testing NotificationApp class...")
    try:
        app = notification_app.NotificationApp()
        success = app.notify_waiting("Test: Class-based notification")
        if success:
            print("✓ NotificationApp class works correctly")
        else:
            print("✗ NotificationApp class failed")
    except Exception as e:
        print(f"✗ NotificationApp class error: {e}")
    
    print("\n" + "=" * 50)
    print("Test completed. Check your device for notifications!")
    print("If you didn't receive notifications, verify your Pushover credentials.")

if __name__ == "__main__":
    test_notifications()