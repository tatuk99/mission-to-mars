#!/usr/bin/env python
# coding: utf-8

# In[108]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[109]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[110]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[111]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[112]:


slide_elem.find('div', class_='content_title')


# In[113]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[114]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[115]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[116]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[117]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[118]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[119]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[120]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[121]:


df.to_html()


# In[122]:


browser.quit()


# In[123]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[124]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# # Visit the NASA Mars News Site

# In[125]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)


# In[126]:


# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[127]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')


# In[128]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[129]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # JPL Space Images Featured Image

# In[130]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[131]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[132]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[133]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[134]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # Mars Facts

# In[135]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


# In[136]:


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles


# In[137]:


### Hemispheres


# In[138]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[139]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[140]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    hemisphere_names = {}
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.find_link_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemisphere_names["img_url"] = img_url
    hemisphere_names["title"] = title
    hemisphere_image_urls.append(hemisphere_names)
    browser.back()


# In[141]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[142]:


# 5. Quit the browser
browser.quit()


# In[ ]:




