from jira import JIRA

from jira_tools import utils

jira_options = {'server': utils.BASE_JIRA_URL}
jira = JIRA(options=jira_options, basic_auth=(utils.JIRA_LOGIN, utils.JIRA_PASSWORD))


def run_jql(jql):
    issues = jira.search_issues(jql)
    print(issues.total)


def get_tickets_tested(sprint_number):
    fav_filters = jira.favourite_filters()
    tickets_tested = []

    for i in range(5):
        name = "Airflow Sprint %d Delivered Issues" % (sprint_number - i)
        print(name)
        sprint_filter = [x.id for x in fav_filters if x.name == name][0]
        tickets_tested.append(jira.search_issues("filter=%s" % sprint_filter).total)

    print(tickets_tested)

def get_sprints(sprint_number):
    pass


if __name__ == '__main__':
    # run_jql("project=FLOW")
    get_tickets_tested(192)
