# paSSH

Description
===========
paSSH (paSSH.py) is a simple Python SSH server that reveals passwords of connecting clients.  This tool is designed for penetration testers and security enthusiasts.

Use Case(s)
===========
- Reveal stored credentials during penetration tests

Requirements
============
- Python 2.x.x
- Paramiko [https://github.com/paramiko/paramiko]
- RSA private key file (example provided)

Tool Usage
==========
- python paSSH.py -k [RSA private key file] -p [TCP port]
- e.g. python paSSH.py -k id_rsa_example -p 22

Example Output
==============

root@zzzz:~/paSSH# python paSSH.py -k id_rsa_example -p 22

===================== paSSH [SSH Password Revealer] =====================
[*] Connection Attempt: user= froo | passwd= vslfnhslkfnh
[*] Connection Attempt: user= froo | passwd= nslgkdgknsl
[*] Connection Attempt: user= froo | passwd= lsgnslgsekbnlb


Tool Usage & Ethics
===================
This tool was designed to help security professionals perform ethical and legal vulnerability assessments and penetration tests.  Do not use for nefarious purposes.

Also, I "program" for functionality, not necessarily final completion.  I am striving the for latter a little more each day...so if you find any major problems, let me know.