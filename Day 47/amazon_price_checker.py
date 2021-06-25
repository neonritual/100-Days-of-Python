from bs4 import BeautifulSoup
import requests

#Set HTTP Headers to pass along to Amazon.
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.285",
    "Accept-Language": "en-US,en;q=0.9"
}

# Def. function to send email alerting to a new low price.
def send_email():
    import smtplib

    my_email = "###Insert Email Login Here"
    password = "###Insert Email Password Here"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="### Insert the FROM Email here.",
                            msg=f"Subject: Low Price Alert!\n\n  Newest Apple MacBook Pro (16 inch, 16GB RAM, 512GB Storage, 2.6GHz Intel Core i7 Processor) - Space Gray"
                                f" is now {raw_price_data}! \n https://www.amazon.co.jp/dp/B081GH8ZXM/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=f52a2bd45a211a9e851a9edb8ea6dea9&hsa_cr_id=4822448240503&pd_rd_plhdr=t&pd_rd_r=13bc5633-7dc2-43e7-b377-f9b1eb11b806&pd_rd_w=sgpIb&pd_rd_wg=xr2At&ref_=sbx_be_s_sparkle_mcd_asin_0_img")


# Get data from Macbook Pro listing on Amazon.co.jp
response = requests.get("https://www.amazon.co.jp/dp/B081GH8ZXM/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=f52a2bd45a211a9e851a9edb8ea6dea9&hsa_cr_id=4822448240503&pd_rd_plhdr=t&pd_rd_r=13bc5633-7dc2-43e7-b377-f9b1eb11b806&pd_rd_w=sgpIb&pd_rd_wg=xr2At&ref_=sbx_be_s_sparkle_mcd_asin_0_img", headers=headers)
amazon_response = response.text

# Pass data into Beautiful Soup and find the price.
soup = BeautifulSoup(amazon_response, "html.parser")
raw_price_data_in_html = soup.find(id="priceblock_ourprice")

# Take out the price text from the html line.
raw_price_data = raw_price_data_in_html.getText()

# Change the price to a correctly formatted integer by removing the , and yen symbol.
todays_price = int(raw_price_data.strip("￥").replace(",", ""))
print(todays_price)

# The price I want to know if it drops to.
looking_for_price = 200000

# If today's price is lower than or equal to my buy price above, I send an email to alert me.
if looking_for_price >= todays_price:
    send_email()

