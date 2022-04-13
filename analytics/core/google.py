import gspread


def get_google_sheet(key_or_url: str):
    gc = gspread.service_account(filename="analytics/core/service_account.json")
    open_func = gc.open_by_key if not key_or_url.startswith("https") else gc.open_by_url
    return open_func(key_or_url)
