# Web-Scraping-CNBC-Latest-News-Market-Card-Tickers
## Authors

- [@Ravish Kamath](https://github.com/RavishKamathStats)


## Acknowledgements

 - [Tech with Tim ](https://www.youtube.com/watch?v=NB8OceGZGjA&t=751s)



## Installation

Activate the virtual enviroment for faster web scraping

```bash
source venv/bin/activate
```
If you do not want to activate the enviroment then you can just: 

```bash
pip install -r requirements.txt
```
To 
```bash
python 
```
## Deployment

To complete the web scraping:

```bash
  cd scripts
  python web_scraping.py
```
These commands will run the web scraping on the CNBC website. MAKE note that it uses Google driver specified for MacOS arm64. If you are on a different operating system, replace the driver in the drivers directory with your specified driver. Please check the FAQ for more details on where to get the specified drivers. 


To run the data filtering 
```bash
python data_filter.py
```

You can view the processed data in the /data/processed_data/ directory. 

Enjoy!!!!
## FAQ

#### How do i get the specified driver for my operating system?

To get the specified driver, please click the link below

[@Google Drivers](https://googlechromelabs.github.io/chrome-for-testing)

Download the specific chromedriver required for your operating system, and then add it to the drivers folder found in this repository. 

Here is a video for help: 

[@ChromeDriver helpful link](https://www.youtube.com/watch?v=m4-Z5KqDHpU)


