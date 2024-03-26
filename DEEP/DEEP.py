import os
import subprocess
from Heuristics import Heuristics


class DEEP:
    filename = None  # Class attribute to hold the filename

    def __init__(self, filename):
        DEEP.filename = filename

    def create_solution(self, heuristics):
        sections = [f"default_settings{i}" for i in range(15)]  # Creating section names
        fit = " "  # Initializing fit

        heuristics_map = {
            'A': "default_settings1",
            'B': "default_settings2",
            'C': "default_settings3",
            'D': "default_settings4",
            'E': "default_settings5",
            'F': "default_settings6",
            'G': "default_settings7",
            'H': "default_settings9",
            'I': "default_settings10",
            'J': "default_settings8",
            'K': "default_settings11",
            'L': "default_settings12",
            'M': "default_settings13",
            'N': "default_settings14",
            'O': "default_settings15",
            'P': "default_settings16",
            'Q': "default_settings17",
            'R': "default_settings18",
            'S': "default_settings19",
            'T': "default_settings20",
            'U': "default_settings21",
            'V': "default_settings22",
            'W': "default_settings23",
            'X': "default_settings24",
            'Y': "default_settings25",
            'Z': "default_settings26",
            'a': "default_settings27",
            'b': "default_settings28",
            'c': "default_settings29",
            'd': "default_settings30",
            'e': "default_settings31",
            'f': "default_settings32",
        }

        for c in heuristics:
            heuristics_obj = Heuristics()  # creating Heuristics object
            section_name = heuristics_map[c]  # getting section name from map
            fit = heuristics_obj.run_heuristic(self.filename, section_name)  # calling run_heuristic

        return fit

    def parse_fitness(self, log_file):
        fit = 0.0
        try:
            with open(log_file, 'r') as file:
                log_line = file.readline()
                print(log_line)
                parts = log_line.split("score:")
                score_parts = parts[1].split(" ")
                fit = float(score_parts[0])
        except Exception as e:
            print(e)
        return fit
