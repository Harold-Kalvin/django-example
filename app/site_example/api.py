from ninja import NinjaAPI

api = NinjaAPI()
api.add_router("/auth/", "authentication.router.router")
