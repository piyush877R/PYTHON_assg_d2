def quad_error(first_func, second_func):
    try:   
        extent = second_func - first_func
        extent["y"] = extent["y"] ** 2
        all_variation = sum(extent["y"])
        return all_variation
    except Exception as e:
        print("Error in quad_error", str(e))
