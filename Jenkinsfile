pipeline {
    agent any 
    stages {
        stage('Tests') {
            steps {
                dir('flask-app'){
                    sh "echo this is a test"
                    // sh "rm application/test/test_int*"
                    // sh "bash test.sh"
                }
            }
        }

        stage('docker-compose build and run') {
            steps {
                sh "docker stop $(docker ps -q)"
                sh "docker rm $(docker ps -a -q)"
                sh "docker rmi $(docker images -q -f)"
                sh "docker-compose up -d"
            }
        }

    }
}
