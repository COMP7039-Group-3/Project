
pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('build') {
            steps {
                 withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install setuptools -U --user'
                    sh 'pip install --user -r requirements.txt'
                    sh 'python -m pytest -v -rs'
                }
            }
        }       
    }
}
