"""Componentes reutilizáveis da interface"""

import flet as ft
from flet import *
from config import *

def create_avatar():
    """Cria um avatar padrão"""
    return ft.Container(
        width=AVATAR_SIZE,
        height=AVATAR_SIZE,
        bgcolor=AVATAR_BG_COLOR,
        border_radius=AVATAR_SIZE/2,
    )

def create_button(text: str, on_click=None):
    """Cria um botão personalizado com avatar"""
    avatar = create_avatar()
    if on_click is None:
        on_click = lambda e: page.go("/descricao_servico")
        
    return ft.ElevatedButton(
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            bgcolor=BUTTON_BG_COLOR,
            text_style=ft.TextStyle(
                weight=ft.FontWeight.W_400,
                size=20,
                color="#FFFFFF"
            ),
        ),
        on_click=on_click,
        content=ft.Row(
            controls=[
                avatar,
                ft.Text(
                    text,
                    size=15,
                    weight=ft.FontWeight.W_700,
                    color="#FFFFFF",
                    text_align=ft.TextAlign.CENTER,
                    max_lines=1,
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
    )

def create_chat_layout(chat, new_message, send_click):
    """Cria o layout do chat"""
    return ft.Stack(
        controls=[
            ft.Container(
                width=CHAT_WIDTH,
                height=CHAT_HEIGHT,
                bgcolor=CHAT_BG_COLOR,
                margin=ft.margin.only(top=70),
                border_radius=5,
            ),
            ft.Column(
                [
                    ft.Container(
                        content=chat,
                        bgcolor="#FFFFFF",
                        width=250,
                        height=320,
                        border_radius=10,
                        padding=10,
                        margin=ft.margin.only(left=10, right=10, top=55),
                        border=ft.border.all(1, ft.colors.BLACK),
                    ),
                    ft.Row(
                        controls=[
                            new_message,
                            ft.ElevatedButton(
                                "Enviar",
                                on_click=send_click,
                                bgcolor=SEND_BUTTON_COLOR,
                                color=ft.colors.WHITE,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Container(
                content=ft.Text(
                    "Chat", color="white", size=18, weight="bold"
                ),
                bgcolor=CHAT_TITLE_BG_COLOR,
                width=CHAT_TITLE_WIDTH,
                height=CHAT_TITLE_HEIGHT,
                border_radius=20,
                alignment=ft.alignment.center,
                margin=ft.margin.only(bottom=420, top=20),
                border=ft.border.all(1, ft.colors.BLACK),
            ),
        ],
        alignment=ft.alignment.center,
        height=470,
    )
