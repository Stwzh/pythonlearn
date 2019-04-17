
from urllib import request
import re ,xlwt ,datetime,time
import urllib
keyname= "短裙"
key = urllib.request.quote(keyname)
headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
opener.addheaders = [headers]
urllib.request.install_opener(opener)

for i in range(0, 1):

    url = "https://s.taobao.com/search?q=" + key + "&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170628&ie=utf8"
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    pat = 'pic_url":"//(.*?)"'
    imagelist = re.compile(pat).findall(data)
    wzh = 'raw_title":"((.*?))"'
    xx = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    wordlist = re.compile(wzh).findall(xx)
workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
style.font = font
sheet1.write(0, 0, "序号", style)
sheet1.write(0, 1, "商品名称", style)
a = 0
for p in wordlist:
    sheet1.write(a + 1, 0, a + 1, style)
    sheet1.write(a + 1, 1, str(p[0]), style)
    a += 1

    if a == a:  # 判断列表是否遍历结束
        t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        t1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        sheet1.write(a + 2, 0, "采集时间", style)  # 在sheet1表尾行写入数据采集时间
        sheet1.write(a + 2, 1, t, style)  # 在sheet1表尾行写入数据采集时间

workbook.save("e:/wzh/data/淘宝商品" + str(t1) + ".xls")
print("--------商品数据写入excel文件成功--------")
for j in range(0, len(imagelist)):
    try:
        #print("抓取第" + str(j) + "张图片")
        thisimg = imagelist[j]
        thisimgurl = "http://" + thisimg
        file = "E:/wzh/photos/" + str(i) + str(j) + ".jpg"
        urllib.request.urlretrieve(thisimgurl, filename=file)
       # print("--------商品图片获取成功--------")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
                time.sleep(10)
    except Exception as e:
     print("exception:" + str(e))
    time.sleep(0)
print("------------商品图片获取成功-----------")
print("--------关于#"+keyname+"#的淘宝信息获取成功--------")
