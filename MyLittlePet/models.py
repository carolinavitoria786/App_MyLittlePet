"""Modelos de dados da aplicação"""

class Message:
    """Classe para representar uma mensagem no chat"""
    def __init__(self, user: str, text: str, message_type: str):
        self.user = user
        self.text = text
        self.message_type = message_type
