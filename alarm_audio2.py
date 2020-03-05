import time,datetime
from  pygame import mixer
#input_time=input("enter time")
def start_audio2(input_time):
    local=datetime.datetime.now().time()
    alarm=input_time.split(':')
    local_time=str(local).split(':')

    timediff_list=[]
    convert_sec=[3600,60,1]

    convert_alarm=[float(i)*float(j) for i,j in zip(alarm,convert_sec)]
    convert_time=[float(i)*float(j) for i,j in zip(local_time,convert_sec)]

    for i,j in zip(convert_alarm,convert_time):
        timediff_list.append(i-j)
    time_diff=sum(timediff_list)
    if time_diff<0:
        time_diff=time_diff+86400
    time.sleep(time_diff)

    mixer.init()
    mixer.music.load(r'C:\Users\Sheena\Shadow of the Beast (Guitar Edit).ogg')
    mixer.music.play()
    while mixer.music.getbusy():
        time.clock().tick(10)

def stop_audio2():
    mixer.music.stop()