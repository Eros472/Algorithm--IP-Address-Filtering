# IP Address Allow List Updater

## Overview
This Python script is designed for a healthcare company to manage access to restricted content by updating an allow list of IP addresses. As a security professional, you are tasked with ensuring that only authorized employees (identified by their IP addresses) can access personal patient records. The script checks an allow list against a remove list and updates the allow list file by removing any IP addresses that appear in the remove list. This project was created for the Google Cybersecurity Certificate course portfolio activity: Automate Cybersecurity Tasks with Python Module 4- Python in practice

## Purpose
- Maintain a secure subnetwork by regularly updating the allow list of IP addresses.
- Remove access for employees whose IP addresses are listed in the remove list.
- Ensure compliance with security protocols by automating IP address management.

## Prerequisites
- Python 3.x installed on your system.
- Two text files: `allow_list.txt` (containing authorized IP addresses) and `remove_list.txt` (containing IP addresses to be removed).
- Both files should be in the same directory as the script or provide the full path.

## Usage
1. Ensure `allow_list.txt` and `remove_list.txt` are created with one IP address per line.
2. Run the script using the command:
   ```bash
   python script_name.py
