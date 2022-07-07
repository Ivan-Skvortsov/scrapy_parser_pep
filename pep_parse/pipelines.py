import csv
from collections import defaultdict

from pep_parse.settings import PEP_STATUS_REPORT_FILE


class PepParsePipeline:
    """Counts PEP by statuses and store data in csv report file."""
    def open_spider(self, spider):
        self.pep_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.pep_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.pep_statuses.values())
        with open(PEP_STATUS_REPORT_FILE, 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Статус', 'Количество'])
            for status in self.pep_statuses.items():
                writer.writerow(status)
            writer.writerow(['Total', total])
