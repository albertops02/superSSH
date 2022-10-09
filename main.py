from functions import connectkey
from paramiko import SSHClient, AutoAddPolicy, RSAKey
from scp import SCPClient
from os import path
import io
import sys

user = "frodo"
keypath = "/home/frodo/.ssh/Frodo"
remotehost = "192.168.1.108"
defaultpassword = "bolson"
ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy)

print("Welcome to the ssh master")
remotehost = input("Give your remote server IP (192.168.1.108): ") or remotehost
defaultpassword = input("Give the default password (bolson): ") or defaultpassword
user = input("Give the default username (frodo): ") or user
keypath = input("Give the path for the key (/home/frodo/.ssh/Frodo): ") or keypath
localpath = input("Give the path for the local file to copy (key path)") or keypath
extpath = input("Give the path where you want to put the file (key path)") or keypath
print("Will start the ssh connection")


connectkey(ssh, remotehost, user, keypath): ssh.connect(remotehost, username=user, pkey=keypath)
scp = SCPClient(ssh.get_transport())
scp.put(localpath, extpath)
ssh.exec_command("cat extpath")
scp.close()