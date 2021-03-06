import numpy as np
import matplotlib.pyplot as plt
import datetime

def pro(a,b,c):
    pa= a/(a+b+c)
    pb = b / (a + b + c)
    pc = c / (a + b + c)
    return [pa,pb,pc]
#pro function to cal the proportion of three counts
f = open("alltweets.txt","r")   # set open object

a=0
b=0
c=0
d=[]
dd={}
for line in f.readlines():  # read a line in file
        if "datetime.datetime(2020, 2, 1" in line or "datetime.datetime(2020, 2, 2" in line:  # find the line has the date
            x=eval(line)            # make a line into a dictionary
            if 'positive' in x['sentiment']:
                a=a+1;              # a is  positive  count
            if 'negative' in x['sentiment']:
                b=b+1;              #b is negative count
            if 'neutral' in x['sentiment'] :
                c=c+1;             #c is neutural count
d=pro(a,b,c)           # cal proportion
dd['2.1']=d          # make the proportion into  a dictionary
a,b,c=0,0,0       #reset parameter
d=[]
f.close()

# the process is same as first block
f = open("alltweets.txt","r")
for line in f.readlines():
    if "datetime.datetime(2020, 2, 3" in line \
    or "datetime.datetime(2020, 2, 4" in line \
    or "datetime.datetime(2020, 2, 5" in line \
    or "datetime.datetime(2020, 2, 6" in line \
    or "datetime.datetime(2020, 2, 7" in line \
    or "datetime.datetime(2020, 2, 8" in line \
    or "datetime.datetime(2020, 2, 9" in line:
        y = eval(line)
        if 'positive' in y['sentiment']:
            a = a + 1;
        if 'negative' in y['sentiment']:
            b = b + 1;
        if 'neutral' in y['sentiment']:
            c = c + 1;
d = pro(a, b, c)
dd['2.3'] = d
a,b,c=0,0,0
d=[]
f.close()


# the process is same as first block
f = open("alltweets.txt","r")
for line in f.readlines():
    if "datetime.datetime(2020, 2, 10" in line \
    or "datetime.datetime(2020, 2, 11" in line \
    or "datetime.datetime(2020, 2, 12" in line \
    or "datetime.datetime(2020, 2, 13" in line \
    or "datetime.datetime(2020, 2, 14" in line \
    or "datetime.datetime(2020, 2, 15" in line \
    or "datetime.datetime(2020, 2, 16" in line:
        y = eval(line)
        if 'positive' in y['sentiment']:
            a = a + 1;
        if 'negative' in y['sentiment']:
            b = b + 1;
        if 'neutral' in y['sentiment']:
            c = c + 1;
d = pro(a, b, c)
dd['2.10'] = d
a,b,c=0,0,0
d=[]
f.close()

# the process is same as first block
f = open("alltweets.txt","r")
for line in f.readlines():
    if "datetime.datetime(2020, 2, 17" in line \
    or "datetime.datetime(2020, 2, 18" in line \
    or "datetime.datetime(2020, 2, 19" in line \
    or "datetime.datetime(2020, 2, 20" in line \
    or "datetime.datetime(2020, 2, 21" in line \
    or "datetime.datetime(2020, 2, 22" in line \
    or "datetime.datetime(2020, 2, 23" in line:
        y = eval(line)
        if 'positive' in y['sentiment']:
            a = a + 1;
        if 'negative' in y['sentiment']:
            b = b + 1;
        if 'neutral' in y['sentiment']:
            c = c + 1;
d = pro(a, b, c)
dd['2.17'] = d
a,b,c=0,0,0
d=[]
f.close()

# the process is same as first block
f = open("alltweets.txt","r")
for line in f.readlines():
    if "datetime.datetime(2020, 2, 24" in line \
    or "datetime.datetime(2020, 2, 25" in line \
    or "datetime.datetime(2020, 2, 26" in line \
    or "datetime.datetime(2020, 2, 27" in line \
    or "datetime.datetime(2020, 2, 28" in line \
    or "datetime.datetime(2020, 2, 29" in line \
    or "datetime.datetime(2020, 3, 1" in line:
        y = eval(line)
        if 'positive' in y['sentiment']:
            a = a + 1;
        if 'negative' in y['sentiment']:
            b = b + 1;
        if 'neutral' in y['sentiment']:
            c = c + 1;
