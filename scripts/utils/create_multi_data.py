import argparse
import json

import numpy as np

""""I don't wanna brag but ... I'm commenting my code rn.  This thing gets Ubuntu data good"""

def create_line(str):
    return "text:" + str


def  good_print(str):
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(str)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

if __name__ == "__main__":
    
    divider = " // "
    bot_divider = " "
    
    # TODO: parse the text input
    parser = argparse.ArgumentParser(description='Process some stuff.')
    parser.add_argument('input_text_json_path', metavar='input_text_json_path', type=str,
                        help='where should I get the stuff??')
    parser.add_argument('output_txt_path', metavar='output_txt_path', type=str,
                                            help='where should I put the stuff??')
                        #    parser.add_argument('text2', metavar='text2', type=str,
                        #                            help='what would you like to say?')
    args = parser.parse_args()

    file_object = open(args.input_text_json_path, "r")
    file_object_read = file_object.read()
    input_speeches = json.loads(file_object_read)
    num_things = len(input_speeches)
    good_print("NUM EXS: " + str(num_things))
    outputs = []
    freq = int(np.sqrt(num_things))
    # TODO: change format of each trainex before (or after ig) appending to outputs
    for t, train_ex in enumerate(input_speeches):
        if t % freq == 0:
            good_print("A good rational approximation of the progress, out of 1.0 is: " + str(t / freq))
        mess = train_ex["messages-so-far"]
        speakers = [snippet["speaker"] for snippet in mess]
        speaker_set = list(set(speakers)) # Is this stable?
        if len(speaker_set) < 3:
            continue # That a three person convo bro? No, it's gotta go
        
        for bot_will_be in speaker_set:
            if bot_will_be == "participant_0":
                continue # Too shy to text first...
            str_so_far = ""
            last_spoke = "NOBODY"
            staged_lines = []
            for snoopy in mess:
                current_speaker = snoopy["speaker"]
                current_utter = snoopy["utterance"]
                
                if current_speaker != bot_will_be: # Current speaker is a human
                    if last_spoke == "BOT":
                        staged_lines.append("text:" + str_so_far)
#                       output_ex.append(create_line(current_str, last_spoke, "NOPE"))
                        str_so_far = ""
                    str_so_far += current_speaker + ": "
                    str_so_far += current_utter
                    str_so_far += divider
                    last_spoke = "HUMAN"
                else: # Current speaker is the bot
                    if last_spoke == "HUMAN":
                        str_so_far += "labels:"
                    str_so_far += (current_utter + bot_divider)
                    last_spoke = "BOT"

            if last_spoke == "BOT":
                staged_lines.append("text:" + str_so_far)
            staged_lines[-1] = staged_lines[-1] + " episode_done:True"
            
            outputs.append(staged_lines)

#    with open(args.output_text_json_path, "w") as file_thing:
#        json.dump(outputs, file_thing)

    with open(args.output_txt_path, "w") as file_thing:
        for output in outputs:
            for data_line in output:
                print(data_line)
                file_thing.write(data_line)
                file_thing.write('\n')

