import requests
from bs4 import BeautifulSoup
import urllib
import xlsxwriter


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }

def get_good_url(word):
    url_str = urllib.parse.quote(word)
    url = "https://search.jd.com/Search?keyword={}&enc=utf-8".format(url_str)
    return url


def get_html(url):
    html = requests.get(url, headers=headers)
    html.encoding = html.apparent_encoding
    soup = BeautifulSoup(html.text, 'lxml')
    return soup


def get_info(soup, good):
    titles = soup.find_all(class_="p-name p-name-type-2")
    prices = soup.find_all(class_="p-price")
    commits = soup.find_all(class_="p-commit")
    imgs = soup.find_all(class_="p-img")

    workbook = xlsxwriter.Workbook(good + '.xlsx') #创建新表
    worksheet = workbook.add_worksheet()
    
    bold = workbook.add_format({'bold': True})  #建立粗体格式
    
    # worksheet.write('A1', 'Title', bold)        #写入标题，粗体
    # worksheet.write('B1', 'Price', bold)
    # worksheet.write('C1', 'Commit', bold)
    # worksheet.write('D1', 'Link', bold)
    # worksheet.write('F1', 'Img', bold)
    worksheet.write('A1','商品名',bold)
    worksheet.write('B1','价格',bold)
    worksheet.write('C1','评价',bold)
    worksheet.write('D1','地址',bold)
    worksheet.write('E1','图片地址',bold)

    worksheet.set_column('A:A', 100)            #改变列宽度
    worksheet.set_column('B:B', 10)
    worksheet.set_column('C:C', 18)
    worksheet.set_column('D:D', 27)
    worksheet.set_column('F:F', 100)
    
    row = 1
    col = 0
    
    for title, price, commit, img in zip(titles, prices, commits, imgs):
        data = {
            'title' :   title.text.strip(),
            'price' :   price.text.strip(),
            'commit':   commit.text.strip(),
            'link'  :   img.find_all('a')[0].get("href"),  #链接的标签也在 img 标签里找
            'img'   :   img.find_all('img')[0].get("src")
            }
        #print(data)
        worksheet.write(row, col, data['title'])    #写入数据
        worksheet.write(row, col+1, data['price'])
        worksheet.write(row, col+2, data['commit'])
        worksheet.write(row, col+3, data['link'])
        worksheet.write(row, col+4, data['img'])
        row += 1
        
    workbook.close()
    
        

if __name__ == '__main__':
    good = input("请输入你要查询的商品：\n")
    link = get_good_url(good)
    html = get_html(link)
    get_info(html, good)