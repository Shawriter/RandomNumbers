import bs4 as bs
import requests as rs
# Get random variables from random.org


def main():

    get_randomintegersets()


def get_randomintegersets():

    litaglist = []
    integerset_list_1 = []
    max = "10"  # Random max upper limit, min 1
    if len(max) == 3:
        numberstrlen = len(max) + 4
    if len(max) == 4:
        numberstrlen = len(max) + 5
    if len(max) == 5:
        numberstrlen = len(max) + 6

    url = 'https://www.random.org/integer-sets/?sets=10&num=1&min=1&max=' + max + '&seqnos= \
    on&commas=on&sort=on&order=index&format=html&rnd=new'

    headers = {'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 \
    (X11; Linux i686 AppleWebkit/537.17 (KHTML, like Gecko) \
    Chrome/24.0.1312.27 \
    Safari/537.17)'}

    try:
        s = rs.Session()
        s.headers.update(headers)

        truecookies = {'cookies': 'RDOSESSION="REPLACE WITH YOURS";\
        __cflb="REPLACE WITH YOURS"; \
        RDOPRIVACY=[true,false,false]'}

        content = s.get(url, cookies=truecookies)

        soup = bs.BeautifulSoup(content.text, 'html.parser')
        soup2 = soup.findAll('li')

        [litaglist.append(li.contents) for li in soup2]

        for num in litaglist:
            numstr = str(num)
            if len(numstr) <= numberstrlen:
                integerset_list_1.append(num)

            else:
                continue
    except Exception as e:
        raise e

    textfilewriter(integerset_list_1)


def textfilewriter(integerset_list_1):

    numbers_1 = "numbers_1"
    # print(integerset_list_1)
    try:
        with open(numbers_1 + ".txt", "w+") as txtfile:
            integerset_list_1.sort()
            for line in integerset_list_1:
                if line is not None:

                    txtfile.write(str(line))
                else:
                    continue
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()
