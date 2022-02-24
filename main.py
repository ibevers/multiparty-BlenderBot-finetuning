import argparse
import json
import copy
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Conversation, ConversationalPipeline
from flask import Flask
from flask import request, jsonify

global conversation

#@app.route('/add_input', methods = ['GET', 'POST'])
def add_input(text, convo):
#    text = request.json['text']
    convo.add_user_input(text)
    result = nlp([convo], do_sample=False, max_length=1000)
    messages = []
    for is_user, text in result.iter_texts():
        messages.append({
                        'is_user': is_user,
                        'text': text
                        })
#    return jsonify({
#                   'uuid': result.uuid,
#                   'messages': messages
#                   })
    return messages

#@app.route('/reset', methods = ['GET', 'POST'])
#def reset():
#    global conversation
#    conversation = Conversation()

def perturb(a_blurb, num_new_blurbs=10):
    many_blurbs = []
    # weird_chars = ["-", "(", ")", "*", "^", "@", "{", "}", "[", "]"]
    # weird_chars = ["b", "c", "d", "e", "f", "g", "h", "j", "k", "m"]
    weird_chars = ["b", "c", "d", "g", "m", "n", "o", "i", "a", "p"]
    weird_chars = weird_chars[:num_new_blurbs]
    for weird_char in weird_chars:
        new_blurb = a_blurb + " " + weird_char
        many_blurbs.append(new_blurb)
    return many_blurbs

def my_print(convo_response):
    for c, conv in enumerate(convo_response):
        print("------ PRINTING CONVERSATION " + str(c + 1) + " ------")
        for respon in conv:
            for line in respon:
                print(line)
        print("+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +")

if __name__ == "__main__":
    # TODO: parse the text input
    parser = argparse.ArgumentParser(description='Process some stuff.')
    parser.add_argument('input_text_json_path', metavar='input_text_json_path', type=str,
                        help='what would you like to say?')
    parser.add_argument('output_text_json_path', metavar='output_text_json_path', type=str,
                            help='what would you like to say?')
#    parser.add_argument('text2', metavar='text2', type=str,
#                            help='what would you like to say?')
    args = parser.parse_args()
    tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")
    nlp = ConversationalPipeline(model=model, tokenizer=tokenizer)
    
#    global conversation
    conversation = Conversation()
    
#    add_input(args.text1)
#
#    output = add_input(args.text2)
    file_object = open(args.input_text_json_path, "r")
    file_object_read = file_object.read()
    input_speeches = json.loads(file_object_read)
    super_outputs = []
#    print("LEN OF INPUT SPEECHES IS " + str(len(input_speeches)))
    for input_speech in input_speeches:
        output = None
        outputs = []
        speech_len = len(input_speech)
        assert speech_len == 2
        for b, blurt in enumerate(input_speech):
            if b < speech_len - 1:
                output = add_input(blurt, conversation)
            else:
#                print("ITS HAPPENING!!!")
                more_blurts = perturb(blurt) # 3 just for debugging
                for more_blurt in more_blurts:
                    old_conversation = copy.deepcopy(conversation)
                    output = add_input(more_blurt, convo=old_conversation)
                    outputs.append(output)
        super_outputs.append(outputs)

    with open(args.output_text_json_path, "w") as file_thing:
        json.dump(super_outputs, file_thing)
#    my_print(super_outputs)

    #app = Flask(__name__)



