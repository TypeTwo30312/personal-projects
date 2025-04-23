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
import sys

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
            code = cells[0].text.strip()
            name = cells[1].text.strip()
            link_tag = cells[0].find("a")                   # hyperlink on the code is the correct one

            if link_tag:
                relative_link = html.unescape(link_tag["href"])
                full_link = base_url + relative_link
                municipality_list.append({
                    "code": code,
                    "name": name,
                    "link": full_link
                })

    return municipality_list

def clean_number(text):
    """Remove spaces and non-breaking spaces from numbers."""
    return text.strip().replace('\xa0', '').replace(' ', '')

def scrape_municipality_result(municipality):
    """Scrapes summary and vote results from one municipality result page."""
    page = get(municipality["link"])
    soup = BeautifulSoup(page.text, "html.parser")

    summary_table = soup.find_all("table", {"class": "table"})[0]

    voters_cell = summary_table.find("td", {"headers": "sa2"})
    envelopes_cell = summary_table.find("td", {"headers": "sa3"})
    valid_votes_cell = summary_table.find("td", {"headers": "sa6"})

    voters = clean_number(voters_cell.text) if voters_cell else None
    envelopes = clean_number(envelopes_cell.text) if envelopes_cell else None
    valid_votes = clean_number(valid_votes_cell.text) if valid_votes_cell else None

    ### Scrape party results
    votes = []
    party_names = []

    result_tables = soup.find_all("table", {"class": "table"})[1:3]  # second and third tables
    for table in result_tables:
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 5:  # result rows should have at least 5 columns Is this necessary?
                party_name = cells[1].text.strip()
                vote_count = clean_number(cells[2].text)
                if party_name:
                    party_names.append(party_name)
                    votes.append(vote_count)

    return {
        "code": municipality["code"],
        "name": municipality["name"],
        "voters": voters,
        "envelopes": envelopes,
        "valid_votes": valid_votes,
        "votes": votes,
        "party_names": party_names
    }
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

def main(district_name, filename):
    
    district_link = find_district_link(district_name)
    municipalities = get_municipality_links(district_link)
    municipality_results = []
    for municipality in municipalities:
        result = scrape_municipality_result(municipality)
        municipality_results.append(result)
    party_names = municipality_results[0]["party_names"]
    write_results_to_csv(filename, municipality_results, party_names)
    

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])