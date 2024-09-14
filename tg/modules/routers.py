from aiogram import Router

from .gpt_module.router import gpt_router

modules_router = Router()

modules_router.include_routers(
    gpt_router,
)
