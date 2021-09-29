import jenkins_repl
import jenkins
import json
import os
from jinja2 import Environment, PackageLoader, select_autoescape
from xml.sax.saxutils import escape


def main():
    j = Jenkins()
    j.test_auth()

    pipeline = load("jenkins_repl/JenkinsfileScripted.groovy")
    name = "james-test"
    # j.delete_job(name)
    j.server.upsert_job(name, config_xml=render_job(pipeline))
    j.run_job(name)

    # print('\n')
    # server.create_folder("james-testing", ignore_failures=True)
    # server.create_folder("james-testing/foo", ignore_failures=True)
    #

    # write_file("jobs", server.get_jobs())
    # server.create_job('james-testing', jenkins.EMPTY_CONFIG_XML)


class Jenkins:
    def __init__(self):
        JENKINS_USERNAME = os.environ["JENKINS_USERNAME"]
        JENKINS_PASSWORD = os.environ["JENKINS_PASSWORD"]
        JENKINS_URL = "http://jenkins.pennywise.cc"
        # overwrite for testing
        JENKINS_USERNAME = "admin"
        JENKINS_PASSWORD = "admin"
        JENKINS_URL = "http://localhost:8080"
        self.server = jenkins.Jenkins(
            url=JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD
        )

    def run_job(self, name):
        job_info = self.server.get_job_info(name)
        build_number = job_info["nextBuildNumber"]
        self.server.build_job(name)
        print(f"Build number: {build_number}")
        from time import sleep
        while self.server.get_job_info(name)["nextBuildNumber"] != build_number + 1:
            sleep(.5)
        while self.server.get_build_info(name=name, number=build_number)["result"] not in ["SUCCESS", "FAILED"]:
            sleep(.5)

        print(self.server.get_build_console_output(name, build_number))
        number = self.server.build_job(name)

    def delete_job(self, job):
        try:
            self.server.delete_job(job)
        except jenkins.NotFoundException:
            pass

    def test_auth(self):
        user = self.server.get_whoami()
        version = self.server.get_version()
        print("Hello %s from Jenkins %s" % (user["fullName"], version))


def render_job(pipeline):
    template_env = Environment(
        loader=PackageLoader("jenkins_repl"), autoescape=select_autoescape()
    )
    return template_env.get_template("pipeline.tmpl").render(
        {"pipeline": escape_all(pipeline)}
    )


def escape_all(data):
    return escape(
        data,
        entities={
            "'": "&apos;",
            '"': "&quot;",
        },
    )


def jprint(data):
    print("\n")
    print(json.dumps(data, indent=4, default=str))


def load(file):
    with open(file, "r") as f:
        return f.read()


def write_file(file, data):
    with open(file, "w") as f:
        f.write(json.dumps(data, indent=4, default=str))


if __name__ == '__main__':
    main()
