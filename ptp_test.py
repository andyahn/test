import re
from netmiko import ConnectHandler
from time import sleep
from datetime import datetime
from os.path import expanduser
from os.path import isfile

def check_host(host_bool):
    check_ip = re.compile('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'); check_path = False; host_check = expanduser('~/host_check.txt').replace('\\', '/')
    if isfile(host_check) and host_bool:
        f = open(host_check, 'r', encoding='UTF8'); h_data = f.read().splitlines(); f.close()
        if len(h_data) == 3: 
            hostname = h_data[0]; username = h_data[1]; password = h_data[2]; print(f'Host IP : {hostname}\tUsername : {username}\tPassword : {password}'); print('1] 해당 정보 그대로 사용(or y)\t그 외] 다른 host 입력'); s = input()
            if s == '1' or s =='1]' or s == 'y': check_path = True
    if not check_path:
        print(); hostname = input('접속하려는 host의 ip를 입력해주세요 : ')
        while(True):
            if check_ip.search(hostname): break
            print('\n입력값이 잘못되었습니다.'); hostname = input('접속하려는 host의 ip를 입력해주세요 : ')
        username = input('username을 입력해주세요 : '); password = input('password를 입력해주세요 : ')
        try: f = open(host_check, 'w', encoding='UTF8'); f.write(hostname); f.write('\n'); f.write(username); f.write('\n');  f.write(password); f.write('\n');
        except: pass
    return hostname, username, password

def connect(platform, host, username, password):
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password); device.config_mode()
    return device

def loop_com(device, port, ptp_asy, diff, loop_count):
    for i in range(loop_count):
        command = f'configure port {port} ethernet ptp-asymmetry {ptp_asy-i*diff}'; output = device.send_config_set(command); print(); print (i+1, output)
        if 'MINOR: CLI ' in output: print(f'port {port}가 맞는지 확인해주세요'); return False
        sleep(2)
    return True

def inputs(check_port, check_asy):
    print(); port = input('port를 입력해주세요 : ')
    while True:
        if check_port.search(port): break
        print('\n입력값이 잘못되었습니다.'); port = input('port를 입력해주세요 : ')
    ptp_asy = input('5자리 이상 delay 시작값을 입력해주세요 (ns) : ')
    while True:
        if check_asy.match(ptp_asy): ptp_asy = int(ptp_asy); break
        print('\n입력값이 잘못되었습니다.'); ptp_asy = input('5자리 이상 delay 시작값을 입력해주세요 (ns) : ')
    return port, ptp_asy

def call(device, check_asy, port, ptp_asy, print_s, delay_time, loop_count):
    now = datetime.now(); print(now); print(print_s); loop_bool = loop_com(device,  port, ptp_asy, delay_time, loop_count); now = datetime.now(); print(now)
    return loop_bool

def after_check(loop_bool, device, check_port, check_asy, port, ptp_asy, print_s, delay_time, loop_count, platform):
    while True:
        print()
        if loop_bool:
            print('config를 다시 진행하시겠습니까?\n1] port 및 delay 미변경\t2] port 변경\t3]접속 host 및 port 변경\t그 외] 종료'); s = input()
            if s == '1' or s == '1]': call(device, check_asy, port, ptp_asy, print_s, delay_time, loop_count); continue
        else: 
            print('config를 다시 진행하시겠습니까?\n2] port 변경\t3]접속 host 및 port 변경\t그 외] 종료'); s = input()
            if s == '1' or s == '1]': print(f'현재 Port인 {port}는 사용이 불가하여, Port를 변경하여야 합니다.'); continue
        if s == '2' or s == '2]': port, ptp_asy = inputs(check_port, check_asy); loop_bool = call(device, check_asy, port, ptp_asy, print_s, delay_time, loop_count)
        elif s == '3' or s == '3]': device.disconnect(); host, username, password = check_host(False); device = connect(platform, host, username, password); port, ptp_asy = inputs(check_port, check_asy); loop_bool = call(device, check_asy, port, ptp_asy, print_s, delay_time, loop_count)
        else: device.disconnect(); break