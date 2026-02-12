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
        
        # Enhanced password lists for simulation
        self.common_passwords = [
            "password", "123456", "password123", "admin", "letmein",
            "qwerty", "123456789", "password1", "abc123", "111111",
            "123123", "admin123", "root", "toor", "pass", "welcome",
            "monkey", "dragon", "master", "sunshine", "princess",
            "football", "baseball", "shadow", "superman", "iloveyou"
        ]
        
        # Leaked passwords from common breaches (educational sample)
        self.breached_passwords = [
            "123456", "password", "123456789", "12345678", "12345",
            "1234567", "1234567890", "1234", "qwerty", "abc123",
            "password123", "admin", "letmein", "welcome", "monkey",
            "1234567890", "password1", "qwertyuiop", "1234567", "12345678"
        ]
        
        # Common patterns for hybrid attacks
        self.common_patterns = {
            'years': ['2020', '2021', '2022', '2023', '2024', '2025', '2026'],
            'months': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
            'symbols': ['!', '@', '#', '$', '%', '&', '*'],
            'common_words': ['admin', 'user', 'login', 'pass', 'secure', 'test', 'demo']
        }
        
        # Character sets for different complexity levels
        self.char_sets = {
            'digits': string.digits,
            'lowercase': string.ascii_lowercase,
            'uppercase': string.ascii_uppercase,
            'symbols': '!@#$%^&*()_+-=[]{}|;:,.<>?',
            'alphanumeric': string.ascii_letters + string.digits,
            'all': string.ascii_letters + string.digits + '!@#$%^&*()_+-=[]{}|;:,.<>?'
        }
        
        # Timing attack data
        self.timing_data = []
    
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
    
    def hybrid_attack(self, username, base_word="password", ip_address="192.168.1.102"):
        """Simulate a hybrid attack combining dictionary with patterns"""
        print(f"\n=== HYBRID ATTACK ON USER: {username} ===")
        print(f"IP Address: {ip_address}")
        print(f"Base word: {base_word}")
        print("Combining base words with common patterns...")
        
        self.start_time = time.time()
        self.attempt_count = 0
        
        # Generate hybrid passwords
        hybrid_passwords = []
        
        # Base word + years
        for year in self.common_patterns['years']:
            hybrid_passwords.append(base_word + year)
            hybrid_passwords.append(year + base_word)
        
        # Base word + symbols
        for symbol in self.common_patterns['symbols']:
            hybrid_passwords.append(base_word + symbol)
            hybrid_passwords.append(symbol + base_word)
        
        # Capitalization variations
        hybrid_passwords.append(base_word.capitalize())
        hybrid_passwords.append(base_word.upper())
        hybrid_passwords.append(base_word.title())
        
        # Common substitutions
        substitutions = {'a': '@', 's': '$', 'i': '1', 'o': '0', 'e': '3'}
        for char, sub in substitutions.items():
            if char in base_word:
                hybrid_passwords.append(base_word.replace(char, sub))
        
        # Remove duplicates
        hybrid_passwords = list(set(hybrid_passwords))
        
        print(f"Generated {len(hybrid_passwords)} hybrid passwords")
        
        for password in hybrid_passwords:
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
            time.sleep(0.05)
            
            if "rate limited" in message.lower() or "blocked" in message.lower():
                print(f"Rate limiting activated: {message}")
                break
        
        self.end_time = time.time()
        print(f"\nHybrid attack failed")
        print(f"Total attempts: {self.attempt_count}")
        print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
        return False
    
    def credential_stuffing_attack(self, username, ip_address="192.168.1.103"):
        """Simulate credential stuffing using leaked credentials"""
        print(f"\n=== CREDENTIAL STUFFING ATTACK ON USER: {username} ===")
        print(f"IP Address: {ip_address}")
        print("Using leaked credentials from common breaches...")
        
        self.start_time = time.time()
        self.attempt_count = 0
        
        # Simulate leaked credential pairs (username, password)
        leaked_credentials = [
            ("admin", "password123"),
            ("user", "123456"),
            ("test", "qwerty"),
            ("admin", "admin"),
            ("root", "toor"),
            ("guest", "guest"),
            ("user", "password"),
            ("admin", "123456"),
            ("test", "test"),
            ("demo", "demo123")
        ]
        
        print(f"Testing {len(leaked_credentials)} leaked credential pairs...")
        
        for cred_user, cred_pass in leaked_credentials:
            # Only test if username matches or try common variations
            if cred_user == username or username in ["admin", "user", "test", "guest", "demo"]:
                self.attempt_count += 1
                print(f"Attempt {self.attempt_count}: Trying leaked pair ({cred_user}, '{cred_pass}')")
                
                success, message = self.login_system.login(username, cred_pass, ip_address)
                
                if success:
                    self.end_time = time.time()
                    print(f"\nPASSWORD FOUND via credential stuffing: '{cred_pass}'")
                    print(f"Source: Leaked credentials database")
                    print(f"Total attempts: {self.attempt_count}")
                    print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
                    return True
                
                print(f"Result: {message}")
                time.sleep(0.1)
                
                if "rate limited" in message.lower() or "blocked" in message.lower():
                    print(f"Rate limiting activated: {message}")
                    break
        
        self.end_time = time.time()
        print(f"\nCredential stuffing attack failed")
        print(f"Total attempts: {self.attempt_count}")
        print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
        return False
    
    def timing_attack(self, username, ip_address="192.168.1.104"):
        """Simulate a timing attack to analyze password characteristics"""
        print(f"\n=== TIMING ATTACK ON USER: {username} ===")
        print(f"IP Address: {ip_address}")
        print("Analyzing response times to gather password information...")
        
        self.start_time = time.time()
        self.attempt_count = 0
        
        # Test different password lengths to see timing differences
        test_passwords = [
            "a", "ab", "abc", "abcd", "abcde",
            "password", "password123", "password1234",
            "x" * 8, "x" * 12, "x" * 16
        ]
        
        timing_results = []
        
        for test_pass in test_passwords:
            self.attempt_count += 1
            
            # Measure response time
            start_time = time.time()
            success, message = self.login_system.login(username, test_pass, ip_address)
            response_time = time.time() - start_time
            
            timing_results.append({
                'password': test_pass,
                'length': len(test_pass),
                'response_time': response_time,
                'success': success
            })
            
            print(f"Attempt {self.attempt_count}: '{test_pass}' (len={len(test_pass)}) - {response_time:.4f}s - {message}")
            
            if success:
                self.end_time = time.time()
                print(f"\nPASSWORD FOUND: '{test_pass}'")
                print(f"Total attempts: {self.attempt_count}")
                print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
                return True
            
            time.sleep(0.05)
        
        # Analyze timing patterns
        print(f"\n=== TIMING ANALYSIS ===")
        avg_times_by_length = {}
        for result in timing_results:
            length = result['length']
            if length not in avg_times_by_length:
                avg_times_by_length[length] = []
            avg_times_by_length[length].append(result['response_time'])
        
        for length, times in sorted(avg_times_by_length.items()):
            avg_time = sum(times) / len(times)
            print(f"Length {length}: Average response time {avg_time:.4f}s")
        
        self.end_time = time.time()
        print(f"\nTiming attack completed (information gathering)")
        print(f"Total attempts: {self.attempt_count}")
        print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
        print("Note: Timing attacks can reveal password length and complexity patterns")
        return False
    
    def rainbow_table_attack(self, username, ip_address="192.168.1.105"):
        """Simulate a rainbow table attack using precomputed hashes"""
        print(f"\n=== RAINBOW TABLE ATTACK ON USER: {username} ===")
        print(f"IP Address: {ip_address}")
        print("Using precomputed hash table for common passwords...")
        
        self.start_time = time.time()
        self.attempt_count = 0
        
        # Simulate a small rainbow table (hash -> password)
        # In reality, this would be much larger
        rainbow_table = {
            "5f4dcc3b5aa765d61d8327deb882cf99": "password",
            "e10adc3949ba59abbe56e057f20f883e": "123456",
            "ef92b778ba7a6c8f2150019a35c23a5d": "password123",
            "21232f297a57a5a743894a0e4a801fc3": "admin",
            "5d41402abc4b2a76b9719d911017c592": "hello",
            "25d55ad283aa400af464c76d713c07ad": "123456789",
            "c4ca4238a0b923820dcc509a6f75849b": "1",
            "eccbc87e4b5ce2fe28308fd9f2a7baf3": "3",
            "a87ff679a2f3e71d9181a67b7542122c": "4",
            "e4da3b7fbbce2345d7772b0674a318d5": "5"
        }
        
        print(f"Rainbow table contains {len(rainbow_table)} precomputed hashes")
        
        # In a real attack, we'd need access to the hash, but for demo purposes
        # we'll simulate by trying the passwords from the rainbow table
        for hash_value, password in rainbow_table.items():
            self.attempt_count += 1
            print(f"Attempt {self.attempt_count}: Testing rainbow table entry: '{password}'")
            
            success, message = self.login_system.login(username, password, ip_address)
            
            if success:
                self.end_time = time.time()
                print(f"\nPASSWORD FOUND via rainbow table: '{password}'")
                print(f"Hash: {hash_value}")
                print(f"Total attempts: {self.attempt_count}")
                print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
                return True
            
            print(f"Result: {message}")
            time.sleep(0.05)
        
        self.end_time = time.time()
        print(f"\nRainbow table attack failed")
        print(f"Total attempts: {self.attempt_count}")
        print(f"Time taken: {self.end_time - self.start_time:.2f} seconds")
        print("Note: Rainbow tables are effective against unsalted hashes")
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
        print("5. Hybrid Attack (dictionary + patterns)")
        print("6. Credential Stuffing Attack")
        print("7. Timing Attack (information gathering)")
        print("8. Rainbow Table Attack")
        print("9. View Attack Statistics")
        print("10. Reset System")
        print("11. Exit")
        
        choice = input("\nSelect an option (1-11): ")
        
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
            username = input("Enter target username: ")
            if username in simulator.login_system.users:
                base_word = input("Enter base word for hybrid attack (default 'password'): ") or "password"
                simulator.hybrid_attack(username, base_word)
            else:
                print("ERROR: User not found!")
        
        elif choice == '6':
            username = input("Enter target username: ")
            if username in simulator.login_system.users:
                simulator.credential_stuffing_attack(username)
            else:
                print("ERROR: User not found!")
        
        elif choice == '7':
            username = input("Enter target username: ")
            if username in simulator.login_system.users:
                simulator.timing_attack(username)
            else:
                print("ERROR: User not found!")
        
        elif choice == '8':
            username = input("Enter target username: ")
            if username in simulator.login_system.users:
                simulator.rainbow_table_attack(username)
            else:
                print("ERROR: User not found!")
        
        elif choice == '9':
            simulator.display_attack_summary()
        
        elif choice == '10':
            simulator.login_system.reset_system()
            simulator.attempt_count = 0
            simulator.start_time = None
            simulator.end_time = None
            print("System reset complete!")
        
        elif choice == '11':
            print("Exiting demo. Remember to use strong passwords!")
            break
        
        else:
            print("ERROR: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
