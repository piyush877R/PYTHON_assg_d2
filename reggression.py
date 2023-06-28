from all_func import Flawless_Function



def minimise_loss(drill_func, inventory_functions, losing_activity):
    try:    
        function_with_smallest_error = None
        smallest_error = None
        for task in inventory_functions:
            Flaw = losing_activity(drill_func, task)
            if ((smallest_error == None) or Flaw < smallest_error):
                smallest_error = Flaw
                function_with_smallest_error = task

        ideal_activity = Flawless_Function(task=function_with_smallest_error, drill_func=drill_func,
                            Flaw=smallest_error)
        return ideal_activity
    except Exception as e:
        print("Error in minimise_loss"+ str(e))


def find_classification(point, ideal_activities):
    try:    
        current_lowest_classi = None
        current_lowest_space = None

        for ideal_activity in ideal_activities:
            try:
                locate_y_in_classi = ideal_activity.Finding_y_using_x(point["x"])
            except IndexError:
                print("This point is not in the classi function")
                raise IndexError

            
            space = abs(locate_y_in_classi - point["y"])

            if (abs(space < ideal_activity.Tolarance_s)):
                
                if ((current_lowest_classi == None) or (space < current_lowest_space)):
                    current_lowest_classi = ideal_activity
                    current_lowest_space = space

        return current_lowest_classi, current_lowest_space
    except Exception as e:
        print("Error in find_classification"+ str(e))
