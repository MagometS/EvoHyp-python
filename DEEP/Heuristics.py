import os
import subprocess

class Heuristics:
    def make_heuristic(self, recombination_gamma, recombination_strategy, gamma_init, ini_file, section):
        try:
            with open(ini_file, 'r') as file:
                # Logic to update the INI file
                # Not shown for brevity
                pass
        except IOError as e:
            print(e)

    def run_heuristic(self, ini_file, section):
        fit = 100.0
        part = "100.000000000000"

        try:
            file_name = os.path.basename(ini_file)
            command = "/home/maria_lyzhina/bin/deepmethod --default-name=/home/maria_lyzhina/hd/{} --settings-group={} --settings-file=/home/maria_lyzhina/hd/{}".format(file_name, section, file_name)
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            log_line = "wtime:-3.313857e+01 tau:14 freeze:0 score:100.000000000000"
            log_line1 = "wtime:-3.313857e+01 tau:14 freeze:0 score:100.000000000000"

            while True:
                line = p.stdout.readline().decode('utf-8').strip()
                if line == '':
                    break
                log_line = line

            part1 = log_line.split("cost:")
            print(part1[1])
            p.communicate()
            part = part1[1]

        except Exception as e:
            print(e)

        return part
