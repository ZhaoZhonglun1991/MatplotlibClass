import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import member
import datetime
from collections import Counter

plt.style.use('ggplot')
font1=FontProperties(fname=r"/Library/Fonts/Songti.ttc",size=20)
font2=FontProperties(fname=r"/Library/Fonts/Songti.ttc",size=10)

color_sequence = ['#1f77b4','#2ca02c','#d62728', '#9467bd', '#17becf',
                '#1f77b4','#2ca02c','#d62728', '#9467bd', '#17becf',
                '#1f77b4','#2ca02c','#d62728', '#9467bd', '#17becf',
                '#1f77b4','#2ca02c','#d62728', '#9467bd', '#17becf',
                '#1f77b4','#2ca02c','#d62728', '#9467bd', '#17becf',]

mem = member.member
name = [i['name'] for i in mem]
work = [i['work_experience'] for i in mem]
gender = [i['gender'] for i in mem]
genderCounter= Counter(gender)
age = [datetime.date.today().year-i['birthdate'].year for i in mem]
birthplace = [i['birthplace'][0:2] for i in mem]
birthplaceCounter= Counter(birthplace)


date = [0]*25
exp = [0]*25
rank = [0]*25
fig = [0]*28
ax = [0]*28

for i in range(0,25):
    date[i] = [j[0] for j in work[i]]
    dateStr = '\n'.join([str(j.year)+'年 ' for j in date[i]])
    exp[i] = [j[1] for j in work[i]]
    expStr = '\n'.join(exp[i])
    rank[i] = [j[2] for j in work[i]]
    fig[i],ax[i] = plt.subplots()
    fig[i].subplots_adjust(left=0.08,right=0.98,top=0.94,bottom=0.07)
    
    ax[i].plot(date[i], rank[i], lw=2.5,color=color_sequence[i],zorder=10)
    
    ax[i].set_title(name[i],fontproperties=font1)
    ax[i].set_xticks(date[i])
    labels = ax[i].get_xticklabels()
    plt.setp(labels, rotation=90, fontsize=10)
    if i ==10 or i == 17:
        ax[i].set_yticks(range(1, 17, 1))
        ax[i].set_ylim(0,16.5)
        ax[i].set_yticklabels([member.aRank[str(i)] for i in range(1,17)], fontproperties=font2) 
        ax[i].text(date[i][0], 16, dateStr, va= 'top', fontproperties= font2)
        ax[i].text(date[i][0]+datetime.timedelta(660), 16, expStr, va= 'top', fontproperties= font2)
      
    else:
        ax[i].set_ylim(0,18.5)
        ax[i].set_yticks(range(1, 19, 1))
        ax[i].set_yticklabels([member.gRank[str(i)] for i in range(1,19)], fontproperties=font2)
        ax[i].text(date[i][0], 18, dateStr, va= 'top', fontproperties= font2)
        ax[i].text(date[i][0]+datetime.timedelta(660), 18, expStr, va= 'top', fontproperties= font2)

fig[25],ax[25] = plt.subplots()
n,bins,patches= ax[25].hist(age,bins=range(53,69),align= 'left', rwidth=0.95)
ax[25].set_xlim(52.5,68.5)
ax[25].set_xticks(range(53,69))
ax[25].set_xticklabels(['<54']+[str(i) for i in range(54,68)]+['>67'])

fig[26],ax[26] = plt.subplots()
ax[26].set_prop_cycle('color', ['lightskyblue','skyblue','deepskyblue', 'dodgerblue', 'lightgreen','springgreen','lawngreen','navajowhite','orange','darkorange','plum','violet','m'])
patches, texts, autotexts=ax[26].pie([i[0] for i in sorted(zip(birthplaceCounter.values(),birthplaceCounter.keys()))],labels=[i[1] for i in sorted(zip(birthplaceCounter.values(),birthplaceCounter.keys()))], autopct='%1.1f%%',shadow=True, startangle=90)
plt.setp(texts, fontproperties= font2)

fig[27],ax[27] = plt.subplots()
ax[27].set_prop_cycle('color', ['salmon','dodgerblue'])
patches, texts, autotexts=ax[27].pie([i[0] for i in sorted(zip(genderCounter.values(),genderCounter.keys()))],labels=[i[1] for i in sorted(zip(genderCounter.values(),genderCounter.keys()))], autopct='%1.1f%%',shadow=True, startangle=90)
plt.setp(texts, fontproperties= font2)

plt.show()
