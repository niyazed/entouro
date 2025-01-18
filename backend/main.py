import os
from loguru import logger

from typing import AsyncGenerator

from fastapi import FastAPI
from fastcrud import FastCRUD, crud_router
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from models.guide import Base, Guide
from schemas.guide import GuideCreateSchema, GuideSearchSchema, GuideUpdateSchema


from dotenv import load_dotenv
load_dotenv()

# Database setup (Async SQLAlchemy)
DATABASE_URL = os.getenv("DATABASE_URI")
logger.debug("That's it, beautiful and simple logging!", DATABASE_URL)

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Database session dependency
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        print("Connection Established, yielding session")
        yield session

# Create tables before the app start
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

# FastAPI app
app = FastAPI(lifespan=lifespan)

# CRUD router setup
guide_router = crud_router(
    session=get_session,
    model=Guide,
    create_schema=GuideCreateSchema,
    update_schema=GuideUpdateSchema,
    path="/guide",
    tags=["Guides"],
)

app.include_router(guide_router)

