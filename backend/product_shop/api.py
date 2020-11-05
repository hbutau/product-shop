from ninja import Router

router = Router()


@router.get("")
def add(request, a: int, b: int):
    return {"result": a + b}
