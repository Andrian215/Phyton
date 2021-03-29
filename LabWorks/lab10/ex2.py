  
import datetime

class GraphicFile:
    def __init__(self,title,extension,date_of_edit,sizes,color_depth):
        self.title = title
        self.extension = extension
        self.date_of_edit = date_of_edit
        self.sizes = sizes
        self.color_depth = color_depth
    def elapsed_time_since_last_edit(self):
        return datetime.datetime.now()-self.date_of_edit
    def file_size(self):
        return self.sizes*self.color_depth
    def name_change(self):
        return self.title
    def change_extension(self):
        return self.extension
    def number_of_shades_to_save(self):
        number_of_colors = 2**self.color_depth
        return number_of_colors
