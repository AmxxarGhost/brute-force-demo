import time
import hashlib
from datetime import datetime, timedelta

class LoginSystem:
    def __init__(self):
        # Simulated user database (username: hashed_password)
        self.users = {
            "admin": self._hash_password("password123"),
            "user": self._hash_password("letmein"),
            "test": self._hash_password("123456")
        }
        
        # Rate limiting: track failed attempts per IP
        self.failed_attempts = {}  # {ip: [timestamp1, timestamp2, ...]}
        self.blocked_ips = {}      # {ip: unblock_time}
        
        # Login attempt logging
        self.attempt_log = []
    
    def _hash_password(self, password):
        """Simple password hashing (for demo purposes only)"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _is_rate_limited(self, ip_address):
        """Check if IP is rate limited or blocked"""
        current_time = datetime.now()
        
        # Check if IP is temporarily blocked
        if ip_address in self.blocked_ips:
            if current_time < self.blocked_ips[ip_address]:
                return True, f"IP blocked. Try again after {self.blocked_ips[ip_address].strftime('%H:%M:%S')}"
            else:
                # Unblock if time has passed
                del self.blocked_ips[ip_address]
                if ip_address in self.failed_attempts:
                    del self.failed_attempts[ip_address]
        
        # Check rate limiting (max 5 attempts per minute)
        if ip_address in self.failed_attempts:
            recent_attempts = [
                ts for ts in self.failed_attempts[ip_address] 
                if current_time - ts < timedelta(minutes=1)
            ]
            
            if len(recent_attempts) >= 5:
                # Block for 5 minutes
                self.blocked_ips[ip_address] = current_time + timedelta(minutes=5)
                return True, "Too many failed attempts. IP blocked for 5 minutes."
            
            self.failed_attempts[ip_address] = recent_attempts
        
        return False, ""
    
    def login(self, username, password, ip_address="127.0.0.1"):
        """Attempt to login with provided credentials"""
        current_time = datetime.now()
        
        # Check rate limiting
        is_limited, limit_message = self._is_rate_limited(ip_address)
        if is_limited:
            self.attempt_log.append({
                'timestamp': current_time,
                'username': username,
                'ip': ip_address,
                'success': False,
                'reason': 'rate_limited'
            })
            return False, limit_message
        
        # Check credentials
        if username in self.users:
            hashed_password = self._hash_password(password)
            if self.users[username] == hashed_password:
                # Successful login
                self.attempt_log.append({
                    'timestamp': current_time,
                    'username': username,
                    'ip': ip_address,
                    'success': True,
                    'reason': 'valid_credentials'
                })
                
                # Clear failed attempts on successful login
                if ip_address in self.failed_attempts:
                    del self.failed_attempts[ip_address]
                
                return True, "Login successful!"
        
        # Failed login
        if ip_address not in self.failed_attempts:
            self.failed_attempts[ip_address] = []
        self.failed_attempts[ip_address].append(current_time)
        
        self.attempt_log.append({
            'timestamp': current_time,
            'username': username,
            'ip': ip_address,
            'success': False,
            'reason': 'invalid_credentials'
        })
        
        return False, "Invalid username or password"
    
    def get_attempt_stats(self):
        """Get login attempt statistics"""
        total_attempts = len(self.attempt_log)
        successful_attempts = len([log for log in self.attempt_log if log['success']])
        failed_attempts = total_attempts - successful_attempts
        
        return {
            'total_attempts': total_attempts,
            'successful_attempts': successful_attempts,
            'failed_attempts': failed_attempts,
            'success_rate': (successful_attempts / total_attempts * 100) if total_attempts > 0 else 0
        }
    
    def display_recent_attempts(self, limit=10):
        """Display recent login attempts"""
        print("\n=== Recent Login Attempts ===")
        recent = self.attempt_log[-limit:] if len(self.attempt_log) > limit else self.attempt_log
        
        for attempt in recent:
            status = "SUCCESS" if attempt['success'] else "FAILED"
            reason = attempt['reason']
            print(f"{attempt['timestamp'].strftime('%H:%M:%S')} - {attempt['username']}@{attempt['ip']} - {status} ({reason})")
    
    def reset_system(self):
        """Reset the login system (for demo purposes)"""
        self.failed_attempts.clear()
        self.blocked_ips.clear()
        self.attempt_log.clear()
        print("Login system reset successfully!")
