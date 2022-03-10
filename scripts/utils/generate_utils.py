import argparse
import json
import copy
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModel, Conversation, ConversationalPipeline
from flask import Flask
from flask import request, jsonify

global conversation

def add_input(text, convo, nlp_thing):
    #    text = request.json['text']
    convo.add_user_input(text)
    result = nlp_thing([convo], do_sample=False, max_length=1000)
    messages = []
    for is_user, text in result.iter_texts():
        messages.append({
                        'is_user': is_user,
                        'text': text
                        })
    return messages

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
#        for respon in conv:
#            for line in respon:
#                print(line)
        print(conv)
        print("+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +")

def collapse(lst, num_copies):
    new_lst = []
    iters = int(len(lst) / num_copies)
    for i in range(iters):
        new_lst.append(lst[i * num_copies: (i + 1) * num_copies])
    return new_lst

def generate_output(input_json_file=None, input_speech_list=None, nlp=None, num_perturbs=10):
    if nlp is None:
        tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
        # model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")
        # model = TypeOfModel.from_pretrained("")
        model = AutoModel.from_pretrained("/Users/matthewking/CS224_Final_Project/model")
        nlp = ConversationalPipeline(model=model, tokenizer=tokenizer)
    
#    conversation = Conversation()

    assert input_json_file is None or input_speech_list is None
    assert input_json_file is not None or input_speech_list is not None

    if input_json_file is not None:
        file_object = open(input_json_file, "r")
        file_object_read = file_object.read()
        input_speech_list = json.loads(file_object_read)

#    super_outputs = []

    conversations = []
    for input_speech in input_speech_list:
        one_sided = ""
        for b, blurt in enumerate(input_speech):
            one_sided += blurt
            if b < len(input_speech) - 1:
                one_sided += "  //  "
        perturbs = perturb(one_sided, num_perturbs)
        for pertur in perturbs:
            new_convo = Conversation()
            new_convo.add_user_input(pertur)
            conversations.append(new_convo)
#        for blurt in input_speech:
#            new_convo.add_user_input(blurt)
#            new_convo.mark_processed()

    uncollapsed_outputs = nlp(conversations, do_sample=False, max_length=1000)

    outputs = collapse(uncollapsed_outputs, num_perturbs)

#    messages = []
#for is_user, text in result.iter_texts():
#    messages.append({
#                    'is_user': is_user,
#                    'text': text
#                    })
#                    return messages

    return outputs


#    for input_speech in input_speech_list:
#        output = None
#            outputs = []
#            speech_len = len(input_speech)
#            assert speech_len == 2
#                for b, blurt in enumerate(input_speech):
#                    if b < speech_len - 1:
#                        output = add_input(blurt, conversation)
#                            else:
#                                more_blurts = perturb(blurt)
#                                for more_blurt in more_blurts:
#                                    old_conversation = copy.deepcopy(conversation)
#                                    output = add_input(more_blurt, convo=old_conversation)
#                                    outputs.append(output)
#                                        super_outputs.append(outputs)
#
#    return super_outputs



#    my_print(super_outputs)





