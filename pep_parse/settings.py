from pathlib import Path
from datetime import datetime as dt


DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
DATETIME = dt.now().strftime(DATETIME_FORMAT)

BASE_DIR = Path(__file__).parent
RESULTS_DIR = BASE_DIR / 'results'
PEP_LIST_REPORT_FILE = RESULTS_DIR / f'pep_{DATETIME}.csv'
PEP_STATUS_REPORT_FILE = RESULTS_DIR / f'status_summary_{DATETIME}.csv'

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    PEP_LIST_REPORT_FILE: {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
        'item_export_kwargs': {"include_headers_line": False}
    }
}
