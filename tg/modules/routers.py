from aiogram import Router

from .contract.router import contract_router

modules_router = Router()

modules_router.include_routers(
    contract_router,
)
