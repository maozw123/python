import paramiko

# 创建一个 ssh 客户端
ssh = paramiko.SSHClient()

# 创建ssh 白名单
know_hosts = paramiko.AutoAddPolicy()

# 加载ssh  白名单
ssh.set_missing_host_key_policy(know_hosts)

# 链接服务器
ssh.connect(
    hostname='10.10.116.57',
    username='mzw',
    password='0321',
    port=22
)
# 执行命令
# stdin, stdout, stderr = ssh.exec_command('ls')
# stdin,stdout,stderr=ssh.exec_command('touch 1.py')
stdin,stdout,stderr=ssh.exec_command('ls -n')
# stdin 标准输入 是一个文件对象
# stdout 标准输出 是一个文件对象
# stderr 标准错误 是一个文件对象 具有读权限
print(stdout.read().decode())
ssh.close()
