import uuid

class ConfigVariables:
    @staticmethod
    def random_bigdecimal():
        return str(uuid.uuid4())

    # Credenciales
    PASSWORD = "TestingQA753159"
    EMAIL = "testingQA1478963@gmail.com"

    # URL de la aplicación a testear
    BASE_URL = "https://ticktick.com/"

    # Nombre de la Tarea (Generado Dinámicamente)
    @staticmethod
    def get_task_name():
        return "Automation - " + ConfigVariables.random_bigdecimal()

    # Nombre de la Tarea Editada
    @staticmethod
    def get_edited_task_name():
        return "Updated - " + ConfigVariables.random_bigdecimal()
