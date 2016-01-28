"""Configuration file for the database"""


class ConfigVars(object):
    """
    Configuration variables
    """
    database = 'mobile_qa_db'
    url = 'http://localhost:8069/web?db={database}'.format(database=database)
    odoo_client_url = 'http://localhost:8069'
    test_db_name = 'openeobs_quality_assurance_db'
