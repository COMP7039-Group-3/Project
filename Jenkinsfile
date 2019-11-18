pipeline {
    agent { docker { image 'stefanscherer/python-windows:nano' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}