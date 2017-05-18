from dc_base_scrapers.xml_scraper import GmlScraper


stations_url = "https://webtest.rbkc.gov.uk/arcgis/services/LBHF/Administration/MapServer/WFSServer?service=WFS&version=1.1.0&request=GetFeature&typeNames=Administration%3APolling_Stations"
stations_fields = {
    '{WFS}OBJECTID': 'OBJECTID',
    '{WFS}POLLING_ST': 'POLLING_ST',
    '{WFS}POLLING_DI': 'POLLING_DI',
    '{WFS}POLLING__1': 'POLLING__1',
    '{WFS}POSTCODE': 'POSTCODE',
    '{WFS}WARD': 'WARD',
    '{WFS}LOCATION': 'LOCATION',
}

districts_url = "https://webtest.rbkc.gov.uk/arcgis/services/LBHF/Administration/MapServer/WFSServer?service=WFS&version=1.1.0&request=GetFeature&typeNames=Administration%3APolling_Districts"
districts_fields = {
    '{WFS}OBJECTID': 'OBJECTID',
    '{WFS}MAPKEY': 'MAPKEY',
    '{WFS}POLLING_ZO': 'POLLING_ZO',
    '{WFS}POLLING_ST': 'POLLING_ST',
}

council_id = 'E09000013'


stations_scraper = GmlScraper(stations_url, council_id, 'stations', stations_fields, 'OBJECTID')
stations_scraper.scrape()
districts_scraper = GmlScraper(districts_url, council_id, 'districts', districts_fields, 'OBJECTID')
districts_scraper.scrape()
