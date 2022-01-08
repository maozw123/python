import paramiko
ssh = paramiko.SSHClient()
know_hosts = paramiko.AutoAddPolicy()
ssh.set_missing_host_key_policy(know_hosts)
ssh.connect(
    hostname='10.10.116.57',
    username='mzw',
    password='0321',
    port=22
)
# stdin, stdout, stderr = ssh.exec_command('ls')
# stdin,stdout,stderr=ssh.exec_command('touch 1.py')
stdin,stdout,stderr=ssh.exec_command('ls -n')
print(stdout.read().decode())
ssh.close()