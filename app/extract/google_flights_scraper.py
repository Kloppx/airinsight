import re
from datetime import date, timedelta

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError, sync_playwright


GOOGLE_FLIGHTS_URL = "https://www.google.com/travel/flights?hl=pt-BR&curr=BRL"
ORIGIN = "MCZ"
DESTINATION = "GRU"
DEPARTURE_DATE = date.today() + timedelta(days=30)


def select_airport(page: Page, field_name: str, airport_code: str) -> None:
    """Fill an airport field and select the matching suggestion."""
    field = page.get_by_role("combobox", name=field_name)
    field.click()

    dialog_field = page.get_by_role("dialog").get_by_role("combobox")
    dialog_field.fill(airport_code)
    page.get_by_role("option", name=re.compile(rf"\({airport_code}\)")).first.click()
    page.get_by_role(
        "combobox", name=re.compile(rf"{re.escape(field_name)}.*{airport_code}")
    ).wait_for(state="visible")


def format_google_date(value: date) -> str:
    """Return the date format accepted by Google Flights in pt-BR."""
    return value.strftime("%d/%m/%Y")


def collect_first_price(page: Page) -> str:
    """Run one flight search and return the first visible price in BRL."""
    page.goto(GOOGLE_FLIGHTS_URL, wait_until="domcontentloaded")

    trip_type = page.get_by_role("combobox", name=re.compile("tipo da passagem", re.I))
    trip_type.click()
    page.get_by_role("option", name="Só ida").click()
    page.get_by_role("combobox", name=re.compile("Só ida", re.I)).wait_for(
        state="visible"
    )

    select_airport(page, "De onde?", ORIGIN)
    select_airport(page, "Para onde?", DESTINATION)

    departure = page.get_by_role("textbox", name="Partida")
    departure.fill(format_google_date(DEPARTURE_DATE))
    departure.press("Enter")

    calendar_dialog = page.get_by_role("dialog").filter(
        has=page.get_by_role("textbox", name="Partida")
    )
    if calendar_dialog.is_visible():
        calendar_dialog.get_by_role(
            "button", name=re.compile("Concluído", re.I)
        ).click()
        calendar_dialog.wait_for(state="hidden")

    page.get_by_role("button", name="Pesquisar").click()

    first_flight = page.get_by_role(
        "link",
        name=re.compile(r"^A partir de \d+ Reais brasileiros.*Selecionar voo$"),
    ).first
    first_flight.wait_for(state="visible", timeout=30_000)

    accessible_name = first_flight.get_attribute("aria-label") or ""
    price_match = re.search(r"A partir de (\d+) Reais brasileiros", accessible_name)
    if price_match is None:
        raise RuntimeError("The first flight was found, but its price could not be read.")

    return f"R$ {int(price_match.group(1)):,}".replace(",", ".")


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page(locale="pt-BR")

        try:
            first_price = collect_first_price(page)
            print(
                f"First price found for {ORIGIN} -> {DESTINATION} "
                f"on {DEPARTURE_DATE.isoformat()}: {first_price}"
            )
        except PlaywrightTimeoutError as error:
            print("The Google Flights search timed out.")
            print(f"Current page: {page.url}")
            print(f"Playwright detail: {error}")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
