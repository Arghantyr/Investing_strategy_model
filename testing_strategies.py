strategies = ["Neutral"]

strats = {}

quantiles = [0.01, 0.25, 0.5, 0.75, 0.99]

for strat in strategies:
    
    n_investments = 1000
    all_outcomes = pd.DataFrame(index=np.arange(1,n_investments+1,1))
    stat_outcomes = pd.DataFrame(index=np.arange(1,n_investments+1,1))
    
    n_rounds = 1000
    for i in range(n_rounds):
        ith_round = Invest(Inv_1, strategy=strat, initial_risk=(0.05,0.045,0.055),
                           initial_profit=(0.1,0.09,0.11), single_sum=130,
                           margin=0.5).Invest_funds(n = n_investments, cross_limit=2000)
        all_outcomes[i] = ith_round
    
    for quant in quantiles:
        stat_outcomes[quant] = all_outcomes.quantile(q=quant, axis=1)
        
    strats[strat] = stat_outcomes
    
    
