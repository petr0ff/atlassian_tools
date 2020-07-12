import requests
import yaml

try:
    config = yaml.safe_load(open("../config.yml"))
except IOError:
    raise Exception("Please, create config.yml from config.yml.example")

BASE_JIRA_URL = config.get("jira")
ZAPI_URL = config.get("zapi")
LOGIN = config.get("login")
PASSWORD = config.get("password")
JIRA_PROJECT = config.get("project")
TEST_CYCLE = config.get("test_cycle")
LABELS = config.get("search_by")
STATUS_FROM = config.get("status_from")
STATUS_TO = config.get("status_to")
BASE_BITBUCKET_URL = config.get("bitbucket")
BITBUCKET_PROJECT = config.get("bb_project")

DEFAULT_HEADERS = {"Content-Type": "application/json"}

STATUSES = {
    "PASSED": 1,
    "FAILED": 2,
    "WIP": 3,
    "BLOCKED": 4,
    "SCHEDULED": -1
}


class ZapiCalls(object):
    PUT_EXECUTION = "/rest/zapi/latest/execution"
    GET_ZQL_SEARCH = "/rest/zapi/latest/zql/executeSearch"


class BBapiCalls(object):
    PUT_EXECUTION = "/rest/zapi/latest/execution"
    GET_ZQL_SEARCH = "/rest/zapi/latest/zql/executeSearch"


def get_request(endpoint, params=None):
    r = requests.get(BASE_JIRA_URL + endpoint,
                     auth=(LOGIN, PASSWORD),
                     headers=DEFAULT_HEADERS,
                     timeout=180,
                     params=params)
    return handle_response_status(r)


def post_request(endpoint, payload=None):
    r = requests.post(BASE_JIRA_URL + endpoint, auth=(LOGIN, PASSWORD), data=payload, headers=DEFAULT_HEADERS)
    return handle_response_status(r)


def put_request(endpoint, payload=None):
    r = requests.put(BASE_JIRA_URL + endpoint, auth=(LOGIN, PASSWORD), data=payload, headers=DEFAULT_HEADERS)
    return handle_response_status(r)


def delete_request(endpoint, params=None):
    r = requests.delete(BASE_JIRA_URL + endpoint, auth=(LOGIN, PASSWORD), headers=DEFAULT_HEADERS,
                        params=params)
    return handle_response_status(r)


def handle_response_status(response):
    if response.status_code in (200, 201, 204):
        return response
    else:
        raise Exception(response.url, response.content, response.status_code)
