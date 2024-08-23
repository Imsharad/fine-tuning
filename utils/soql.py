from typing import Dict, Any
from simple_salesforce import Salesforce
import logging

general_logger = logging.getLogger("general")

def execute_soql_query(sf_conn: Salesforce, soql_query: str) -> Dict[str, Any]:
    general_logger.info(f"Executing SOQL query {soql_query}")
    return sf_conn.query_all(soql_query)