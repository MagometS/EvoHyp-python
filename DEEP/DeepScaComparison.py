from DeepProblem import DeepProblem
from ScaProblem import ScaProblem
from Heuristics import Heuristics
from SCA import SCA

class DeepScaComparison:
    heuristics = None

    def __init__(self, filename) :
        self.filename = filename
    

    def create_solution(self, heuristics):
        sections = [f"default_settings{i}" for i in range(15)]  # Creating section names
        fit = " "  # Initializing fit

        heuristics_map_deep = {
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
            'c': "default_settings29",
            'd': "default_settings30",
            'e': "default_settings31",
            'f': "default_settings32",
        }

        heuristics_map_sca = {'g': "sca_default_settings1"}

        
        for heuristic_key in heuristics:
            if heuristic_key in heuristics_map_deep.keys():
                heuristics_obj = Heuristics()  # creating Heuristics object
                section_name = heuristics_map_deep[heuristic_key]  # getting section name from map
                fit = heuristics_obj.run_heuristic(self.filename, section_name)  # calling run_heuristic
            
            if heuristic_key in heuristics_map_sca.keys():
                sca = SCA(self.filename)
                section_name = heuristics_map_sca[heuristic_key]
                fit = sca.run_heuristic(section_name)


        return fit


    
