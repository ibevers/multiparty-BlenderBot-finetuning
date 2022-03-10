import argparse
import json
#import copy
import generate_utils
#from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Conversation, ConversationalPipeline
#from flask import Flask
#from flask import request, jsonify

global conversation


if __name__ == "__main__":
    # TODO: parse the text input
    parser = argparse.ArgumentParser(description='Process some stuff.')
    parser.add_argument('input_json_file', metavar='input_json_file', type=str)
    parser.add_argument('output_json_file', metavar='output_json_file', type=str)
#    parser.add_argument('input_speech_list', metavar='input_speech_list', type=list)
#    parser.add_argument('nlp', metavar='nlp')
    parser.add_argument('num_perturbs', metavar='num_perturbs')
    args = parser.parse_args()

    outputs = generate_utils.generate_output(
        input_json_file=args.input_json_file,
        input_speech_list=None,
        nlp=None,
        num_perturbs=args.num_perturbs,
    )

#    with open(args.output_json_file, "w") as file_thing:
#        json.dump(outputs, file_thing)

    print(outputs)
