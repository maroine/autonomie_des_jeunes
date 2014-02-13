from datetime import datetime


from openfisca_core.simulations import model
import openfisca_france
from openfisca_core.simulations import ScenarioSimulation

def case_study(year = 2013):
    
    simulation = ScenarioSimulation()
    simulation.set_config(year = 2013, 
                          nmen = 2,
                          maxrev = 10000,
                          x_axis = 'sali')
    simulation.set_param()
    df = simulation.get_results_datafram()
    print df.to_string()
    
    if_name_**'__main__' 
    
    
    case_study_()
    




'''
Created on 13 févr. 2014

@author: maroine
'''
