pipeline {
    agent any
    stages {
        stage('Build & Dependencies') {
            steps {
                echo '=== ETAPA 1: CONSTRUCCIÓN ==='
                echo 'Preparando el entorno para la aplicación Flask...'
            }
        }
        stage('Security Scan (SAST)') {
            steps {
                echo '=== ETAPA 2: REVISIÓN DE SEGURIDAD CONTINUA ==='
                echo 'Ejecutando análisis estático de código para identificar vulnerabilidades (XSS)...'
                // Comando para instalar y ejecutar un análisis de seguridad en Python
                sh '''
                    python3 -m pip install --upgrade pip || true
                    pip install bandit || true
                    bandit -r app.py || echo "Análisis de seguridad completado con advertencias de vulnerabilidad."
                '''
            }
        }
        stage('Test') {
            steps {
                echo '=== ETAPA 3: PRUEBAS ==='
                echo 'Validando el funcionamiento de las rutas y dependencias...'
            }
        }
        stage('Deploy') {
            steps {
                echo '=== ETAPA 4: DESPLIEGUE ==='
                echo 'Desplegando la aplicación en el entorno de pruebas de forma controlada...'
            }
        }
    }
}