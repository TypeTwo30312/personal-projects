"""

project_3: třetí projekt do Engeto Online Python Akademie

author: Tomáš Vamberský

email: tomas.vambersky@protonmail.com

discord: TypeTwo

"""

from requests import get
from bs4 import BeautifulSoup
import csv
import html

def find_district_link(district):
    """Returns a link to the chosen districts page."""
    main_link = "https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    base_url = "https://www.volby.cz/pls/ps2017nss/"
    page = get(main_link)
    parsed_page = BeautifulSoup(page.text, features="html.parser")
    district_dict = {}
    rows = parsed_page.find_all("tr")
    print(rows)
    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 4:
            link_tag = cells[3].find("a")  # 4th <td> is link
            district_name = cells[1].text.strip() # second td is district name)
            if link_tag:
                relative_link = html.unescape(link_tag["href"]) # escaping the "&amp;"
                full_link = base_url + relative_link
                district_dict[district_name] = full_link
    print(district_dict[district])
    return district_dict[district]

find_district_link("Praha")
### first css selector table.table:nth-child(7) > tbody:nth-child(1) > tr:nth-child(3)