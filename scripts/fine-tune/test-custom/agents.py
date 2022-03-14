from ParlAI.parlai.core.teachers import ParlAIDialogTeacher
from .build import build
import os
import copy


def _path(opt, filtered):
    # build the data if it does not exist
    #build(opt)
    #build(opt)

    #dt = opt['datatype'].split(':')[0]

    #if dt == 'train':
    #    prefix = 'train'
    ## Using matched set as valid and mismatched set as test
    #elif dt == 'valid':
    #    prefix = 'dev'
    #elif dt == 'test':
    #    prefix = 'test'
    #else:
    #    raise RuntimeError('Not valid datatype.')

    #data_path = os.path.join(opt['datapath'], AQUA, AQUA, prefix + '.tok.json')
    data_path = os.path.join("/Users/isaacbevers/cs-projects/cs224n/final/cs224n-final-project/data/mini-test/ubuntu_mini_parlai_format.txt")
    return data_path



class DefaultTeacher(ParlAIDialogTeacher):
    def __init__(self, opt, shared=None):
        opt = copy.deepcopy(opt)

        # get datafile
        opt['parlaidialogteacher_datafile'] = _path(opt, '')

        super().__init__(opt, shared)

#class DefaultTeacher(ParlAIDialogTeacher):
#    def __init__(self, opt, shared=None):
#        opt = copy.deepcopy(opt)
#
#        # get datafile
#        opt['parlaidialogteacher_datafile'] = _path(opt, '')
#
#        super().__init__(opt, shared)
