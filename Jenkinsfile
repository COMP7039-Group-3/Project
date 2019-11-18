pipeline {
    agent { docker { image 'python:3-windowsservercore' } }
    stages {
        stage('build') {
            steps {
                bat 'python --version'
            }
        }
    }
}
