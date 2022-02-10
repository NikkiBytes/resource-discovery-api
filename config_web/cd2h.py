from config_local import ES_PRIVATE_HOST, ES_HTTP_AUTH
from web.handlers import EXTRA_HANDLERS
from biothings.web.settings.default import QUERY_KWARGS

# *****************************************************************************
# Elasticsearch Settings
# *****************************************************************************
ES_HOST = ES_PRIVATE_HOST
ES_ARGS = {
    "http_auth": ES_HTTP_AUTH
}

ES_INDICES = {
    None: "c*,o*",   # all indices excluding internal ones
    "outbreak": "outbreak_*",
    "cd2h": "cd2h-*",
    "csbc": "csbc-*"
}
ES_DOC_TYPE = 'doc'
ANNOTATION_DEFAULT_SCOPES = ["_id", "symbol"]
QUERY_KWARGS['*']['_source']['default'] = ["description", "entity"] # restrict results


# *****************************************************************************
# Web Application
# *****************************************************************************
API_PREFIX = 'api'
API_VERSION = 'v1'

# *****************************************************************************
# Elasticsearch Query Pipeline
# *****************************************************************************
#ES_QUERY_PIPELINE = "web.handlers.CD2HQueryPipeline"
#ES_QUERY_BUILDER = "web.handlers.CD2HQueryBuilder"
#AVAILABLE_FIELDS_EXCLUDED = ['all', 'accession_agg', 'refseq_agg']