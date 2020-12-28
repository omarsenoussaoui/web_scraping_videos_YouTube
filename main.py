from selenium import webdriver
import pandas as pd
url="https://www.youtube.com/channel/UC8tgRQ7DOzAbn9L7zDL8mLg/videos"
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get(url)
videos = driver.find_elements_by_class_name("style-scope ytd-grid-video-renderer")

videos_list=[]
for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    link = video.find_element_by_xpath('.//*[@id="video-title"]').get_attribute("href")
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    video_items={
        'title': title,
        'link': link,
        'views': views,
        'post_time': when
    }
    videos_list.append(video_items)

for x in range(len(videos_list)):
    print(videos_list[x])

