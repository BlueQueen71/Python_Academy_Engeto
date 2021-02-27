import requests
from bs4 import BeautifulSoup
import csv
import traceback


def get_locations_list():
    url = input("PLease input url address from your required district: ").strip()
    soup = get_soup(url)

    cislo_lokace = get_locations_numbers(soup)
    jmeno_lokace = get_locations_names(soup)
    lokace_url = get_locations_links(soup)

    return list(zip(cislo_lokace, jmeno_lokace, lokace_url))

def get_soup(url):
    try:
        odp_server = requests.get(url)
    except:
        err = traceback.format_exc()
        return err
    else:
        return BeautifulSoup(odp_server.text, "html.parser")

def get_td_elements(soup, *args):
    elements = []

    for arg in args:
        elements += soup.select("td[headers='{}']".format(arg))

    return elements

def get_locations_names(soup):
    td_elements = get_td_elements(soup, 't1sa1 t1sb2', 't2sa1 t2sb2', 't3sa1 t3sb2')
    td_el = []

    for td in td_elements:
        td = td.text
        td_el.append(td)

    return td_el

def get_locations_numbers(soup):
    td_elements = get_td_elements(soup, "t1sa1 t1sb1", "t2sa1 t2sb1", "t3sa1 t3sb1")
    cislo_obce = []

    for td in td_elements:
        if a:= td.find("a"):
            cislo_obce.append(a.text)

    return cislo_obce

def get_locations_links(soup):
    td_elements = get_td_elements(soup, "t1sa1 t1sb1", "t2sa1 t2sb1", "t3sa1 t3sb1")
    odkaz_obce = []

    for td in td_elements:
        if a:= td.find('a'):
            odkaz_obce.append(a.get("href"))

    return odkaz_obce


def write_to_csv(lokace_list):
    file = input("Please, write the name of your file (without suffix): ").strip()
    url = "https://www.volby.cz/pls/ps2017nss/" + lokace_list[0][2]
    header_soup = get_soup(url)
    header = make_csv_header(header_soup)

    print("Processing locations, please wait...")

    with open("{}.csv".format(file), "w", encoding="utf-8") as f:
        csv_file = csv.writer(f)
        csv_file.writerow(header)

        for lokace in lokace_list:
            url = "https://www.volby.cz/pls/ps2017nss/" + lokace[2]
            soup = get_soup(url)
            lokace_vysledky = get_location_results(soup)
            csv_file.writerow([lokace[0], lokace[1]] + lokace_vysledky)

def make_csv_header(soup):
    header = ["Code", "City name", "Voters in the list", "Issued envelopes", "Valid votes", "Candidate parties"]
    kandidujici_strany = get_parties_names(soup)

    return header + kandidujici_strany

def get_parties_names(soup):
    td_elements = get_td_elements(soup, "t1sa1 t1sb2", "t2sa1 t2sb2")
    elements = []

    for element in td_elements:
        if element.text != "-":
            element = element.text
            elements.append(element)

    return elements

def get_location_results(soup):
    return get_info_values(soup) + get_parties_votes(soup)

def get_info_values(soup):
    vysledky_headers = ["sa2", "sa3", "sa6"]
    values = []

    for header in vysledky_headers:
        vysledky_element = soup.find("td", {"headers": "{}".format(header)})
        vysledky_element = vysledky_element.text
        vysledky_element = vysledky_element.replace("\xa0", "")
        values.append(int(vysledky_element))

    return values

def get_parties_votes(soup):
    td_elements = get_td_elements(soup, "t1sa2 t1sb3", "t2sa2 t2sb3")
    hlasy = []

    for element in td_elements:
        if element.text != '-':
            element = element.text.replace("\xa0", "")
            hlasy.append(int(element))

    return hlasy

def main():
    lokace = get_locations_list()
    write_to_csv(lokace)

main()

