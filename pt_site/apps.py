import json
import logging
import traceback

from django.apps import AppConfig
from django.db.models.signals import post_migrate

logger = logging.getLogger('ptools')


def app_ready_handler(sender, **kwargs):
    from pt_site.models import Site
    from pt_site.models import UserLevelRule
    logger.info('初始化站点信息')
    try:
        with open('pt_site_site.json', 'r') as f:
            # print(f.readlines())
            # Site.objects.filter(url='http://leaves.red/').update(url='https://leaves.red/')
            # UserLevelRule.objects.filter(site_id='http://leaves.red/').update(site_id='https://leaves.red/')
            data = json.load(f)
            logger.info('正在初始化站点规则信息表')
            # '更新规则中，返回结果为True为新建，为False为更新，其他是错误了')
            for site_rules in data:
                if site_rules.get('pk'):
                    del site_rules['pk']
                if site_rules.get('id'):
                    del site_rules['id']
                url = site_rules.get('url')
                site_obj = Site.objects.update_or_create(defaults=site_rules, url=url)
                msg = site_obj[0].name + (' 规则新增成功！' if site_obj[1] else '规则更新成功！')
                # logger.info(msg)

        with open('pt_site_userlevelrule.json', 'r') as file:
            upgrade_data = json.load(file)
            for upgrade in upgrade_data:
                if upgrade.get('id'):
                    del upgrade['id']
                upgrade['level'] = upgrade.get('level').replace(' ', '')
                upgrade['rights'] = upgrade.get('rights').replace(' ', '')
                upgrade_obj = UserLevelRule.objects.update_or_create(
                    site_id=upgrade.get('site_id'), level_id=upgrade.get('level_id'),
                    defaults=upgrade
                )
                # logger.info(
                #     f'{upgrade_obj[0].site.name} {"用户升级规则新增成功！" if site_obj[1] else "用户升级规则更新成功！"}')
        logger.info('数据库初始化完成！')
    except Exception as e:
        logger.error('初始化站点信息出错！{}'.format(e))
        logger.error(traceback.format_exc(limit=5))


class PtSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pt_site'
    verbose_name = '下载管理'

    def ready(self):
        # 环境变量不存在，说明数据库还未初始化，先跳过初始化站点数据
        # if os.path.exists('CONTAINER_ALREADY_STARTED_PLACEHOLDER'):
        #     logger.info('第一次启动容器，初始化数据库中')
        post_migrate.connect(app_ready_handler, sender=self)
