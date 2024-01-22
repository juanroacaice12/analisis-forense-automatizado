__author__ = 'Juan Camilo R'

from ast import main
from cryptography.fernet import Fernet
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import datetime

class DataProtector: 
    def __init__(self, key):
        self.key = key
        self.cipher = Fernet(key)

    def encrypt_data(self, data):
        encrypted_data = self.cipher.encrypt(data.encode())
        return encrypted_data
    

class DataClassifier:
    def __init__(self):
        nltk.download("vader_lexion")
        self.analyzer = SentimentIntensityAnalyzer()


    def classify_data(self, data):
        sentiment_score = self.analyzer.polarity_scores(data)["compound"]

        if sentiment_score >= 0.05:
            return "positivo"
        elif sentiment_score <= -0.05:
            return "negativo"
        else:
            return "neutral"
        
class DataAuditor:
    def __init__(self):
        self.acces_log = []

    def log_access(self, user, action, timestamp):
        log_entry = f"{timestamp}: Usuario {user} realizó la acción '{action}'"
        self.access_log.append(log_entry)
        print(log_entry)

    def view_access_log(self):
        print("\nRegistro de acceso:")
        for entry in self.access_log:
            print(entry)

class DataRetentiponPolicy:
    def __init__(self, retention_days):
        self.retention_days = retention_days
        self.data_store = []

    def store_data(self, data, timestamp):
        self.data_store.append((data, timestamp))

    def clean_expired_data(self, current_timestamp):
         expired_data = [(data, timestamp) for data, timestamp in self.data_store if current_timestamp - timestamp >= self.retention_days]
         for data, timestamp in expired_data:
             print(f"Eliminando datos expirados: {data}")
             self.data_store.remove((data, timestamp))

class RiskAssessment:
    def __init__(self, classification):
        self.classification == classification

    def assess_risk(self):
        if self.classification == "Negativo":
            print("Riesgo alto: Datos clasificados como negativos.")
        elif self.classification == "Positivo":
            print("Riesgo bajo: Datos clasificados como positivos.")
        else:
            print("Riesgo moderado: Datos clasificados como neutrales.")

    def main():
        key = Fernet.generate_key()


        data_protector = DataProtector(key)
        data_classifier = DataClassifier()
        data_auditor = DataAuditor()
        data_retention_policy = DataRetentiponPolicy(retention_days=30)


        sensitive_data = "Informacion confidencial sobre un nuevo proyecto"
        encrypted_data = data_protector,encrypted_data(sensitive_data)
        print(f"Dato encriptado: {encrypted_data}")

        decrypted_data = data_protector.decrypted_data(encrypted_data)
        classification = data_classifier.classify_data(decrypted_data)
        print(f"Dato desencriptado: {decrypted_data}")
        print(f"Clasificacion: {classification}")

        user = "Alicia"
        action = "Lectura"
        timestamp = datetime.datetime.now()
        data_auditor.log_access(user, action, timestamp)

        data_retention_policy.store_data(decrypted_data, timestamp)
        
        data_auditor.view_access_log()
        current_timestamp = datetime.datetime.now()
        data_retention_policy.clean_expired_data(current_timestamp)

        risk_assessment = RiskAssessment(classification)
        risk_assessment.assess_risk()

if __name__ == "__main__":
    main()
