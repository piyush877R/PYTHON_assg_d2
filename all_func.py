import  pandas as pd
from sqlalchemy import create_engine as CE


class Managing_Functions:
    try:
        def __init__(self, Location_of_CSV_File):
            
            self._M_func = []

            
            try:
                self._M_func_data = pd.read_csv(Location_of_CSV_File)
            except FileNotFoundError:
                print("Issue while reading file {}".format(Location_of_CSV_File))
                raise

            
            Value_of_X = self._M_func_data["x"]

            
            for name_for_column, data_in_column in self._M_func_data.items():
                if "x" in name_for_column:
                    continue
                
                Sub_Set = pd.concat([Value_of_X, data_in_column], axis=1)
                task = Task.amongst_dataframe(name_for_column, Sub_Set)
                self._M_func.append(task)


        def to_sql(self, Name_of_file, Suff):
            
            Engine = CE('sqlite:///{}.db'.format(Name_of_file), echo=False)

            
            Duplicate_of_func_data = self._M_func_data.copy()
            Duplicate_of_func_data.columns = [tag.capitalize() + Suff for tag in Duplicate_of_func_data.columns]
            Duplicate_of_func_data.set_index(Duplicate_of_func_data.columns[0], inplace=True)

            Duplicate_of_func_data.to_sql(
                Name_of_file,
                Engine,
                if_exists="replace",
                index=True,
            )

        @property
        def func_S(self):
            
            return self._M_func

        def __iter__(self):
            
            return ManageFuncIterator(self)

        def __repr__(self):
            return "Contains {} number of functions".format(len(self.func_S))
    except Exception as e:
        print("Error in Managing_Functions"+ str(e))


class ManageFuncIterator():
    try:
        def __init__(self, manage_func):
            
            self._index = 0
            self._manage_function = manage_func

        def __next__(self):
            
            if self._index < len(self._manage_function.func_S):
                requested_value_ = self._manage_function.func_S[self._index]
                self._index = self._index + 1
                return requested_value_
            raise StopIteration
    except Exception as e:
        print("Error in ManageFuncIterator"+ str(e))


class Task:
    try:
        def __init__(self, tag):
            
            self._tag = tag
            self.dataframe = pd.DataFrame()

        def Finding_y_using_x(self, x):
            
            Search_Pointer = self.dataframe["x"] == x
            try:
                return self.dataframe.loc[Search_Pointer].iat[0, 1]
            except IndexError:
                raise IndexError


        @property
        def tag(self):
            
            return self._tag

        def __iter__(self):
            return Itrator_of_Functions(self)

        def __sub__(self, additional):
            
            contrast  = self.dataframe - additional.dataframe
            return contrast 

        @classmethod
        def amongst_dataframe(cls, tag, dataframe):
            
            task = cls(tag)
            task.dataframe = dataframe
            task.dataframe.columns = ["x", "y"]
            return task

        def __repr__(self):
            return "Function for {}".format(self.tag)
    except Exception as e:
        print("Error in Task"+ str(e))

class Flawless_Function(Task):
    try:    
        def __init__(self, task, drill_func, Flaw):
            
            super().__init__(task.tag)
            self.dataframe = task.dataframe

            self.drill_func = drill_func
            self.Flaw = Flaw
            self._Values_tolerance = 1
            self._Tolarance_s = 1

        def _determine_largest_deviation(self, ideal_activity , train_activity):
            
            extent = train_activity - ideal_activity 
            extent["y"] = extent["y"].abs()
            Big_difference = max(extent["y"])
            return Big_difference

        @property
        def Tolarance_s(self):
            
            self._Tolarance_s = self.tolerance_factor * self.Big_difference
            return self._Tolarance_s

        @Tolarance_s.setter
        def Tolarance_s(self, value):

            self._Tolarance_s = value

        @property
        def tolerance_factor(self):
            
            return self._Values_tolerance

        @tolerance_factor.setter
        def tolerance_factor(self, value):
            self._Values_tolerance = value

        @property
        def Big_difference(self):
            
            Big_difference = self._determine_largest_deviation(self, self.drill_func)
            return Big_difference
    except Exception as e:
        print("Error in Flawless_Function"+ str(e))


class Itrator_of_Functions:
    try:
        def __init__(self, task):
            
            self._func = task
            self._index = 0

        def __next__(self):
            
            if self._index < len(self._func.dataframe):
                series_of_value_requested = (self._func.dataframe.iloc[self._index])
                point = {"x": series_of_value_requested.x, "y": series_of_value_requested.y}
                self._index += 1
                return point
            raise StopIteration
    except Exception as e:
        print("Error in Itrator_of_Functions"+ str(e))

