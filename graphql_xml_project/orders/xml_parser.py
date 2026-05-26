import xmltodict


def parse_xml():

    with open("orders/sample_order.xml") as file:
        data = xmltodict.parse(file.read())

    return data