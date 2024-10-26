"""
This code is mostly inspired from the PyTorch Lightning API, and is included 
only to give you an idea of the main steps you need to implement.
Feel free to modify the code as you see fit. 
"""


class Trainer:
    def __init__(self, *args, **kwargs):
        # TODO: set any required training arguments 
        pass

    def setup(self, *args, **kwargs):
        # TODO: setup your data, devices, models, optimizers etc.
        pass

    def training_step(self, input_batch, *args, **kwargs):
        # TODO: Write the training step for one single batch through your model
        # Your code might contain a forward pass, a backward pass and anything
        # else that is required.
        pass

    def validation_step(self, input_batch, *args, **kwargs):
        # TODO: Write the validation step for one single batch through your model
        pass

    def train(self, num_epochs: int=1, *args, **kwargs):
        for epoch_idx in enumerate(range(1, num_epochs+1)):
            # TODO: Train a single epoch
            # TODO: Print out the mean training loss and training accuracy at
            # the end of each epoch
            # TODO: Validate the model at each epoch
            # TODO: Print out the mean validation accuracy at the end of each epoch
            pass

    def validate(self, *args, **kwargs):
        # TODO: Run inference over the entire validation set
        pass