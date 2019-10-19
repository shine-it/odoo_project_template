# Copyright 2019 Shine It (www.openerp.cn)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from base64 import b64encode
from pkg_resources import Requirement, resource_string
from anthem.lyrics.records import create_or_update


def setup_company(ctx, req):
    """ Setup company """
    company = ctx.env.ref('base.main_company')
    company.name = '上海先安信息科技有限公司'

    # load logo on company
    logo_content = resource_string(req, 'data/images/logo.png')
    logo = b64encode(logo_content)
    company.logo = logo
    company.street = "Demo Street"
    company.website = "http://www.openerp.cn"
    company.email = "contact@openerp.cn"
    company.phone = "021-56473822"
    company.city = "上海市"
    company.currency_id  = ctx.env.ref('base.CNY')


def setup_language(ctx):
    """ install language and configure locale formatting """
    ctx.env['base.language.install'].create({'lang': 'zh_CN'}).lang_install()


def main(ctx):
    """ Create demo data """
    req = Requirement.parse('odoo-demo')
    setup_company(ctx, req)
    setup_language(ctx)
