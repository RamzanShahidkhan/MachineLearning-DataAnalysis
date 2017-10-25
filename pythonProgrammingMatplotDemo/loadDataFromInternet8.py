import matplotlib.pyplot as plt
import numpy as np
import urllib
import datetime as dt
import matplotlib.dates as mdates


def bytespdate2num(fmt,encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s= b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graph_data():
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data =[]
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt('pythonProgramFileCode_TSLA.txt',
                                                         delimiter=',',
                                                         unpack=True)
             # %Y = full Year. 2015 # %y = partial year 15  # %m = number month
              # %d = number day  # %H = hour # %M = minutes # %S = seconds
            # 12-06-2014  # %m-%d-%Y

    dateconv =np.vectorize(dt.datetime.fromtimestamp())
    date = dateconv(date)

    '''
    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                         delimiter=',',
                                                      converters={0: bytespdate2num('%Y-%m-%d')})
                                                      '''
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True)  # , color='g', linestyle='-', linewidth=5)

    ax1.plot_date(date, closep, '-', label='Price')
    #plt.plot_date(date,closep,'-',label='price')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title("Interesting Graph\n check it out")
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()

graph_data()