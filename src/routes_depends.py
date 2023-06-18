
from typing import List, Optional
from fastapi import FastAPI, Path, Query

async def params_styletransfer(
    style1: Optional[int] = 1,
    style2: Optional[int] = 2,
    alpha: Optional[float] = Query(0.0, gt=0, lt=1.0),
    test: Optional[int] = None
):
    """
    """

    ret = {
        'style1': style1,
        'style2': style2,
        'alpha': alpha,
        'test': test,
    }
    return ret