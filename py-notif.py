import socket
import subprocess
import time

CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''


def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text])


ip = socket.gethostbyname('[ADDRESS]')
ip2 = socket.gethostbyname('[ADDRESS]')

while ip2 == ip:
  print('wait')
  time.sleep(5)
  ip2 = socket.gethostbyname('[ADDRESS]')


str_ip2 = str(ip2)
notify('changement d\'IP', str_ip2)

