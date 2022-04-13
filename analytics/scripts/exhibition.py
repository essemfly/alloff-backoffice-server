from typing import List

import arrow
from analytics.core.google import get_google_sheet
from analytics.models.exhibition import ExhibitionCVR
from gen.pyalloff.exhibition_pb2 import ListExhibitionsRequest
from product.services.exhibition import ExhibitionService

GROUP_TYPE_TUPLES = {
    (0, "NORMAL"),
    (1, "TIMEDEAL"),
    (2, "GROUPDEAL"),
}


def get_all_exhibition_cvr() -> List[ExhibitionCVR]:
    ex_ids = []
    for val, _ in GROUP_TYPE_TUPLES:
        req = ListExhibitionsRequest(
            offset=0,
            limit=100,
            group_type=val,
            is_live=False,
            query="",
        )
        exhibitions = ExhibitionService.list(req)
        for ex in exhibitions.exhibitions:
            ex_ids.append(ex.exhibition_id)

    return [ExhibitionCVR.make(x) for x in ex_ids]


ANALYTICS_CVR_SHEET_URL = "https://docs.google.com/spreadsheets/d/13vJpqIYATt7oSsvm-vixuy_pWpIVz6ihXJco2vjM0aY/edit#gid=0"
ANALYTICS_CVR_SHEET_STARTING_CELL = "A2"
ANALYTICS_CVR_SHEET_WORKSHEET_GID = 0


def update_google_sheet():
    sheet = get_google_sheet(ANALYTICS_CVR_SHEET_URL)
    ws = sheet.get_worksheet_by_id(ANALYTICS_CVR_SHEET_WORKSHEET_GID)
    records = get_all_exhibition_cvr()
    res = ws.update(
        ANALYTICS_CVR_SHEET_STARTING_CELL, [x.google_sheet_row for x in records]
    )
    sheet.update_title(
        f"Exhibition Analytics - Updated at {arrow.now().format('YYYY-MM-DD HH:mm:ss')}"
    )
    return res
