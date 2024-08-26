import csv
import os
from typing import List, Dict
from utils.connection import get_salesforce_connection
from utils.soql import execute_soql_query
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_soql_queries(file_path: str) -> List[Dict[str, str]]:
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return [{"question": row["natural_language_ask"], "soql": row["soql_query"]} for row in reader]

def execute_queries(sf_conn, queries: List[Dict[str, str]]) -> List[Dict[str, any]]:
    results = []
    total_queries = len(queries)
    for i, query_data in enumerate(queries, 1):
        logger.info(f"Executing query {i}/{total_queries}")
        try:
            result = execute_soql_query(sf_conn, query_data["soql"])
            results.append({"question": query_data["question"], "soql": query_data["soql"], "result": True})
            logger.info(f"Query {i} executed successfully")
        except Exception as e:
            results.append({"question": query_data["question"], "soql": query_data["soql"], "result": False})
            logger.error(f"Query {i} failed. Error: {str(e)}")
    return results

def write_results(results: List[Dict[str, any]], output_file: str):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['question', 'soql', 'result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    logger.info(f"Results written to {output_file}")

def main():
    logger.info("Starting query validation")
    sf_conn = get_salesforce_connection()
    input_file = 'SOQL_samples_2_stg2.csv'
    queries = read_soql_queries(input_file)
    logger.info(f"Read {len(queries)} queries from {input_file}")
    results = execute_queries(sf_conn, queries)
    output_file = f"{os.path.splitext(input_file)[0]}_results.csv"
    write_results(results, output_file)
    logger.info("Query validation completed")

if __name__ == "__main__":
    main()