import random,webbrowser,datetime,time
# input_time=input("enter time")

def start_video(input_time):
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
    with open("web.txt","r") as fp:
         read_contents=fp.read()
         l=read_contents.split("\n")
         random_choice=random.choice(l)
         webbrowser.open(random_choice,new=2)
    return