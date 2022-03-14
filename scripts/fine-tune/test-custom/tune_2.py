#cmd = "parlai train_model -t blended_skill_talk,wizard_of_wikipedia,convai2:normalized -m transformer/generator --multitask-weights 1,3,3,3 --init-model zoo:tutorial_transformer_generator/model --dict-file zoo:tutorial_transformer_generator/model.dict --embedding-size 512 --n-layers 8 --ffn-size 2048 --dropout 0.1 --n-heads 16 --learn-positional-embeddings True --n-positions 512 --variant xlm --activation gelu --fp16 True --text-truncate 512 --label-truncate 128 --dict-tokenizer bpe --dict-lower True -lr 1e-06 --optimizer adamax --lr-scheduler reduceonplateau --gradient-clip 0.1 -veps 0.25 --betas 0.9,0.999 --update-freq 1 --attention-dropout 0.0 --relu-dropout 0.0 --skip-generation True -vp 15 -stim 60 -vme 20000 -bs 16 -vmt ppl -vmm min --save-after-valid True --model-file /tmp/test_train_90M"


from parlai.scripts.train_model import TrainModel 


TrainModel.main( 
    
    task='vqa_v2'

    model = transformer/generator
    init_model=zoo:tutorial_transformer_generator/model

        
    n_heads=16
    n_layers=8
    n_positions=512
    text_truncate=512
    label_truncate=128
    ffn_size=2048
    embedding_size=512
    activation='gelu'
    variant='xlm'
    dict_lower=True
    dict_tokenizer='bpe'
    dict_file='zoo:tutorial_transformer_generator/model.dict'
    learn_positional_embeddings=True

    lr=1e-06
    optimizer='adamax'


    multitask-weights=1,3,3,3
    init-model=zoo:tutorial_transformer_generator/model
    dropout=0.1
    fp16=True
    lr-scheduler=reduceonplateau
    gradient-clip=0.1
    veps=0.25
    betas=0.9,0.999
    update-freq=1
    attention-dropout=0.0
    relu-dropout=0.0
    skip-generation=True
    vp=15
    stim=60
    vme=20000
    bs=16
    vmt=ppl
    vmm=min
    save-after-valid=True
    model-file=/tmp/test_train_90M

    )






#cmd = cmd.split(" -")
#print(cmd)
#for ln in cmd:
#    if ln[0] == '-':
#        ln = ln[1:]
#    ln = ln.replace(' ', '=')
#    print(ln)
