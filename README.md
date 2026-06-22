# Secure Coding Review

## Overview

This project was developed as part of the CodeAlpha Cyber Security Internship.

The objective is to review a vulnerable login application, identify security vulnerabilities, evaluate associated risks, and implement secure coding practices.

## Vulnerabilities Identified

### 1. Hardcoded Credentials

Credentials were stored directly in source code, making them accessible to attackers.

### 2. Plain Text Password Storage

Passwords were stored and compared in plain text.

### 3. No Brute Force Protection

The application allowed unlimited login attempts.

### 4. Weak Authentication Design

The authentication mechanism lacked modern security controls.

## Security Improvements

* Password hashing using SHA-256
* Improved credential handling
* Better authentication practices
* Security-focused code review process

## Tools Used

* Python
* hashlib

## Learning Outcomes

* Secure Coding Practices
* Vulnerability Assessment
* Password Hashing
* Security Review Methodology

## Author

Shrilekha S

## Internship

CodeAlpha Cyber Security Internship
