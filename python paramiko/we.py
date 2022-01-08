import paramiko

## 实例化一个对象
ssh = paramiko.Transport(
sock=("192.168.49.170",22)
)
# 创建链接
ssh.connect(
username="root",
password="111111",
)
sftp = paramiko.SFTPClient.from_transport(ssh)

# 上传文件
# sftp.put("test.py","/root/hello/hello.p")
# 下载文件
sftp.get("/root/hello/hello.p",'hello.py')

sftp.close()