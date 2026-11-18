pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Construyendo el entorno y preparando dependencias...'
            }
        }
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias o de seguridad...'
            }
        }
        stage('Analyze') {
            steps {
                echo 'Ejecutando análisis de calidad y vulnerabilidades estáticas...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Desplegando la aplicación en el entorno de prueba...'
            }
        }
    }
}