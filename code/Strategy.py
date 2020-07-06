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
    """
    def funds_spread(self, funds: float, initial_funds: float, l_rate: float, g_rate: float):
        """
        Computes the spread of profit and risk values based on current funds.
        
        Parameters:
        -----------
        
        funds: float
            Funds for which the spread will be computed.
            
        initial_funds: float
            Funds at the beginning of the investment process.
        
        l_rate: float
            Rate for the change in losses spread with respect to funds per 1000.
            
        g_rate: float
            Rate for the change in gains spread with respect to funds per 1000.
        
        
        Returns:
        --------
        
        Tuple in format (losses_spread, gains_spread)
        
        """
        
        if funds > initial_funds:
            
            fund_diff = funds - initial_funds
            
            if self.strategy == "Neutral":
                value = (0,0)

            elif self.strategy == "Greedy":
                l_spread = 0.001 * l_rate * fund_diff
                g_spread = 0.001 * g_rate * fund_diff

                value = (l_spread, g_spread)

            elif self.strategy == "Cautious":
                value = (0,0)
                
        else:
            value = (0,0)
        
        return value
    
    def outcome_spread(self, num_outcomes: list, l_rate: float, g_rate: float):
        """
        Computes the spread of profit and risk values based on the number of consecutive outcomes.
        
        Parameters:
        -----------
        
        num_outcomes: list
            Tuple with information on type and number of consecutive outcomes of the last transactions.
            Format: (str, int)
            Example:
            ("l", 5) - 5 consecutive losses
            ("g", 3) - 3 consecutive gains
        
        l_rate: float
            Rate for the change in losses spread with respect to the number of consecutive outcomes of one type.
            
        g_rate: float
            Rate for the change in gains spread with respect to the number of consecutive outcomes of one type.
        
        
        Returns:
        --------
        
        Tuple in format (losses_spread, gains_spread)
        
        """
        
        
        if self.strategy == "Neutral":
            value = (0,0)
        
        elif self.strategy == "Greedy":
            value = (0,0)
            
        elif self.strategy == "Cautious":
            l_spread = 2**(-l_rate * (num_outcomes[1] - 1))
            
            value = (l_spread, 1)
        
        return value
