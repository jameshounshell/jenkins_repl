node {
    checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '0f1ca2e1-29b3-417c-bb7e-e859f041a6ab', url: 'https://github.com/missionlane/big-brother']]])
    sh("pwd")
    sh("ls")
}
