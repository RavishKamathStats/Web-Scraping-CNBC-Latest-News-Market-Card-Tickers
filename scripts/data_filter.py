import csv
import lxml
import os
from bs4 import BeautifulSoup

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
raw_data_directory = os.path.join(parent_directory, "data/raw_data")
raw_data_path = os.path.join(raw_data_directory, "web_data.html")
processed_data_path = os.path.join(parent_directory, "data/processed_data")

with open(raw_data_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')

market_data = []
latest_news_data = []

# Filtering out Specific Market Data
market_parent = soup.find(id='market-data-scroll-container')

if market_parent:
    market_banners = market_parent.find_all(class_= 'MarketCard-container')

    for banners in market_banners:
        symbol = banners.select_one('.MarketCard-symbol').text.strip() if banners.select_one('.MarketCard-symbol') else "N/A"
        stock_pos = banners.select_one('.MarketCard-stockPosition').text.strip() if banners.select_one('.MarketCard-stockPosition') else "N/A"
        chang_pc = banners.select_one('.MarketCard-changesPct').text.strip() if banners.select_one('.MarketCard-changesPct') else "N/A"
        market_data.append([symbol, stock_pos, chang_pc])

else:
    print("Market parent container not found")

# Filtering Specific News Data
latest_news_parent = soup.find(class_='LatestNews-list')

if latest_news_parent:
    latest_news_items = latest_news_parent.find_all(class_='LatestNews-item')
    
    for news in latest_news_items:
        time_stamp = news.select_one('.LatestNews-timestamp').text.strip() if news.select_one('.LatestNews-timestamp') else "N/A"  
        title = news.find('a')['title'] if news.find('a') and 'title' in news.find('a').attrs else "N/A"
        link = news.find('a')['href'] if news.find('a') and 'href' in news.find('a').attrs else "N/A"
        latest_news_data.append([time_stamp, title, link])

else:
    print("Latest news parent container not found")

os.makedirs(processed_data_path, exist_ok = True)

market_csv_path = os.path.join(processed_data_path, "market_data.csv")
print("Creating csv file")
with open(market_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    print("uploading data to csv")
    csv_writer.writerow(['Symbol', 'Stock Postion', 'Change Pct'])
    csv_writer.writerows(market_data)
print("Market data csv file successfully completed")

news_csv_path = os.path.join(processed_data_path, "news_data.csv")
print("Creating csv file")
with open(news_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    print("uploading data to csv")
    csv_writer.writerow(['Timestamp', 'Title', 'Link'])
    csv_writer.writerows(latest_news_data)
print("News data csv file successfully completed")
