Jenkins REPL
============

An insane experiment to run Jenkins jobs from the command line.

Note: Everything is very Alpha quality at the moment!

``jenkins_repl`` is a python library for loading, running, and collecting the results of a job on a remote Jenkins server (or local container)

``Jenkinsfile.sh`` is an example of how with the help of mocks (``Jenkinsfile.mocks.groovy``) a Jenkinsfile can be run simply with a groovy interpreter instead of a full Jenkins installation.
