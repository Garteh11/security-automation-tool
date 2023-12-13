#!/usr/bin/env python3
import subprocess
import os
import logging

# Configure logging
logging.basicConfig(filename='security_tool_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_action(action):
    logging.info(action)

def check_for_updates():
    try:
        print("\nChecking for updates...")
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "list", "--upgradable"])
        log_action("Checked for system updates.")
    except Exception as e:
        print(f"Error: {e}")
        log_action(f"Error checking for updates: {e}")

def port_scanner():
    try:
        print("\nScanning open ports...")
        subprocess.run(["nmap", "-p", "1-1000", "localhost"])
        log_action("Performed port scanning.")
    except Exception as e:
        print(f"Error: {e}")
        log_action(f"Error during port scanning: {e}")

def security_audit():
    try:
        print("\nRunning security audit...")
        subprocess.run(["sudo", "lynis", "audit", "system"])
        log_action("Completed security audit.")
    except Exception as e:
        print(f"Error: {e}")
        log_action(f"Error during security audit: {e}")

if __name__ == "__main__":
    print("Advanced Security Automation Tool")

    while True:
        print("\nOptions:")
        print("1. Check for updates")
        print("2. Port Scanner")
        print("3. Security Audit")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            check_for_updates()
        elif choice == "2":
            port_scanner()
        elif choice == "3":
            security_audit()
        elif choice == "4":
            print("Exiting the tool.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
