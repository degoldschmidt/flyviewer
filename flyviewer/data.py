import os
import os.path as op

class Video(object):
    pass

class Data(object):
    def __init__(self, directory):
        self.dir = directory
        self.videos = []
        self.conditions = []
        conditions_file = op.join(directory, '{}_{}'.format(op.basename(directory), 'pytrack_out'))
        print(conditions_file)
        for files in os.listdir(directory):
            if files.endswith('avi'):
                self.videos.append(files)
                self.conditions.append('I dont know')

    def get_video(self, id):
        if id in self.videos:
            return op.join(self.dir, id)
        else:
            print(id, self.videos)
            return None
