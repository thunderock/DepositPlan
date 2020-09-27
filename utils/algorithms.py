def subset_sum(deposit_plan_denominations: list, amount: int) -> list:
    """:arg

    """
    # because this portfolios list can be only at max 2 long

    length = len(deposit_plan_denominations)
    ret = [False] * length
    if length == 0:
        return ret
    if length == 1:
        if amount == deposit_plan_denominations[0]:
            ret[0] = True
        return ret
    assert length == 2
    if amount == deposit_plan_denominations[0]:
        ret[0] = True
    elif amount == deposit_plan_denominations[1]:
        ret[1] = True
    elif amount == sum(deposit_plan_denominations):
        ret[0], ret[1] = True, True
    return ret
