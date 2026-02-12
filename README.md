# 🔐 Brute Force Attack Simulation - Educational Demo

A cybersecurity educational project that demonstrates brute force attacks and the importance of security measures like rate limiting and strong passwords.

## 🎯 Learning Objectives

- Understand how brute force attacks work
- Learn the importance of rate limiting in preventing attacks
- See why strong passwords are crucial
- Demonstrate different attack vectors (dictionary, brute force, multi-IP)

## 📋 Features

### ✅ Minimum Requirements Met
- **Simple login system** with multiple test users
- **Brute force simulation** with multiple attack methods
- **Attempt counter** displaying number of tries
- **Basic rate limiting** (5 attempts per minute, 5-minute block)

### 🚀 Additional Features
- **Dictionary attacks** using common and breached password lists
- **Hybrid attacks** combining dictionary words with patterns
- **True brute force attacks** with configurable character sets
- **Multi-IP attacks** to bypass rate limiting
- **Credential stuffing** using leaked credential pairs
- **Timing attacks** for information gathering
- **Rainbow table attacks** using precomputed hashes
- **Comprehensive logging** and statistics tracking
- **Interactive and automated demo modes**

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Running the Demo
```bash
# Navigate to the project directory
cd brute-force-demo

# Run the main interactive demo
python brute_force_demo.py

# Run the enhanced automated demo (recommended)
python enhanced_demo.py
```

## 📖 How to Use

### Demo Options

#### Enhanced Automated Demo (Recommended)
Run `python enhanced_demo.py` for a comprehensive demonstration of all attack methods:
- Dictionary attacks
- Hybrid attacks (dictionary + patterns)
- Credential stuffing attacks
- Timing attacks (information gathering)
- Rainbow table attacks
- Rate limiting effectiveness
- Multi-IP bypass attempts

#### Interactive Demo
Run `python brute_force_demo.py` for hands-on exploration with these menu options:

### Main Menu Options
1. **View system users** - See available test accounts
2. **Dictionary Attack** - Try common passwords
3. **Brute Force Attack** - Try all possible combinations
4. **Multi-IP Attack** - Simulate attacks from multiple IPs
5. **Hybrid Attack** - Dictionary + patterns (years, symbols, substitutions)
6. **Credential Stuffing Attack** - Use leaked credentials
7. **Timing Attack** - Analyze response times
8. **Rainbow Table Attack** - Precomputed hash lookup
9. **View Attack Statistics** - See detailed attack logs
10. **Reset System** - Clear all logs and blocks
11. **Exit** - Quit the demo

### Test Accounts
The system includes these test users:
- `admin` (password: `password123`)
- `user` (password: `letmein`)
- `test` (password: `123456`)

## 🔒 Security Features Demonstrated

### Rate Limiting
- **5 attempts per minute** per IP address
- **5-minute temporary block** after exceeding limits
- IP-based tracking and blocking

### Password Security
- SHA-256 hashing (for demo purposes only)
- Demonstrates why weak passwords are vulnerable
- Shows the time difference between attacking weak vs strong passwords

### Attack Prevention
- Logs all login attempts with timestamps
- Tracks success/failure rates
- IP-based blocking mechanisms

## 🎓 Educational Concepts

### Brute Force Attacks
A trial-and-error method used to obtain information such as a user password or personal identification number (PIN).

**Types demonstrated:**
1. **Dictionary Attack** - Uses a list of common passwords
2. **Brute Force Attack** - Tries all possible combinations
3. **Multi-IP Attack** - Bypasses rate limiting using multiple sources

### Rate Limiting
A security measure that controls the rate of requests received from a particular IP address.

**Benefits:**
- Prevents automated attacks
- Reduces server load
- Makes brute force attacks impractical

### Password Security
**Why strong passwords matter:**
- Weak passwords can be cracked in seconds
- Strong passwords take years to brute force
- Complexity exponentially increases difficulty

## 📊 Example Outputs

### Enhanced Demo Output
```
ENHANCED CYBERSECURITY ATTACK SIMULATION DEMO
======================================================================
1. SYSTEM USERS:
   - admin
   - user
   - test

2. DICTIONARY ATTACK DEMO
==================================================
Target: admin user
Method: Common password list
PASSWORD FOUND: 'password123'
Total attempts: 3
Time taken: 0.20 seconds
SUCCESS: Dictionary attack successful!

3. CREDENTIAL STUFFING DEMO
==================================================
Target: test account
Method: Leaked credentials database
PASSWORD FOUND via credential stuffing: '123456'
Source: Leaked credentials database
Total attempts: 2
Time taken: 0.10 seconds
SUCCESS: Credential stuffing successful!
```

### Successful Dictionary Attack
```
=== DICTIONARY ATTACK ON USER: admin ===
IP Address: 192.168.1.100
Testing 15 common passwords...
Attempt 1: Trying 'password'
Result: Invalid username or password
Attempt 2: Trying '123456'
Result: Invalid username or password
Attempt 3: Trying 'password123'
🎯 PASSWORD FOUND: 'password123'
Total attempts: 3
Time taken: 0.30 seconds
```

### Rate Limiting in Action
```
Attempt 5: Trying 'qwerty'
Result: Invalid username or password
Attempt 6: Trying '123456789'
⚠️  Rate limiting activated: Too many failed attempts. IP blocked for 5 minutes.
```

## 🧪 Experiment Ideas

1. **Compare attack speeds** between dictionary and brute force
2. **Test different password lengths** to see complexity impact
3. **Try multi-IP attacks** to bypass rate limiting
4. **Monitor statistics** to understand attack patterns

## ⚠️ Important Notes

### Educational Purpose Only
This tool is designed **exclusively for educational purposes** to demonstrate:
- How brute force attacks work
- Why security measures are necessary
- The importance of strong passwords

### Real-World Security
In production environments, consider:
- Much stronger rate limiting
- Account lockout policies
- Multi-factor authentication
- CAPTCHA systems
- Advanced threat detection

### Password Hashing
The demo uses simple SHA-256 for clarity. In production:
- Use bcrypt, scrypt, or Argon2
- Include salt values
- Implement proper key stretching

## 📈 Performance Metrics

The demo tracks:
- **Total attempts** made during attacks
- **Time duration** of each attack
- **Success rate** percentage
- **Attack rate** (attempts per second)
- **IP blocking** events

## 🤝 Contributing

This is an educational project. Feel free to:
- Add new attack simulations
- Improve the user interface
- Add more security features
- Create additional learning modules

## 📝 License

This project is provided for educational purposes. Use responsibly and only on systems you own or have explicit permission to test.

---

**Remember:** The best defense against brute force attacks is using strong, unique passwords and enabling multi-factor authentication! 🔐
