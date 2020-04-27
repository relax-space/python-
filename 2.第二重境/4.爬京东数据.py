import urllib.parse
from bs4 import BeautifulSoup
import requests
import xlsxwriter

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

def get_good_url(word):
    url_str = urllib.parse.quote(word)
    url = "https://search.jd.com/Search?keyword={}&enc=utf-8".format(url_str)
    urls = ("https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=4&page={}&s=1&click=0".format(url_str, i) for i in range(1,12,2))
    return urls
    return url 

def get_html(url):
    html = requests.get(url,headers=headers)
    html.encoding = html.apparent_encoding
    soup = BeautifulSoup(html.text,'lxml')
    return soup

def get_info(soup,good):
    titles = soup.find_all(class_="p-name p-name-type-2")
    prices = soup.find_all(class_="p-price")
    commits = soup.find_all(class_="p-commit")
    imgs = soup.find_all(class_="p-img")

    workbook = xlsxwriter.Workbook(good + '.xlsx')
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({'bold':True})

    worksheet.write('A1','商品名',bold)
    worksheet.write('B1','价格',bold)
    worksheet.write('C1','评价',bold)
    worksheet.write('D1','地址',bold)
    worksheet.write('E1','图片地址',bold)

    worksheet.set_column('A:A',100)
    worksheet.set_column('B:B',20)
    worksheet.set_column('C:C',20)
    worksheet.set_column('D:D',50)
    worksheet.set_column('E:E',100)

    row = 1
    rol = 0

    for title,price,commit,img in zip(titles,prices,commits,imgs):
        data ={
            'title' : title.text.strip(),
            'price' : price.text.strip(),
            'commit' : price.text.strip(),
            'link' : img.find_all('a')[0].get('href'),
            'img'  : img.find_all('img')[0].get("src")
            }
        #print(data)
        worksheet.write(row,rol,data['title'])
        worksheet.write(row,rol+1,data['price'])
        worksheet.write(row,rol+2,data['commit'])
        worksheet.write(row,rol+3,data['link'])
        worksheet.write(row,rol+4,data['img'])
        row +=1
    workbook.close()



if __name__ ==  '__main__':
    good = input("请输入你要查询的商品：\n")
    link = get_good_url(good)
    html = get_html(link)
    get_info(html,good)