
#Initialize the dataset
#Initialize the model
#train:
#python parlai/scripts/safe_interactive.py -t blended_skill_talk -mf zoo:blender/blender_90M/model

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

from parlai.scripts.train_model import TrainModel

TrainModel.main(
    # similar to before
    task='empathetic_dialogues', 
    model='transformer/generator',
    model_file='from_pretrained/model',
    
    # initialize with a pretrained model
    init_model="zoo:blender/blender_90M/model",

    # arguments we get from the pretrained model.
    # Unfortunately, these must be looked up separately for each model.
    n_heads=16, n_layers=8, n_positions=512, text_truncate=512,
    label_truncate=128, ffn_size=2048, embedding_size=512,
    activation='gelu', variant='xlm',
    dict_lower=True, dict_tokenizer='bpe',
    dict_file='zoo:tutorial_transformer_generator/model.dict',
    learn_positional_embeddings=True,
    
    # some training arguments, specific to this fine-tuning
    # use a small learning rate with ADAM optimizer
    lr=1e-5, optimizer='adam',
    warmup_updates=100,
    # early stopping on perplexity
    validation_metric='ppl',
    # train at most 10 minutes, and validate every 0.25 epochs
    max_train_time=600, validation_every_n_epochs=0.25,
    
    # depend on your gpu. If you have a V100, this is good
    batchsize=1, fp16=True, fp16_impl='mem_efficient',
    
    # speeds up validation
    skip_generation=True,
    
    # helps us cram more examples into our gpu at a time
    dynamic_batching='full'



import parlai.core.build_data as build_data
import os

def build(opt):
    dpath = os.path.join(opt['datapath'], 'SQuAD')
    version = None

    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')
        if build_data.built(dpath):
            # An older version exists, so remove these outdated files.
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Download the data.
        for downloadable_file in RESOURCES[:2]:
            downloadable_file.download_file(dpath)

        # Mark the data as built.
        build_data.mark_done(dpath, version_string=version)

import parlai.core.teachers.FixedDialogTeacher

class SquadTeacher(DialogTeacher):
    def __init__(self, opt, shared=None):
        self.datatype = opt['datatype']
        build(opt)  # NOTE: the call to build here
        suffix = 'train' if opt['datatype'].startswith('train') else 'dev'
        # whatever is placed into datafile will be passed as the argument to
        # setup_data in the next section.
        opt['datafile'] = os.path.join(opt['datapath'], 'SQuAD', suffix + '-v1.1.json')
        self.id = 'squad'
        super().__init__(opt, shared)


def setup_data(self, path):
    # note that path is the value provided by opt['datafile']
    print('loading: ' + path)
    with PathManager.open(path) as data_file:
        self.squad = json.load(data_file)['data']
    for article in self.squad:
        # each paragraph is a context for the attached questions
        for paragraph in article['paragraphs']:
            # each question is an example
            for qa in paragraph['qas']:
                question = qa['question']
                answers = tuple(a['text'] for a in qa['answers'])
                context = paragraph['context']
                yield {"text": content + "\n" + question, "labels": answers}, True














parlai train_model -t blended_skill_talk,wizard_of_wikipedia,convai2:normalized -m transformer/generator --multitask-weights 1,3,3,3 --init-model zoo:tutorial_transformer_generator/model --dict-file zoo:tutorial_transformer_generator/model.dict --embedding-size 512 --n-layers 8 --ffn-size 2048 --dropout 0.1 --n-heads 16 --learn-positional-embeddings True --n-positions 512 --variant xlm --activation gelu --fp16 True --text-truncate 512 --label-truncate 128 --dict-tokenizer bpe --dict-lower True -lr 1e-06 --optimizer adamax --lr-scheduler reduceonplateau --gradient-clip 0.1 -veps 0.25 --betas 0.9,0.999 --update-freq 1 --attention-dropout 0.0 --relu-dropout 0.0 --skip-generation True -vp 15 -stim 60 -vme 20000 -bs 16 -vmt ppl -vmm min --save-after-valid True --model-file /tmp/test_train_90M
)












