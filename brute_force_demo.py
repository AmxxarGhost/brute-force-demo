import time
import itertools
import random
import string
from login_system import LoginSystem

class BruteForceSimulator:
    def __init__(self):
        self.login_system = LoginSystem()
        self.attempt_count = 0
        self.start_time = None
        self.end_time = None
        
        # Common password lists for simulation
        self.common_passwords = [
            "password", "123456", "password123", "admin", "letmein",
            "qwerty", "123456789", "password1", "abc123", "111111",
            "123123", "admin123", "root", "toor", "pass"
        ]
        
        # Character sets for different complexity levels
        self.char_sets = {
            'digits': string.digits,
            'lowercase': string.ascii_lowercase,
            'uppercase': string.ascii_uppercase,
            'symbols': '!@#$%^&*()_+-=[]{}|;:,.<>?'
        }
    
    def dictionary_attack(self, username, target_password=None, ip_address="192.168.1.100"):
        """Simulate a dictionary attack using common passwords"""
        print(f"\n=== DICTIONARY ATTACK ON USER: {username} ===")
        print(f"IP Address: {ip_address}")
        print(f"Testing {len(self.common_passwords)} common passwords...")
        
        self.start_time = time.time()
        self.attempt_count = 0
        
        for password in self.common_passwords:
            self.attempt_count += 1
            print(f"Attempt {self.attempt_count}: Trying '{password}'")
            
            success, message = self.login_system.login(username, password, ip_address)
            
            if success:
                self.end_time = time.time()
                print(f"\nPASSWORD FOUND: '{password}'")
                print(f"Total attempts: {self.attempt_count}")
                print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
                return True
            
            print(f"Result: {message}")
            
            # Small delay to simulate real attack
            time.sleep(0.1)
            
            # Check if we're rate limited
            if "rate limited" in message.lower() or "blocked" in message.lower():
                print(f"Rate limiting activated: {message}")
                break
        
        self.end_time = time.time()
        print(f"\nDictionary attack failed")
        print(f"Total attempts: {self.attempt_count}")
        print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
        return False
    
    def brute_force_attack(self, username, max_length=4, charset='lowercase', ip_address="192.168.1.101"):
        """Simulate a brute force attack by trying all combinations"""
        print(f"\n=== BRUTE FORCE ATTACK ON USER: {username} ===")
        print(f"IP Address: {ip_address}")
        print(f"Max password length: {max_length}")
        print(f"Character set: {charset}")
        
        chars = self.char_sets[charset]
        total_combinations = sum(len(chars) ** length for length in range(1, max_length + 1))
        
        print(f"Total possible combinations: {total_combinations:,}")
        print("WARNING: This may take a very long time!")
        
        response = input("Continue with brute force attack? (y/n): ")
        if response.lower() != 'y':
            print("Brute force attack cancelled.")
            return False
        
        self.start_time = time.time()
        self.attempt_count = 0
        
        for length in range(1, max_length + 1):
            print(f"\nTrying all {length}-character combinations...")
            
            for combination in itertools.product(chars, repeat=length):
                password = ''.join(combination)
                self.attempt_count += 1
                
                if self.attempt_count % 1000 == 0:
                    elapsed = time.time() - self.start_time
                    rate = self.attempt_count / elapsed
                    print(f"Attempt {self.attempt_count:,} ({rate:.1f} attempts/sec): '{password}'")
                
                success, message = self.login_system.login(username, password, ip_address)
                
                if success:
                    self.end_time = time.time()
                    print(f"\nPASSWORD FOUND: '{password}'")
                    print(f"Total attempts: {self.attempt_count:,}")
                    print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
                    return True
                
                # Check if we're rate limited
                if "rate limited" in message.lower() or "blocked" in message.lower():
                    print(f"Rate limiting activated: {message}")
                    break
        
        self.end_time = time.time()
        print(f"\nBrute force attack failed")
        print(f"Total attempts: {self.attempt_count:,}")
        print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
        return False
    
    def multi_ip_attack(self, username, num_ips=5):
        """Simulate attack from multiple IP addresses to bypass rate limiting"""
        print(f"\n=== MULTI-IP ATTACK ON USER: {username} ===")
        print(f"Simulating attack from {num_ips} different IP addresses...")
        
        self.start_time = time.time()
        self.attempt_count = 0
        
        # Generate fake IP addresses
        ip_addresses = [f"192.168.1.{100+i}" for i in range(num_ips)]
        
        for round_num in range(3):  # 3 rounds of attacks
            print(f"\nRound {round_num + 1}:")
            
            for ip in ip_addresses:
                # Try a few passwords from each IP
                for password in self.common_passwords[:3]:  # Try first 3 passwords
                    self.attempt_count += 1
                    print(f"Attempt {self.attempt_count}: {ip} trying '{password}'")
                    
                    success, message = self.login_system.login(username, password, ip)
                    
                    if success:
                        self.end_time = time.time()
                        print(f"\nPASSWORD FOUND: '{password}'")
                        print(f"Total attempts: {self.attempt_count}")
                        print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
                        return True
                    
                    print(f"Result: {message}")
                    time.sleep(0.05)
        
        self.end_time = time.time()
        print(f"\nMulti-IP attack failed")
        print(f"Total attempts: {self.attempt_count}")
        print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
        return False
    
    def display_attack_summary(self):
        """Display summary of the attack"""
        if self.start_time and self.end_time:
            duration = self.end_time - self.start_time
            print(f"\n=== ATTACK SUMMARY ===")
            print(f"Total attempts: {self.attempt_count:,}")
            print(f"Duration: {duration:.2f} seconds")
            print(f"Average rate: {self.attempt_count/duration:.1f} attempts/second")
        
        # Display login system statistics
        stats = self.login_system.get_attempt_stats()
        print(f"\n=== LOGIN SYSTEM STATISTICS ===")
        print(f"Total login attempts: {stats['total_attempts']}")
        print(f"Successful attempts: {stats['successful_attempts']}")
        print(f"Failed attempts: {stats['failed_attempts']}")
        print(f"Success rate: {stats['success_rate']:.1f}%")
        
        # Display recent attempts
        self.login_system.display_recent_attempts()

