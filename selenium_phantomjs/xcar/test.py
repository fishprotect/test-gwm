#
from scrapy.selector import Selector
def count(content):
    cou = 0
    for i in content:
        cou += 1
    print(cou)
def css_all_text(content):
    s = ''
    cs = content.css('*')
    for i in cs:
        text = i.css('::text').extract()
        if text:
            for i in text:
                s = s+i.strip()
    return s

with open('res.html','r',encoding='gb2312',errors='ignore') as f:
    html = f.read()
sel = Selector(text=html)
title = sel.css('title::text').extract_first()
print(title)
row_title = sel.css('tr#base_title > td[id^=mod_] >  a::text').extract()
print(row_title)
content = sel.css('.para_box#para_box>table[id^=base_]') # 16
for column_titles in content:
    titles = column_titles.css('tr')                        # 14
    count(titles)
    for t in titles:
        title = css_all_text(t.css('td.title'))
        print(title)
        detail_content = t.css('td:not(.title)')
        for j in detail_content:
            text = css_all_text(j)
            # text = j.css('::text').extract_first().strip()
            print(text)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    break
         
count(content)