# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import urllib2
import os
import sys
from string import Template


URL_TMPLATE = Template('http://www.pixiv.net/member_illust.php?mode=medium&illust_id=${illust_id}')


pixiv_illust_id = sys.argv[1]

page_url = URL_TMPLATE.substitute(illust_id=pixiv_illust_id)
response = urllib2.urlopen(page_url)

soup = BeautifulSoup(response.read())

user_data = soup.find("div", {"class": "userdata"})

img_title = user_data.h1.contents[0]
img_author = user_data.h2.a.contents[0]
img_url = soup.find("div", {"class": "img-container"}).a.img['src']

print 'Downloading %s by %s' % (img_title, img_author)

img_request = urllib2.Request(img_url)
img_request.add_header('Referer', 'http://www.pixiv.net/')
img_data = urllib2.urlopen(img_request).read()

img_extension = os.path.splitext(img_url)[1][1:]
img_filename = '%s_%s.%s' % (img_author, img_title, img_extension)

img_file = open(img_filename, 'wb')
img_file.write(img_data)
img_file.close()

print 'Saved as %s' % (img_filename)