def main():
    print("CYBERSECURITY EDUCATIONAL DEMO - BRUTE FORCE SIMULATION")
    print("=" * 60)
    print("WARNING: This tool is for EDUCATIONAL PURPOSES ONLY!")
    print("Demonstrates why strong passwords and rate limiting are important.")
    print("=" * 60)
    
    simulator = BruteForceSimulator()
    
    while True:
        print("\nMENU:")
        print("1. View system users")
        print("2. Dictionary Attack")
        print("3. Brute Force Attack")
        print("4. Multi-IP Attack (bypass rate limiting)")
        print("5. View Attack Statistics")
        print("6. Reset System")
        print("7. Exit")
        
        choice = input("\nSelect an option (1-7): ")
        
        if choice == '1':
            print("\nSYSTEM USERS:")
            for username in simulator.login_system.users.keys():
                print(f"  - {username}")
        
        elif choice == '2':
            username = input("Enter target username: ")
            if username in simulator.login_system.users:
                simulator.dictionary_attack(username)
            else:
                print("ERROR: User not found!")
        
        elif choice == '3':
            username = input("Enter target username: ")
            if username in simulator.login_system.users:
                max_length = input("Enter max password length (default 3): ")
                max_length = int(max_length) if max_length.isdigit() else 3
                
                print("Available character sets:")
                for i, charset in enumerate(simulator.char_sets.keys(), 1):
                    print(f"{i}. {charset}")
                
                charset_choice = input("Select character set (1-4): ")
                charsets = list(simulator.char_sets.keys())
                charset = charsets[int(charset_choice) - 1] if charset_choice.isdigit() else 'lowercase'
                
                simulator.brute_force_attack(username, max_length, charset)
            else:
                print("ERROR: User not found!")
        
        elif choice == '4':
            username = input("Enter target username: ")
            if username in simulator.login_system.users:
                num_ips = input("Number of IP addresses (default 5): ")
                num_ips = int(num_ips) if num_ips.isdigit() else 5
                simulator.multi_ip_attack(username, num_ips)
            else:
                print("ERROR: User not found!")
        
        elif choice == '5':
            simulator.display_attack_summary()
        
        elif choice == '6':
            simulator.login_system.reset_system()
            simulator.attempt_count = 0
            simulator.start_time = None
            simulator.end_time = None
            print("System reset complete!")
        
        elif choice == '7':
            print("Exiting demo. Remember to use strong passwords!")
            break
        
        else:
            print("ERROR: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
