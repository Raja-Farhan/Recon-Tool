import dns.resolver
from utils.logger import setup_logger

logger = setup_logger()

def run(domain):
    record_types = ['A', 'MX', 'TXT', 'NS']
    records = {}
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record, raise_on_no_answer=False)
            records[record] = [rdata.to_text() for rdata in answers] if answers else []
            logger.info(f"Fetched {len(records[record])} {record} records for {domain}")
        except Exception as e:
            logger.warning(f"Could not fetch {record} records: {e}")
            records[record] = []
    return records
