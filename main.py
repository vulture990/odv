from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
quotes = Scraper()


@app.get('/{tag}')
async def read_item(tag: str):
    return quotes.scrapedata(tag)