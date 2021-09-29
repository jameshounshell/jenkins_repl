def parsePathParts(String pth) {
  def match = pth =~ /^\.\/(.*?)(?:\/(.*?))?\/Dockerfile$/
  if (match == null) {
    return null
  }
  return [owner: "sre", repo: match[0][1], tag: match[0][2] ?: "latest", dir: pth.replace("Dockerfile", "")]
}

def main(){
    println {
        "foo"
    }
    println parsePathParts("./foo/Dockerfile")
    println "find . -type f -name Dockerfile -print0".execute().text.trim().split("\0").sort()

}

builderNode {
    main()
}


