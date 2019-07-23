# pip install paramiko

import paramiko

pk_path = "/home/shadhini/.ssh/uwcc-admin"
host = "104.198.0.87"
user="uwcc-admin"
# command = "python /home/uwcc-admin/db_scripts/test/hello.py"
command = "nohup /home/uwcc-admin/db_scripts/test/hello.sh &> /home/uwcc-admin/db_scripts/test//nohup.out"
# command = "whoami"


def ssh_command(ssh, command):
    ssh.invoke_shell()
    stdin, stdout, stderr = ssh.exec_command(command)
    for line in stdout.readlines():
        print(line)
    for line in stderr.readlines():
        print(line)


def run_remote_command(host, user, key, command):
    try:
        ssh = paramiko.SSHClient()
        print('Calling paramiko')
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, key_filename=key)

        ssh_command(ssh, command)
    except Exception as e:
        print('Connection Failed')
        print(e)
    finally:
        print("Close connection")
        ssh.close()


if __name__=='__main__':
    # user = input("Username:")
    # key = input("Public key full path:")
    # host = input("Target Hostname:")
    run_remote_command(host, user, pk_path, command)
