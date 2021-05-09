from scipy.optimize import minimize

# maximizing correlation between ar_tech and HDI to reasonably calculate weights
min_eq = lambda x: -1 * df['human_development_index'].corr(df['mobile_subscriptions'] * x[0] + df['perc_internet_users'] * x[1] + df['access_to_electricity'] * x[2])

# constr
constraints = (
    {'type':'eq','fun': lambda x: x[0] + x[1] + x[2]-1},
    {'type':'ineq','fun': lambda x: x[0]-1},
    {'type':'ineq','fun': lambda x: x[1]-1},
    {'type':'ineq','fun': lambda x: x[2]-1}
)

# bounds
bounds = ((0,0), (-1,0), (-1,0), (-1,0))

res = minimize(fun=min_eq, x0=[0,0.1,0.35,0.55], constraints=constraints, bounds=bounds, method='Nelder-Mead')
res