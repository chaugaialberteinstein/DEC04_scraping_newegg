# DEC04_scraping_newegg
# Project 02

Bài toán: Sau khi bitcoin và các đồng tiền ảo sụt giảm, công ty có nhu cầu khảo sát thông tin về card đồ họa thông qua một website. Yêu cầu team Data Engineer collect và thống kê các thông tin tại danh mục trên website: [https://www.newegg.com](https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48?Tid=7709) để phía đội kinh doanh có cơ sở triển khai chiến dịch mới.

Mô tả cụ thể:

- Nguồn dữ liệu cần crawl là danh mục sau: https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48?Tid=7709
- Thông tin cần lấy:
    - ItemID
    - Title
    - Branding (Hãng)
    - Rating
    - Số lượng Rating
    - Price (Current Price) → Chuyển đổi dưới dạng number
    - Shipping (Free, Ko ship, hay mất phí)
    - Image URL
    - Các thông tin chi tiết về sản phẩm:
        - Max Resolution
        - DisplayPort
        - HDMI
        - DirectX
        - Model
- Số lượng: Toàn bộ các sản phẩm của 100 pages (khoảng 3600 sản phẩm)
- Thông tin sau khi collect đẩy vào một cơ sở dữ liệu MySQL
    - Thêm một cột total price dựa trên giá shipping
    - Thông tin chi tiết về sản phẩm lưu dưới dạng JSON
- Yêu cầu thống kê (visualize dữ liệu nếu có thể):
    - Các hãng đang cung cấp Card đồ họa, số lượng sản phẩm của mỗi hãng.
    - Phân bố giá của các sản phẩm (Mức giá phổ biến là bao nhiêu)
    - Phân bố giá sản phẩm theo hãng
    - Biểu diễn mối liên hệ giữa giá sản phẩm và rating của người dùng
 

Project Description: Scraping Graphic Card Products from Newegg Website using BeautifulSoup in Python
This project focuses on scraping graphic card product data from the Newegg website, specifically targeting multiple brands. The project aims to extract information from 100 pages, resulting in approximately 3600 items. The project workflow can be summarized as follows:

1. Extraction (main.py):

The Python script main.py is developed using an IDE such as PyCharm.
BeautifulSoup library is utilized to scrape data based on HTML tags. The Google Developer tools (F12) can assist in inspecting the webpage structure and identifying relevant tags for data extraction.
Exception handling is implemented for each function to handle any potential errors.
The scraped data is saved to an "item.csv" file.


2. Transformation and Visualization (Notebook):

The data extracted in the "item.csv" file is loaded into a Jupyter Notebook for further processing and analysis.
Data cleaning steps are applied to remove null and duplicate values from the dataset.
A new column called "total price" is created by combining relevant columns.
The cleaned data is then saved to a new file named "items.csv".
Additionally, a JSON file named "item_features.json" is generated, containing detailed information about the item features.
The data is visualized using interactive charts and plots in the Notebook to gain insights and facilitate reporting.


3. Loading to MySQL for Querying:

The "items.csv" file is reviewed in Excel to examine its contents.
The index column, if present, is removed before loading the data into MySQL.
A Python script is written in PyCharm to establish a connection with the MySQL database.
SQL queries can be executed on the loaded data to extract specific information.
By following this project workflow, users can scrape graphic card product data from the Newegg website, perform data transformation and visualization using a Jupyter Notebook, and even load the data into a MySQL database for further querying and analysis.
  
