import os
from os.path import expanduser

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                pass
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.log' or ext == '.txt' :
                    check_filename = filename
                    if '_' in filename:
                        check_filename_list = filename.split('_')
                        check_filename = ''
                        for fn in range(1, len(check_filename_list)):
                            check_filename += check_filename_list[fn]
                    
                    #log_list.append(filename.replace(ext, ''))
                    if '전' in check_filename or '14' in check_filename:
                        #print(check_filename)
                        before = full_filename
                    elif '후' in check_filename or '19' in check_filename or '16' in check_filename:
                        #print(check_filename)
                        after = full_filename
        return before, after
    except PermissionError:
        pass

def check_diff(be_list, af_list):
    copy_af = af_list[:]
    iaf = len(copy_af)
    for daf in af_list[::-1]:
        iaf -=1
        for dbe in be_list:
            if daf in dbe:
                copy_af.pop(iaf)
            else:
                continue
    
    copy_be = be_list[:]
    ibe = len(copy_be)
    for dbe in be_list[::-1]:
        ibe -= 1
        for daf in af_list:
            if daf in dbe:
                copy_be.pop(ibe)
            else:
                continue
    
    return copy_af, copy_be

def find_start_index(data_list, find_start='# show port'):
    for i, d in enumerate(data_list):
        if find_start in d:
            return i
            
def finds_index_list(data_list, index, find_fir='--------------------------------', brk_str='Port Descriptions on Slot A'):
    finds_list = []
    for i, d in enumerate(data_list[index:]):
        if find_fir in d:
            finds_list.append(i)
        elif brk_str in d:
            break
    return finds_list

def find_port_check(finds_list, data_list, index, find_thi='======================'):
    port_list = []; port_state = {}; port_bool = True
    for i in finds_list:
        if port_bool:
            for d in data_list[index+i+1:]:
                if d == '\n' or find_thi in d or 'A/' in d or 'B/' in d:
                    if 'A/' in d or 'B/' in d:
                        port_bool = False
                    break
                data = d.replace('\n', '').split()
                port = data[0]
                port_list.append(port)
                #print(data)
                port_state[port] = f'{data[1]} {data[2]}'
    return port_list, port_state

def find_bgp_check(finds_list, data_list, index, find_thi='--------------------------------'):
    bgp_list = []; act = []; sent = []
    
    

#home = expanduser("~")
#dir_path =  home + '/Desktop/비교 log/'
dir_path =  'D:/Desktop/비교 log/'
before, after = search(dir_path)
print()
print('기존 파일 : ', before)
print('변경 파일 : ', after, end='\n\n')

fbe = open(before, 'r', encoding='UTF8')
databe = fbe.readlines()
fbe.close()

faf = open(after, 'r', encoding='UTF-8')
dataaf = faf.readlines()
faf.close()


be_index = find_start_index(databe)
finds_be_list = finds_index_list(databe, be_index)
port_be_list, port_be_state = find_port_check(finds_be_list, databe, be_index)


af_index = find_start_index(dataaf)
finds_af_list = finds_be_list = finds_index_list(dataaf, af_index)
port_af_list, port_af_state = find_port_check(finds_af_list, dataaf, af_index)


check = True
for i in range(len(port_be_list)):
    if not port_be_list[i] == port_af_list[i]:
        print('서로 다른 포트, 포트를 먼저 확인하세요 : ', port_be_list[i], port_af_list[i])
        check = False

print('='*95)
#print(port_be_state)
be_up_port = '14 up_port : '
af_up_port = '19 up_port : '
if check:
    for key in port_be_list:
        if not port_be_state[key] == port_af_state[key]:
            print(f'서로 다른 상태, 확인 필요 |\tport : {key:7s}   전 : {str(port_be_state[key]):18s}   후 : {str(port_af_state[key])}')
        if 'Up' in port_be_state[key]:
            be_up_port += f'{key}  '
        if 'Up' in port_af_state[key]:
            af_up_port += f'{key}  '

print(be_up_port); print(); print(af_up_port);
be_bgp_index = find_start_index(databe, 'BGP Summary')
finds_be_bgp_list = finds_index_list(databe, be_bgp_index)
bgp_be_list, bgp_be_state = find_bgp_check(finds_be_bgp_list, databe, be_index)

af_bgp_index = find_start_index(dataaf, 'BGP Summary')