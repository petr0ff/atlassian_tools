import stashy

from commons import utils


class BitBucket(object):
    def __init__(self, project, repo):
        self.project = project
        self.repo = repo
        self.bb = stashy.connect(utils.BASE_BITBUCKET_URL, utils.LOGIN, utils.PASSWORD)

    def get_pull_requests(self, branch=None, state='OPEN'):
        self.prs = list(self.bb.projects[self.project].repos[self.repo].pull_requests.all(at='refs/heads/%s' % branch,
                                                                                          state=state))
        print("Total %s PRs to branch %s" % (len(self.prs), branch))
        return self.prs

    def get_pull_request(self, pr_id):
        pr = self.bb.projects[self.project].repos[self.repo].pull_requests[pr_id]
        return pr

    def get_pull_request_updates_count(self, pr_id):
        activities = list(self.get_pull_request(pr_id).activities())
        updates = [a for a in activities if a["action"] == "RESCOPED"]
        return updates

    def get_pull_requests_updates(self):
        prs_and_updates = {}
        total_updates = 0
        flow_prs = [p for p in self.prs if "FLOW" in p["title"]]
        print("Total %s PRs with FLOW prefix" % len(flow_prs))
        for pr in flow_prs:
            updates = self.get_pull_request_updates_count(pr["id"])
            updates_num = len(updates)
            prs_and_updates[pr["title"]] = updates_num
            print("Number of updates for PR %s is %s" % (pr["title"], updates_num))
            total_updates += updates_num
        prs_and_updates["total_updates"] = total_updates
        return prs_and_updates
