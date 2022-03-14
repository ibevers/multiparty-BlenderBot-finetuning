import parlai.core.build_data as build_data
import os

def build(opt):
    dpath = os.path.join(opt['datapath'], 'ubuntu')
    dpath = os.path.join("toy_train.txt")
    version = None

    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')
        if build_data.built(dpath):
            # An older version exists, so remove these outdated files.
            #build_data.remove_dir(dpath)
            pass
        build_data.make_dir(dpath)
        ## Download the data.
        #for downloadable_file in RESOURCES[:2]:
        #    downloadable_file.download_file(dpath)

        # Mark the data as built.
        build_data.mark_done(dpath, version_string=version)