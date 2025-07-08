import requests
import time
import os
from typing import Optional


class NotificationApp:
    def __init__(self, user_key: Optional[str] = None, api_token: Optional[str] = None):
        self.user_key = user_key or os.getenv('PUSHOVER_USER_KEY', 'ub25psac18b2gz7qhgd7s6hr2sg1zq')
        self.api_token = api_token or os.getenv('PUSHOVER_API_TOKEN', 'ajp8ouohjzi6tff2a55sri3bqox3hf')
        self.base_url = 'https://api.pushover.net/1/messages.json'
        self.max_retries = 3
        self.retry_delay = 1
    
    def _send_notification(self, message: str, title: str, priority: int = 0) -> bool:
        data = {
            'token': self.api_token,
            'user': self.user_key,
            'message': message,
            'title': title,
            'priority': priority
        }
        
        for attempt in range(self.max_retries):
            try:
                response = requests.post(self.base_url, data=data, timeout=10)
                
                if response.status_code == 200:
                    return True
                else:
                    print(f"Pushover API error (attempt {attempt + 1}): {response.status_code} - {response.text}")
                    
            except requests.exceptions.RequestException as e:
                print(f"Network error (attempt {attempt + 1}): {e}")
            
            if attempt < self.max_retries - 1:
                time.sleep(self.retry_delay)
        
        print("Failed to send notification after all retry attempts")
        return False
    
    def notify_waiting(self, custom_message: Optional[str] = None) -> bool:
        message = custom_message or "Claude Code is waiting for your input. Please check your terminal."
        title = "Claude Code - Input Required"
        return self._send_notification(message, title, priority=1)
    
    def notify_done(self, custom_message: Optional[str] = None) -> bool:
        message = custom_message or "Claude Code has completed the task successfully."
        title = "Claude Code - Task Complete"
        return self._send_notification(message, title, priority=0)


_default_app = NotificationApp()

def notify_waiting(custom_message: Optional[str] = None) -> bool:
    return _default_app.notify_waiting(custom_message)

def notify_done(custom_message: Optional[str] = None) -> bool:
    return _default_app.notify_done(custom_message)