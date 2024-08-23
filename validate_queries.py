import csv
from typing import List, Dict
from utils.connection import get_salesforce_connection
from utils.soql import execute_soql_query
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_soql_queries(file_path: str) -> List[str]:
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader if row]

def execute_queries(sf_conn, queries: List[str], max_runs: int = 8) -> List[Dict[str, any]]:
    results = []
    for i, query in enumerate(queries[:max_runs], 1):
        logger.info(f"Executing query {i}/{max_runs}")
        try:
            result = execute_soql_query(sf_conn, query)
            results.append({"soql": query, "result": True})
            logger.info(f"Query {i} executed successfully")
        except Exception as e:
            results.append({"soql": query, "result": False})
            logger.error(f"Query {i} failed. Error: {str(e)}")
    return results

def write_results(results: List[Dict[str, any]], output_file: str):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['soql', 'result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    logger.info(f"Results written to {output_file}")

def main():
    logger.info("Starting query validation")
    sf_conn = get_salesforce_connection()
    queries = read_soql_queries('soql_queries.csv')
    logger.info(f"Read {len(queries)} queries from soql_queries.csv")
    results = execute_queries(sf_conn, queries, max_runs=8)
    write_results(results, 'soql_results.csv')
    logger.info("Query validation completed")

if __name__ == "__main__":
    main()