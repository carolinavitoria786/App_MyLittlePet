"""Componentes e lógica relacionados ao chat"""

import flet as ft
from flet import *
from config import CHAT_USER_BG_COLOR, CHAT_OTHER_BG_COLOR

def create_chat_message(message, is_user_message: bool):
    """Cria uma mensagem de chat formatada"""
    return ft.Row(
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            f"{message.user}:",
                            size=12,
                            weight="bold",
                            color="white" if is_user_message else "black",
                        ),
                        ft.Text(
                            message.text,
                            size=14,
                            color="white" if is_user_message else "black",
                        ),
                    ],
                    spacing=5,
                ),
                padding=10,
                border_radius=8,
                bgcolor=CHAT_USER_BG_COLOR if is_user_message else CHAT_OTHER_BG_COLOR,
                margin=ft.margin.symmetric(vertical=5),
                alignment=ft.alignment.center_left
                if not is_user_message
                else ft.alignment.center_right,
            )
        ],
        alignment=ft.MainAxisAlignment.END if is_user_message else ft.MainAxisAlignment.START,
    )

def create_chat_input():
    """Cria o campo de entrada de texto do chat"""
    return ft.TextField(
        hint_text="Digite sua mensagem...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
    )
