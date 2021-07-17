# case 2
import re
import ptp_test as ptp

host, username, password = ptp.check_host(True); platform = 'alcatel_sros'; check_port = re.compile('^(\d{1,2})[/](\w{1,3})[/](\w{1,3})'); check_asy = re.compile('\d{5,}')
device = ptp.connect(platform, host, username, password); port, ptp_asy = ptp.inputs(check_port, check_asy)
delay_time = 200; loop_count = 16; print_s = f'\nwindow (2초 간격)으로 계산되는 delay 를 PTSF 미 발동 조건인 250 ns 미만 변동 ({delay_time}ns)'; loop_bool = ptp.call(device, check_asy, port, ptp_asy, print_s, delay_time, loop_count)

ptp.after_check(loop_bool, device, check_port, check_asy, port, ptp_asy, print_s, delay_time, loop_count, platform)