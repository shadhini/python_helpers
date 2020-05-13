import scrapy
from datetime import datetime, timedelta
COMMON_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def write_to_file(file_name, data):
    with open(file_name, 'w+') as f:
        f.write('\n'.join(data))


def append_to_file(file_name, data):
    with open(file_name, 'a+') as f:
        f.write('\n'.join(data))


def read_last_line(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        if len(lines) > 0:
            return lines[-1]
        else:
            None


class IFSSpider(scrapy.Spider):
    name = "ifs"

    def start_requests(self):
        urls = [
            'https://docs.google.com/spreadsheets/d/1zIgPU0ZlYkiKaavYAUcHKgEP95jdaMaf9ljJgRqtog4/htmlview#'
            # 'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        db_last_update = read_last_line('latest_update.txt')
        website_latest_update = response.xpath('//*[@id="614137682"]/div/table/tbody/tr[3]/td[1]/text()').getall()[0]

        if db_last_update is not None and db_last_update == website_latest_update:
            return
        else:
            append_to_file('latest_update.txt', ['', website_latest_update])

            # Mar 20 2020, 12:36 IST %Y-%m-%d %H:%M:%S
            website_latest_update_time  = datetime.strptime(website_latest_update.split(" IST")[0], "%b %d %Y, %H:%M")
            latest_update_time = website_latest_update_time.strftime(COMMON_DATE_TIME_FORMAT)

            patient_file_name = 'IFS_patient.csv'
            prefecture_file_name = 'IFS_prefecture.csv'

            patient_col_index = [1, 2, 6, 7, 8, 5, 4, 9, 11]
            patient_data = ['Patient_No, Confirmed_Date, Residence_City, Detected_City, Detected_Prefecture, Gender, Age, Status, Notes']

            length = len(response.xpath('//*[@id="0"]/div/table/tbody/tr/td[1]/text()').getall())

            for i in range(3, length+2):
                row = []
                for j in patient_col_index:
                    list = response.xpath('//*[@id="0"]/div/table/tbody/tr[{}]/td[{}]/text()'.format(i, j)).getall()
                    print(list)
                    if len(list) > 0:
                        row.append("\"" + list[0]+ "\"")
                    else:
                        if j==4:
                            row.append('0')
                        else:
                            row.append('NULL')

                patient_data.append(','.join(row))

            write_to_file(patient_file_name, patient_data)

            prefecture_col_index = [1, 4, 5, 6]
            prefecture_data = ['Prefecture, time, Cases, Recovered, Deaths']

            length = len(response.xpath('//*[@id="1399411442"]/div/table/tbody/tr/td[1]/text()').getall())

            for i in range(4, length + 2):
                row = []
                for j in prefecture_col_index:
                    list = response.xpath('//*[@id="1399411442"]/div/table/tbody/tr[{}]/td[{}]/text()'.format(i, j)).getall()
                    print(list)
                    if len(list) > 0:
                        row.append(str(list[0]))
                    else:
                        row.append(str(0))

                row.insert(1, latest_update_time)
                prefecture_data.append(','.join(row))

            write_to_file(prefecture_file_name, prefecture_data)



