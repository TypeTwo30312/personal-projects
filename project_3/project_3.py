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
import re

import unicodedata

def clean_number(text):
    """Remove all spaces, non-breaking spaces, and narrow spaces between digits."""
    return text.strip().replace('\xa0', '').replace(' ', '').replace('\u202f', '')



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

def get_municipality_links(district_link):
    """Return a list of dicts with municipality code, name, and result page link from the given district link."""
    base_url = "https://www.volby.cz/pls/ps2017nss/"
    page = get(district_link)
    soup = BeautifulSoup(page.text, "html.parser")

    municipality_list = []

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
                municipality_list.append({
                    "code": code,
                    "name": name,
                    "link": full_link
                })

    return municipality_list

def extract_summary_data(soup):
    summary_table = soup.find_all("table", {"class": "table"})[0]  # first table is the summary
    rows = summary_table.find_all("tr")

    for row in rows:
        voters_cell = row.find("td", {"headers": "sa2"})
        envelopes_cell = row.find("td", {"headers": "sa3"})
        valid_votes_cell = row.find("td", {"headers": "sa6"})

        if voters_cell:
            voters = clean_number(html.unescape(voters_cell.text))
        if envelopes_cell:
            envelopes = clean_number(html.unescape(envelopes_cell.text))
        if valid_votes_cell:
            valid_votes = clean_number(html.unescape(valid_votes_cell.text))


    return {
        "voters": voters,
        "envelopes": envelopes,
        "valid_votes": valid_votes
    }

def scrape_municipality_result(municipality):

    page = get(municipality["link"])
    soup = BeautifulSoup(page.text, "html.parser")
    return extract_summary_data(soup)


    """### return {
        "code": municipality["code"],
        "name": municipality["name"],
        "voters": voters,
        "envelopes": envelopes,
        "valid_votes": valid_votes,
        "votes": votes,
        "party_names": party_names  # keep for now to confirm vote order
    }"""

def write_results_to_csv(filename, municipality_results, party_names):
    """Writes municipality results to a CSV file with one line per municipality."""
    header = ["kód obce", "název obce", "voliči v seznamu", "vydané obálky", "platné hlasy"] + party_names

    with open(filename, "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for municipality in municipality_results:
            row = [
                municipality["code"],
                municipality["name"],
                municipality["voters"],
                municipality["envelopes"],
                municipality["valid_votes"]
            ] + municipality["votes"]
            writer.writerow(row)
municipality_results = [
    {
        "code": "CZ0714",
        "name": "Přerov",
        "voters": "54000",
        "envelopes": "39000",
        "valid_votes": "38500",
        "votes": ["10000", "15000", "5000"]
    },
    {
        "code": "CZ0214",
        "name": "Perov",
        "voters": "54000",
        "envelopes": "39000",
        "valid_votes": "38500",
        "votes": ["10000", "15000", "5000"]
    }]
party_names = ["ODS", "ANO 2011", "ČSSD"]
write_results_to_csv("fdg.csv", municipality_results, party_names)
"""district_link = find_district_link("Ostrava-město")
municipalities = get_municipality_links(district_link)
for municipality in municipalities:
    result = scrape_municipality_result(municipality)
    print(result)"""
