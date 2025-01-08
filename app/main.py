from fastapi import FastAPI, Request, Depends
from .import models
from .database import engine
from .routers import journal, user, mood, auth, password_reset, stats
from .config import settings
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .oath2 import get_current_user
from .schemas import TokenData


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(journal.router)
app.include_router(user.router)
app.include_router(mood.router)
app.include_router(auth.router)
app.include_router(password_reset.router)
app.include_router(stats.router)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/journals", response_class=HTMLResponse)
async def get_journal_page(request: Request):
    return templates.TemplateResponse("journal.html", {"request": request})

@app.get("/entries", response_class=HTMLResponse)
async def get_entries_page(request: Request):
    return templates.TemplateResponse("entries.html", {"request": request})

@app.get("/moods", response_class=HTMLResponse)
async def get_mood_page(request: Request):
    return templates.TemplateResponse("mood.html", {"request": request})

@app.get("/verify-token")
async def verify_token(token_data: TokenData = Depends(get_current_user)):
    return {"status": "Token is valid"}

@app.get("/calendar", response_class=HTMLResponse)
async def get_calendar_page(request: Request):
    return templates.TemplateResponse("calendar.html", {"request": request})

@app.get("/stats", response_class=HTMLResponse)
async def get_stats_page(request: Request):
    return templates.TemplateResponse("stats.html", {"request": request})