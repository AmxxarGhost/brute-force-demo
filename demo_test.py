#!/usr/bin/env python3
"""
Automated demo of the brute force simulation
This script demonstrates the key features without requiring user input
"""

from brute_force_demo import BruteForceSimulator
import time

def run_demo():
    print("CYBERSECURITY EDUCATIONAL DEMO - AUTOMATED")
    print("=" * 60)
    print("This demo shows how brute force attacks work and why security matters")
    print("=" * 60)
    
    simulator = BruteForceSimulator()
    
    # Show available users
    print("\n1. SYSTEM USERS:")
    for username in simulator.login_system.users.keys():
        print(f"   - {username}")
    
    # Demonstrate dictionary attack
    print("\n2. DICTIONARY ATTACK DEMO:")
    print("   Target: admin user")
    print("   Method: Common password list")
    
    success = simulator.dictionary_attack("admin")
    
    # Show statistics
    print("\n3. ATTACK STATISTICS:")
    simulator.display_attack_summary()
    
    # Reset for next demo
    simulator.login_system.reset_system()
    simulator.attempt_count = 0
    
    # Demonstrate rate limiting
    print("\n4. RATE LIMITING DEMO:")
    print("   Target: user account")
    print("   Method: Multiple failed attempts to trigger rate limiting")
    
    # Make several failed attempts to trigger rate limiting
    for i in range(7):
        success, message = simulator.login_system.login("user", f"wrongpass{i}", "192.168.1.200")
        print(f"   Attempt {i+1}: {message}")
        if "rate limited" in message.lower() or "blocked" in message.lower():
            break
    
    # Final statistics
    print("\n5. FINAL STATISTICS:")
    stats = simulator.login_system.get_attempt_stats()
    print(f"   Total attempts: {stats['total_attempts']}")
    print(f"   Successful attempts: {stats['successful_attempts']}")
    print(f"   Failed attempts: {stats['failed_attempts']}")
    print(f"   Success rate: {stats['success_rate']:.1f}%")
    
    print("\n" + "=" * 60)
    print("KEY LEARNING POINTS:")
    print("1. Dictionary attacks can quickly find weak passwords")
    print("2. Rate limiting slows down automated attacks")
    print("3. Strong passwords are essential for security")
    print("4. Multiple security layers work best together")
    print("=" * 60)

if __name__ == "__main__":
    run_demo()
