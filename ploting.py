from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, grid
from bokeh.models import Band, ColumnDataSource


def plotting_ideal_activities(ideal_activities, Name_of_file):
    try:    
        ideal_activities.sort(key=lambda ideal_activity: ideal_activity.drill_func.tag, reverse=False)
        plots = []
        for ideal_activity in ideal_activities:
            p = plotting_graph_from_two_functions(line_function=ideal_activity, scatter_function=ideal_activity.drill_func,
                                            quad_error=ideal_activity.Flaw)
            plots.append(p)
        output_file("{}.html".format(Name_of_file))
        
        show(column(*plots))
    except Exception as e:
        print("Error in plotting_ideal_activities"+ str(e))


def plotting_points_with_their_ideal_function(pointing_with_classi, Name_of_file):
    try:    
        plots = []
        for index, item in enumerate(pointing_with_classi):
            if item["classi"] is not None:
                p = plotting_classifications(item["point"], item["classi"])
                plots.append(p)
        output_file("{}.html".format(Name_of_file))
        show(column(*plots))
    except Exception as e:
        print("Error in plotting_points_with_their_ideal_function"+ str(e))


def plotting_graph_from_two_functions(scatter_function, line_function, quad_error):
    try:    
        f1_dataframe = scatter_function.dataframe
        f1_name = scatter_function.tag

        f2_dataframe = line_function.dataframe
        f2_name = line_function.tag

        quad_error = round(quad_error, 2)
        p = figure(title="train model {} vs ideal {}. Total squared error = {}".format(f1_name, f2_name, quad_error),
                x_axis_label='x', y_axis_label='y')
        p.scatter(f1_dataframe["x"], f1_dataframe["y"], fill_color="red", legend_label="Train")
        p.line(f2_dataframe["x"], f2_dataframe["y"], legend_label="Ideal", line_width=2)
        return p
    except Exception as e:
        print("Error in plotting_graph_from_two_functions"+ str(e))


def plotting_classifications(point, ideal_activity):
    try:
        if ideal_activity is not None:
            classi_function_dataframe = ideal_activity.dataframe

            point_str = "({},{})".format(point["x"], round(point["y"], 2))
            title = "point {} with classi: {}".format(point_str, ideal_activity.tag)

            p = figure(title=title, x_axis_label='x', y_axis_label='y')

            
            p.line(classi_function_dataframe["x"], classi_function_dataframe["y"],
                    legend_label="classi function", line_width=2, line_color='black')

            
            criterion = ideal_activity.Tolarance_s
            classi_function_dataframe['upper'] = classi_function_dataframe['y'] + criterion
            classi_function_dataframe['lower'] = classi_function_dataframe['y'] - criterion

            source = ColumnDataSource(classi_function_dataframe.reset_index())

            band = Band(base='x', lower='lower', upper='upper', source=source, level='underlay',
                fill_alpha=0.3, line_width=1, line_color='green', fill_color="green")

            p.add_layout(band)

            
            p.scatter([point["x"]], [round(point["y"], 4)], fill_color="red", legend_label="Test point", size=8)

            return p
    except Exception as e:
        print("Error in plotting_classifications"+ str(e))
