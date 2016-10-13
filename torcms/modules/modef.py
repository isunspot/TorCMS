# -*- coding:utf-8 -*-

from torcms.modules.base_modules import *
from torcms.modules.info_modules import *

core_modules = {'ModuleCatMenu': ModuleCatMenu,
                'get_footer': get_footer,
                'previous_post_link': previous_post_link,
                'next_post_link': next_post_link,
                'the_category': the_category,
                'list_categories': list_categories,
                'post_most_view': post_most_view,
                'post_random': post_random,
                'post_recent': post_recent,
                'link_list': link_list,
                'post_recent_most_view': post_recent_most_view,
                'post_cat_random': post_cat_random,
                'post_cat_recent': post_category_recent,
                'showout_recent': showout_recent,
                'generate_abstract': generate_abstract,
                'category_menu': category_menu,
                'site_url': site_url,
                'generate_description': generate_description,
                'reply_panel': reply_panel,
                'post_tags': post_tags,
                'post_catalogs': post_tags,
                'post_categories': post_tags,
                'copyright': copyright,
                'baidu_share': baidu_share,
                'catalog_pager': catalog_pager,
                'info_label_pager': info_label_pager,
                'doc_label_pager': doc_label_pager,
                'catalog_of': catalog_of,
                'app_catalog_of': app_catalog_of,
                'widget_search': widget_search,

                'Topline': ToplineModule,
                'Banner': BannerModule,
                'BreadCrumb': BreadCrumb,
                'parentname': parentname,
                'catname': catname,
                'ContactInfo': ContactInfo,
                'BreadcrumbPublish': BreadcrumbPublish,
                'ImgSlide': ImgSlide,
                'user_info': UserInfo,
                'vip_info': VipInfo,

                'rel_post2app': rel_post2app,
                'rel_app2post': rel_app2post,
                'app_most_used': app_most_used,
                'app_random_choose': app_random_choose,
                'app_tags': app_tags,
                'app_menu': app_menu,
                'app_user_recent': app_user_recent,
                'app_user_most': app_user_most,
                'app_recent_used': app_recent_used,
                'label_count': label_count,

                'amazon_ad': amazon_ad,
                'baidu_search': baidu_search,
                'site_ad': site_ad,
                'app_most_used_by_cat': app_most_used_by_cat,
                'app_least_used_by_cat': app_least_use_by_cat,
                'app_user_recent_by_cat': app_user_recent_by_cat,
                'widget_editor': widget_editor,
                'show_page': show_page,

                }
