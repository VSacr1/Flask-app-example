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
            environment {
                ROOT_PASSWORD = credentials('ROOT_PASSWORD')   
            }
            steps {
                sh "docker-compose down -v"
                sh "/bin/bash -c 'docker rmi \$(docker images -a -q)'"
                sh "docker-compose up -d < deploy.sh"
            }
        }

    }
}
