# -*- coding:utf-8 -*-

import config
from torcms.model.core_tab import CabPost
from torcms.model.core_tab import CabCatalog as CabLabel
from torcms.model.core_tab import CabPost2Catalog as CabPost2Label
from torcms.model.label_model import MLabel
from torcms.model.label_model import MPost2Label


class MInforLabel(MLabel):
    def __init__(self):
        self.tab = CabLabel
        self.tab2 = CabPost2Label



class MInfor2Label(MPost2Label):
    def __init__(self):
        self.tab = CabPost2Label
        self.tab_label = CabLabel
        self.tab_post = CabPost
        self.mtag = MInforLabel()
        try:
            CabPost2Label.create_table()
        except:
            pass

    def query_count(self, uid):
        return self.tab.select().where(self.tab.tag == uid).count()