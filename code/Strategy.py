class Strategy:

    """
    A strategy investor wants to adopt on the market.
    Takes initial risk and profit values and exposes them on market-dependent
    values:
    - current funds
    - outcome (number of consecutive gains or losses)

    Calculates the exposition to risk (modified risk and profit values) by returning new:
    - profit-to-risk-ratio (PTRR)
    - shift of profit mean value
    - shift of risk mean value
    - spread of accepted profit values
    - spread of accepted risk values