d = pro(a, b, c)
dd['2.24'] = d
a,b,c=0,0,0
d=[]
f.close()

# the process is same as first block
f = open("alltweets.txt","r")
for line in f.readlines():
    if "datetime.datetime(2020, 3, 2" in line \
    or "datetime.datetime(2020, 3, 3" in line \
    or "datetime.datetime(2020, 3, 4" in line \
    or "datetime.datetime(2020, 3, 5" in line \
    or "datetime.datetime(2020, 3, 6" in line \
    or "datetime.datetime(2020, 3, 7" in line \
    or "datetime.datetime(2020, 3, 8" in line:
        y = eval(line)
        if 'positive' in y['sentiment']:
            a = a + 1;
        if 'negative' in y['sentiment']:
            b = b + 1;
        if 'neutral' in y['sentiment']:
            c = c + 1;
d = pro(a, b, c)
dd['3.2'] = d
a,b,c=0,0,0
d=[]
f.close()

# the process is same as first block
f = open("alltweets.txt","r")
for line in f.readlines():
    if "datetime.datetime(2020, 3, 9" in line \
    or "datetime.datetime(2020, 3, 10" in line \
    or "datetime.datetime(2020, 3, 11" in line \
    or "datetime.datetime(2020, 3, 12" in line \
    or "datetime.datetime(2020, 3, 13" in line \
    or "datetime.datetime(2020, 3, 14" in line \
    or "datetime.datetime(2020, 3, 15" in line:
        y = eval(line)
        if 'positive' in y['sentiment']:
            a = a + 1;
        if 'negative' in y['sentiment']:
            b = b + 1;
        if 'neutral' in y['sentiment']:
            c = c + 1;
d = pro(a, b, c)
dd['3.9'] = d
a,b,c=0,0,0
d=[]
f.close()

# the process is same as first block
f = open("alltweets.txt","r")
for line in f.readlines():
    if "datetime.datetime(2020, 3, 16" in line \
    or "datetime.datetime(2020, 3, 17" in line \
    or "datetime.datetime(2020, 3, 18" in line \
    or "datetime.datetime(2020, 3, 19" in line \
    or "datetime.datetime(2020, 3, 20" in line \
    or "datetime.datetime(2020, 3, 21" in line \
    or "datetime.datetime(2020, 3, 22" in line:
        y = eval(line)
        if 'positive' in y['sentiment']:
            a = a + 1;
        if 'negative' in y['sentiment']:
            b = b + 1;
        if 'neutral' in y['sentiment']:
            c = c + 1;
d = pro(a, b, c)
dd['3.16'] = d
a,b,c=0,0,0
d=[]
f.close()

# the process is same as first block
f = open("alltweets.txt","r")
for line in f.readlines():
    if "datetime.datetime(2020, 3, 23" in line \
    or "datetime.datetime(2020, 3, 24" in line \
    or "datetime.datetime(2020, 3, 25" in line \
    or "datetime.datetime(2020, 3, 26" in line \
    or "datetime.datetime(2020, 3, 27" in line \
    or "datetime.datetime(2020, 3, 28" in line \
    or "datetime.datetime(2020, 3, 29" in line:
        y = eval(line)
        if 'positive' in y['sentiment']:
            a = a + 1;
        if 'negative' in y['sentiment']:
            b = b + 1;
        if 'neutral' in y['sentiment']:
            c = c + 1;
d = pro(a, b, c)
dd['3.23'] = d
a,b,c=0,0,0
d=[]
f.close()

# the process is same as first block
f = open("alltweets.txt","r")
for line in f.readlines():
    if "datetime.datetime(2020, 3, 30" in line \
    or "datetime.datetime(2020, 3, 31" in line \
    or "datetime.datetime(2020, 4, 1" in line \
    or "datetime.datetime(2020, 4, 2" in line \
    or "datetime.datetime(2020, 4, 3" in line \
    or "datetime.datetime(2020, 4, 4" in line \
    or "datetime.datetime(2020, 4, 5" in line:
        y = eval(line)
        if 'positive' in y['sentiment']:
            a = a + 1;
        if 'negative' in y['sentiment']:
            b = b + 1;
        if 'neutral' in y['sentiment']:
            c = c + 1;
