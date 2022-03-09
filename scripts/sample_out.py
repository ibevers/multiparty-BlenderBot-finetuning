from parlai.scripts.display_model import DisplayModel

DisplayModel.main(
    task='empathetic_dialogues',
    model_file='models/empathetic/model',
    num_examples=2,
)
