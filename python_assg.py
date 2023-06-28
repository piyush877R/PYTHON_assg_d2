import math
import pandas as pd
from sqlalchemy import create_engine  as ce 
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, grid
from bokeh.models import Band, ColumnDataSource
from sqlalchemy import create_engine, table, column, String, Float, MetaData 
from unittest import TestCase
from all_func import Managing_Functions
from loss_func import quad_error
from utilities import write_deviation_results_to_sqlite
from reggression import find_classification , minimise_loss
from ploting import plotting_ideal_activities , plotting_points_with_their_ideal_function





FACTOR_ACCEPTED = math.sqrt(2)

if __name__ == '__main__':
    
    ideal_Location = "data/ideal.csv"
    train_Location = "data/train.csv"

    
    Dupe_ideal_Managing_Function = Managing_Functions(Location_of_CSV_File=ideal_Location)
    train_function_manager = Managing_Functions(Location_of_CSV_File=train_Location)

    
    train_function_manager.to_sql(Name_of_file="training", Suff=" (training func)")
    Dupe_ideal_Managing_Function.to_sql(Name_of_file="ideal", Suff=" (ideal func)")

    
    ideal_activities = []
    for train_activity in train_function_manager:
        
        ideal_activity = minimise_loss(drill_func=train_activity,
                                    inventory_functions=Dupe_ideal_Managing_Function.func_S,
                                    losing_activity=quad_error)
        ideal_activity.tolerance_factor = FACTOR_ACCEPTED
        ideal_activities.append(ideal_activity)

    
    plotting_ideal_activities(ideal_activities, "train_and_ideal")

    
    test_Location = "data/test.csv"
    test_function_manager = Managing_Functions(Location_of_CSV_File=test_Location)
    test_function = test_function_manager.func_S[0]

    points_ideal_activity = []
    for point in test_function:
        ideal_activity, delta_y = find_classification(point=point, ideal_activities=ideal_activities)
        result = {"point": point, "classi": ideal_activity, "delta_y": delta_y}
        points_ideal_activity.append(result)

    
    
    plotting_points_with_their_ideal_function(points_ideal_activity, "point_and_ideal")

    
    write_deviation_results_to_sqlite(points_ideal_activity)
    