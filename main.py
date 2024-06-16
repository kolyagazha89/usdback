from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from starlette.middleware.cors import CORSMiddleware

from auth.auth import auth_backend
from auth.database import User
from auth.manger import get_user_manager
from auth.schemas import UserRead, UserCreate, UserUpdate
from src.classes.router import router as router_class
from src.partners.router import router as router_partners
from src.img.router import router as router_img
from src.typeStage.router import  router as router_type
from src.tagsStage.router import router as router_tags
from src.stage.router import router as router_stage
from src.users.router import router as router_user
from src.party.router import router as router_party
from rtc.router import router as router_rtc

app=FastAPI()

origins =["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_class)
app.include_router(router_partners)
app.include_router(router_img)
app.include_router(router_type)
app.include_router(router_tags)
app.include_router(router_stage)
app.include_router(router_user)
app.include_router(router_party)
app.include_router(router_rtc)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
current_active_user = fastapi_users.current_user(active=True)

@app.get("/protected-route")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}"

current_superuser = fastapi_users.current_user(active=True, superuser=True)

@app.get("/protected-route/super")
def protected_route(user: User = Depends(current_superuser)):
    return f"Hello, {user.email}"

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)