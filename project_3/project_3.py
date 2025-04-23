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
    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 4:
            link_tag = cells[3].find("a")  # 4th <td> is link
            district_name = cells[1].text.strip() # second td is district name)
            if link_tag:
                relative_link = html.unescape(link_tag["href"]) # escaping the "&amp;"
                full_link = base_url + relative_link
                district_dict[district_name] = full_link
    return district_dict[district]

def get_town_links(district_link):
    """Return a list of dicts with town code, name, and result page link from the given district link."""
    base_url = "https://www.volby.cz/pls/ps2017nss/"
    page = get(district_link)
    soup = BeautifulSoup(page.text, "html.parser")

    town_list = []

    rows = soup.find_all("tr")

    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 3:
            code = cells[0].text.strip()                    # first <td>: town code
            name = cells[1].text.strip()                    # second <td>: town name
            link_tag = cells[2].find("a")                   # third <td>: link to result page (adjust index if needed)

            if link_tag:
                relative_link = html.unescape(link_tag["href"])
                full_link = base_url + relative_link
                town_list.append({
                    "code": code,
                    "name": name,
                    "link": full_link
                })

    return town_list

district_link = find_district_link("Ostrava-město")
towns = get_town_links(district_link)
print(towns)
