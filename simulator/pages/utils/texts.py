INTRODUCTION = '''
# COVID-19 simulator

Data Science applied to the new coronavirus pandemic

---
'''

ABOUT = '''
This project is a task force of the scientific and technological communities in order to create prediction models of infected by COVID-19 - and other related metrics -, for Brazil. The project is public and can be used by everyone.

Visit [this link] (https://github.com/3778/COVID-19) for detailed information and instructions on how to contribute.
'''

PARAMETER_SELECTION='''
# Parameter selection
To simulate other scenarios, change a parameter and press ** Enter **. The new result will be calculated and displayed automatically.
#### UF / Municipality parameters
'''

MODEL_INTRO='''
### Exposure of exposed and infected
The graph below shows the result of the simulation of the evolution of exposed and infected patients for the selected parameters. More information about this model is available [here] (https://github.com/3778/COVID-19#seir-bayes).

**(!) Important **: The results presented are * preliminary * and are in the validation phase.
'''

def make_SIMULATION_PARAMS(SEIR0, intervals, should_estimate_r0):
    alpha_inv_inf, alpha_inv_sup, _, _ = intervals[0]
    gamma_inv_inf, gamma_inv_sup, _, _ = intervals[1]

    if not should_estimate_r0:
        r0_inf, r0_sup, _, _ = intervals[2]
        r0_txt = f'- $${r0_inf:.03} < R_{{0}} < {r0_sup:.03}$$'
    else:
        r0_txt = '- $$R_{{0}}$$ is being estimated with historical data'

    intro_txt = '''
    ---

    ### Simulation parameters
    
    Initial values of the compartments:
    '''
    
    seir0_labels = [
        "Susceptible",
        "Exposed",
        "Infected",
        "Removed",
    ]
    seir0_values = list(map(int, SEIR0))
    seir0_dict = {
        "Compartment": seir0_labels,
        "Initial value": seir0_values,
    }
    
    other_params_txt = f'''
    Other parameters:
    - $${alpha_inv_inf:.03} < T_{{incub}} = 1/\\alpha < {alpha_inv_sup:.03}$$
    - $${gamma_inv_inf:.03} < T_{{infec}} = 1/\gamma < {gamma_inv_sup:.03}$$
    {r0_txt}

    The intervals $$T_{{incub}}$$ e $$T_{{infec}}$$ define 95% of the confidence interval for a LogNormal distribution.
    ''' 
    return intro_txt, seir0_dict, other_params_txt

SIMULATION_CONFIG = '''
---

### Simulation settings (menu on the left)

#### UF / Municipality Selection
It is possible to select a unit of the federation or municipality to use its parameters in the initial conditions of * Total population * (N), * Infectious individuals initially * (I0), * Individuals removed with immunity initially * (R0) and * Individuals initially exposed ( E0) *.

#### Lower and upper limits of parameters
Upper and lower limits of the parameters * Infectious period *, * Incubation time * and * Basic number of reproduction * can also be adjusted. These limits define a 95% confidence interval of a log-normal distribution for each parameter.\n\n\n
'''

DATA_SOURCES = '''
---

### Data sources

* Confirmed cases by municipality: [Number of confirmed cases of COVID-19 in Brazil] (https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities-time.csv) (from https: // github.com/wcota/covid19br)
* Cases confirmed by state: [Panel of coronavirus disease cases 2019 (COVID-19) in Brazil by the Ministry of Health] (https://covid.saude.gov.br/)
* Population: IBGE estimate of 7/1/2019 (available at: [IBGE - Population estimates] (https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html) )
'''

r0_ESTIMATION_TITLE = '### Basic reproduction number $R_{{0}}$'

def r0_ESTIMATION(place, date): return  f'''
The basic reproduction number $ R_{0} $ is being estimated with historical data for {place}. The value used in the SEIR-Bayes model is that of {date}, which is the most recent.

If you wanted to specify the value manually, disable the option above and enter the desired values.

**(!) Important **: The estimation is sensitive to the quality of the notifications of positive cases.
'''

r0_ESTIMATION_DONT = '''
Use the menu on the left to configure the parameter.
'''

r0_CITATION = '''
The methodology used for estimation was based on the article [* Thompson, R. N., et al. "Improved inference of time-varying reproduction numbers during infectious disease outbreaks." Epidemics 29 (2019): 100356 *] (https://www.sciencedirect.com/science/article/pii/S1755436519300350). The implementation code can be found [here] (https://github.com/3778/COVID-19/blob/master/covid19/estimation.py).
'''

def r0_NOT_ENOUGH_DATA(w_place, w_date): return f'''
**{w_place} does not have enough data on the date
{w_date} to do the estimation. Soon,
aggregated data used Brazil**
'''
