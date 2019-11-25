
pipeline {
    agent { docker { image 'python:3.7.5' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt --user'
            }
        }
        stage('test') {
            steps {
                sh 'pytest -v -rs'
            }
        }
    }
}