d = pro(a, b, c)
dd['3.30'] = d
a,b,c=0,0,0
d=[]
f.close()

# the process is same as first block
f = open("alltweets.txt","r")
for line in f.readlines():
    if "datetime.datetime(2020, 4, 6" in line \
    or "datetime.datetime(2020, 4, 7" in line \
    or "datetime.datetime(2020, 4, 8" in line \
    or "datetime.datetime(2020, 4, 9" in line \
    or "datetime.datetime(2020, 4, 10" in line \
    or "datetime.datetime(2020, 4, 11" in line \
    or "datetime.datetime(2020, 4, 12" in line:
        y = eval(line)
        if 'positive' in y['sentiment']:
            a = a + 1;
        if 'negative' in y['sentiment']:
            b = b + 1;
        if 'neutral' in y['sentiment']:
            c = c + 1;
d = pro(a, b, c)
dd['4.6'] = d
a,b,c=0,0,0
d=[]
f.close()

# the process is same as first block
f = open("alltweets.txt","r")
for line in f.readlines():
    if "datetime.datetime(2020, 4, 13" in line \
    or "datetime.datetime(2020, 4, 14" in line \
    or "datetime.datetime(2020, 4, 15" in line \
    or "datetime.datetime(2020, 4, 16" in line \
    or "datetime.datetime(2020, 4, 17" in line :
        y = eval(line)
        if 'positive' in y['sentiment']:
            a = a + 1;
        if 'negative' in y['sentiment']:
            b = b + 1;
        if 'neutral' in y['sentiment']:
            c = c + 1;
d = pro(a, b, c)
dd['4.13'] = d
a,b,c=0,0,0
d=[]
f.close()

print(dd)


#make line graph
import matplotlib.pyplot as plt

x_data = ['2.1-2.2', '2.3-2.9', '2.10-2.16', '2.17-2.23', '2.24-3.1', '3.2-3.8', '3.9-3.15','3.16-3.22','3.23-3.29','3.30-4.5','4.6-4.12','4.13-4.17']
y_data1 = [dd['2.1'][0], dd['2.3'][0], dd['2.10'][0],  dd['2.17'][0],  dd['2.24'][0],  dd['3.2'][0],  dd['3.9'][0],dd['3.16'][0],dd['3.23'][0],dd['3.30'][0],dd['4.6'][0],dd['4.13'][0]]
y_data2 = [dd['2.1'][1], dd['2.3'][1], dd['2.10'][1],  dd['2.17'][1],  dd['2.24'][1],  dd['3.2'][1],  dd['3.9'][1],dd['3.16'][1],dd['3.23'][1],dd['3.30'][1],dd['4.6'][1],dd['4.13'][1]]
y_data3 = [dd['2.1'][2], dd['2.3'][2], dd['2.10'][2],  dd['2.17'][2],  dd['2.24'][2],  dd['3.2'][2],  dd['3.9'][2],dd['3.16'][2],dd['3.23'][2],dd['3.30'][2],dd['4.6'][2],dd['4.13'][2]]
#x-axis is date y-axis is proportion of three kinds of sentiment
figsize = 11,9
figure, ax = plt.subplots(figsize=figsize)
colors1 = '#6D6D6D'
plt.title('Weekly sentiment proportion',color = colors1,fontsize = 25)
plt.xlabel('Date',fontsize=20)
plt.ylabel('Proportion',fontsize=20)

plt.plot(x_data, y_data1, color='red', linewidth=2.0, linestyle='-',label='Positive' )
plt.plot(x_data, y_data2, color='green', linewidth=2.0, linestyle='-',label='Negative')
plt.plot(x_data, y_data3, color='blue', linewidth=2.0, linestyle='-',label='Neutral')
plt.legend()
plt.tick_params(labelsize=12)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
plt.savefig('all day.png',dpi = 400)
plt.show()



f = open("alltweets.txt","r")
p=0
for line in f.readlines():
        p=p+1
print(p)    # print number of tweets
f.close()


