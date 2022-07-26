# Password Cracking - CS 3339 Lab 3
Developed and maintained by Kirk Watson.

Email: klwatson@smu.edu

Class: Info Assurance & Security CS 3339 - Spring 2021

Southern Methodist University

## Functionality
This program takes a file containing 50 passwords that have been salted and hashed using SHA256 and attempts to crack them. This program implements a dictionary and brute-force attack and is able to successfully crack 42 of the 50 hashes.

## How to Use
To use this program, you will not need command-line arguments, but you will need 3 files that have been provided.

### Files:
* rockyou.txt - This text file contains a popular wordlist used to crack passwords
* salt.txt - This text file contains the randomly generated salt used to create the hashes
* hashes.txt - This text file contains the hashes that are to be cracked

## Output
After execution of the program, a cracked.txt file will be created. This text file will contain all 50 hashes in the following format: `hash:password`. Hashes that were not cracked will be followed by a blank space.
