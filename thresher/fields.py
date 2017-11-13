

class FactField(object):

    def __init__(self, source, keep_in_sync=False):
        self.source = source
        self.keep_in_sync = keep_in_sync


class RelatedFactField(object):

    def __init__(self, source):
        self.source = source
