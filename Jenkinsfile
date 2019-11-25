
pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                 withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
                }
                
            }
        }
        stage('test') {
            steps {
                sh 'pytest -v -rs'
            }
        }
    }
}
