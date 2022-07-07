import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Parse peps.python.org, get all PEP data: number, name, status."""
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org']

    def parse(self, response):
        """Parse main page, get all links to all PEP pages."""
        numerical_index_table = response.css('section[id="numerical-index"]')
        pep_links = numerical_index_table.css(
            'a.pep.reference.internal::attr("href")'
        )
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Parse single PEP page, get PEPs number, name and status."""
        pep_title = response.css('h1.page-title::text').get()
        pattern = re.compile(r'PEP\s(?P<pep_number>\d+)\s–\s(?P<pep_name>.+)')
        num_and_name = re.search(pattern, pep_title)
        status = response.css('dt:contains("Status") + dd::text').get()
        yield PepParseItem(
            number=int(num_and_name.group('pep_number')),
            name=num_and_name.group('pep_name'),
            status=status
        )
