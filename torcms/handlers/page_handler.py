# -*- coding:utf-8 -*-
import json

import tornado.escape
import tornado.web

import config
from torcms.core.base_handler import BaseHandler
from torcms.core import tools
from torcms.model.category_model import MCategory
from torcms.model.page_model import MPage
from torcms.model.page_hist_model import MPageHist

class PageHandler(BaseHandler):
    def initialize(self):
        self.init()
        self.mpage = MPage()
        self.mpage_hist = MPageHist()
        self.mcat = MCategory()
        self.cats = self.mcat.query_all()
        self.kind = '2'


    def get(self, url_str=''):
        url_arr = self.parse_url(url_str)

        if len(url_arr) == 1 and url_str.endswith('.html'):
            self.redirect(url_str.split('.')[0])
        elif url_arr[0] in ['modify', 'edit', '_edit']:
            self.to_modify(url_arr[1])
        elif url_str == 'list':
            self.list()
        elif url_arr[0] == 'ajax_count_plus':
            self.ajax_count_plus(url_arr[1])

        elif len(url_arr) == 1:
            self.to_view(url_str)
        else:
            self.render('html/404.html', userinfo=self.userinfo, kwd={})

    def post(self, url_str=''):
        url_arr = self.parse_url(url_str)

        if url_arr[0] in ['modify', 'edit', '_add']:
            self.update(url_arr[1])
        else:
            self.add_page()

    def to_view(self, slug):

        rec_page = self.mpage.get_by_uid(slug)

        if rec_page:
            if rec_page.kind == self.kind:
                self.viewit(rec_page)
            else:
                return False
        else:

            self.to_add(slug)

    @tornado.web.authenticated
    def to_add(self, citiao):
        if self.check_post_role(self.userinfo)['ADD']:
            pass
        else:
            return False
        kwd = {
            'cats': self.cats,
            'slug': citiao,
            'pager': '',
        }
        self.render('doc/page/page_add.html',
                    kwd=kwd,
                    userinfo=self.userinfo, )

    def __could_edit(self, slug):
        page_rec = self.mpage.get_by_uid(slug)
        if not page_rec:
            return False
        if self.check_post_role(self.userinfo)['EDIT'] or page_rec.user_name == self.userinfo.user_name:
            return True
        else:
            return False

    @tornado.web.authenticated
    def update(self, slug):
        if self.__could_edit(slug):
            pass
        else:
            return False
        post_data = self.get_post_data()

        if 'slug' in post_data:
            pass
        else:
            self.set_status(400)
            return False

        self.mpage_hist.insert_data(self.mpage.get_by_uid(slug))
        self.mpage.update(slug, post_data)

        self.redirect('/page/{0}.html'.format(post_data['slug']))

    @tornado.web.authenticated
    def to_modify(self, uid):
        if self.__could_edit(uid):
            pass
        else:
            return False

        kwd = {
            'pager': '',

        }
        self.render('doc/page/page_edit.html',
                    view=self.mpage.get_by_uid(uid),  # Deprecated
                    postinfo = self.mpage.get_by_uid(uid),
                    kwd=kwd,
                    unescape=tornado.escape.xhtml_unescape,
                    cfg=config.cfg,
                    userinfo=self.userinfo,
                    )

    def viewit(self, rec):
        kwd = {
            'pager': '',
        }
        # rec.user_name = rec.user_name
        self.render('doc/page/page_view.html',
                    view=rec, # Deprecated
                    postinfo = rec,
                    unescape=tornado.escape.xhtml_unescape,
                    kwd=kwd,
                    format_date=tools.format_date,
                    userinfo=self.userinfo,
                    cfg=config.cfg
                    )

    def ajax_count_plus(self, slug):
        output = {
            'status': 1 if self.mpage.view_count_plus(slug) else 0,
        }

        return json.dump(output, self)

    def list(self):
        kwd = {
            'pager': '',
            'unescape': tornado.escape.xhtml_unescape,
            'title': '单页列表',
        }
        self.render('doc/page/page_list.html',
                    kwd=kwd,
                    view=self.mpage.query_recent(),
                    view_all=self.mpage.query_all(),
                    format_date=tools.format_date,
                    userinfo=self.userinfo,
                    cfg=config.cfg
                    )

    @tornado.web.authenticated
    def add_page(self):
        if self.check_post_role(self.userinfo)['ADD']:
            pass
        else:
            return False

        #  post_data = {}
        # for key in self.request.arguments:
        #     post_data[key] = self.get_arguments(key)

        post_data = self.get_post_data()


        post_data['user_name'] = self.userinfo.user_name

        if 'slug' in post_data:
            pass
        else:
            self.set_status(400)
            return False

        if self.mpage.get_by_uid(post_data['slug']):
            self.set_status(400)
            return False
        else:
            self.mpage.insert_data(post_data)
            self.redirect('/page/{0}.html'.format(post_data['slug']))


class PageAjaxHandler(PageHandler):
    def initialize(self):
        self.init()
        self.mpage = MPage()
        self.mcat = MCategory()
        self.cats = self.mcat.query_all()
