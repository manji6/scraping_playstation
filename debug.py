from scraper import Scraper
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


logger.info("Message")


scraper = Scraper()
scraper.store_playstation("https://store.playstation.com/ja-jp/category/1b6c3e7d-4445-4cef-a046-efd94a1085b7/")
