/*

A file devoted to mocking Jenkinsfile DSL

Just concatenate this with the Jenkinsfile.
This file comes first.

ex:
  `cat Jenkinsfile.mocks.groovy Jenkinsfile > /tmp/Jenkinsfile; groovy /tmp/Jenkinsfile`
*/

/* Jenkinsfile DSL mocks */
// https://groovy-lang.org/closures.html
def builderNode(closure) {
    closure.call()
}
def node(closure) {
    closure.call()
}

def stage(name, closure){
    closure.call()
}

@interface NonCPS {}

def scm = ""
def checkout(scm){}

def parallelBatched(args){}

def sh(Map args){
  script = args.script
  stdout = new StringBuilder()
  stderr = new StringBuilder()
  proc = script.execute()
  proc.consumeProcessOutput(stdout, stderr)
  proc.waitForOrKill(1000)
  if (stderr){
    println stderr
  }
  return stdout.toString()
}

/* mimic pythons dir function*/
def dir(obj){
    println ""
    obj.properties*.each{println it}
    println obj.metaClass.methods*.name.sort().unique()
}
