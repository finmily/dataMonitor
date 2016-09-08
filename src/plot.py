import json, numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys

if len(sys.argv) != 2:
    print("USAGE: %s field" % sys.argv[0])
    exit(1)
field = sys.argv[1]

pkl_file = open('data.pkl', 'r')
datas = []
for line in pkl_file:
    timestamp = line.split('\t')[0]
    data = json.loads(line.split('\t')[1])
    datas.append((timestamp, data))

time_list = [one[0] for one in datas]
data_list = np.array([one[1][field] for one in datas])

N = len(time_list)


def format_date(x, pos=None):
    if not x % 1:
        thisind = np.clip(int(x), 0, N - 1)
        return time_list[thisind]
    else:
        return ''


ind = np.arange(N)
ind1 = np.arange(N + 3)

fig = plt.figure()
plt.xlabel("Time")
plt.ylabel("Num")
plt.title("PLOT")
ax = fig.add_subplot(111)
ax.plot(ind, data_list, 'o-', label=str(field))
ax.plot(ind1, ind1, '-', color='white')
datadotxy = tuple(zip(ind, data_list + 1))
for dotxy in datadotxy:
    ax.annotate(str(int(dotxy[1] - 1)), xy=dotxy)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
fig.autofmt_xdate()
plt.legend()
plt.show()
