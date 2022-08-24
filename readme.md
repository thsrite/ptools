# pt助手开发

[![simpleui](https://img.shields.io/badge/developing%20with-Simpleui-2077ff.svg)](https://github.com/newpanjing/simpleui)

### 基本信息

1. 技术栈：Docker、Python、Sqlite3,celery
2. 开发工具：pycharm
3. 部署方式：docker-compose部署
4. 用到的Python包：
   ```bash
   # DJango后台美化
   pip install django-simpleui
   # 汉字简繁转化
   pip install opencc
   # 破cf盾
   pip install cloudscraper
   # django定时任务
   pip install django-apscheduler
   # django redis支持
   pip install django-redis
   # 下载器接口
   pip install transmission-rpc qbittorrent-api deluge-client
   ```

### 功能实现

| 日期 | 功能                                                                               | 实现                                                                                      |
| ------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| 0717 | 站点管理（内附爬虫规则、站点授权信息）                                             | 已实现，支持站点见下表                                                                    |
| 0718 | 抓取种子信息                                                                       | 已实现                                                                                    |
| 0719 | 下载器管理                                                                         | 已实现，目前仅支持Transmission，qBittorrent下载器添加任务不返回任务信息，需迂回，容后处理 |
| 0720 | 推送种子到下载器                                                                   | 已实现                                                                                    |
| 0721 | 推送种子后下载任务与种子信息关联                                                   | 已关联，但目前仅支持Tr                                                                    |
| 0725 | 签到功能                                                                           | 已实现                                                                                    |
| 0729 | 实现站点个人数据抓取                                                               |                                                                                           |
| 0801 | 多线程开发                                                                         | 已实现                                                                                    |
| 0802 | 重构部分代码，将用户数据与站点配置文件分离，防止误操作                             | 已完成                                                                                    |
| 0805 | docker部署                                                                         | 已实现                                                                                    |
| 0806 | 定时任务                                                                           | 已实现                                                                                    |
| 0808 | 通知服务                                                                           | 已实现，企业微信需要可信IP，可能需要自行添加                                              |
| -    | 实时监控种子上传下载信息（开发下载器主页，通过hash与种子关联，并获取种子促销信息） | 未开发                                                                                    |
| -    | 后台推送种子信息                                                                   | 计划内，未开发                                                                            |

### 更新日志

- > 2022.08.24
  >

  - > 发布PTools1.0版本
    >

    1. 支持站点列表附后
    2. 支持多站签到，支持天空验证码签到
    3. 支持拉取多站个人数据信息
    4. 支持多站拉取首页种子信息
    5. 支持企业微信、WxPusher、PushDeer、Bark通知
    6. 支持定时任务
       1. 支持自动签到，默认一天签到三次，每七小时签到一次，保留签到状态，已签到的不会重复签到
       2. 支持自动拉取个人数据，默认五个小时拉取一次
       3. 支持自动拉取首页促销种子，默认五个小时拉取一次
    7. 提供一份NP架构站点通用配置，未适配站点可以通过XPATH自行适配

### 站点支持列表

> 2022.08.03支持列表，根本本人现有站点数据整理


| 序号 | 站点             | 签到 | 个人数据 | 推送种子 |
| ------ | ------------------ | ------ | ---------- | ---------- |
| 1    | 阿童木           | 支持 | 支持     | 支持     |
| 2    | 猪猪网           | 支持 | 支持     | 支持     |
| 3    | 学校             | 支持 | 支持     | 支持     |
| 4    | 1PT              | 支持 | 支持     | 支持     |
| 5    | ASL              | 支持 | 支持     | 支持     |
| 6    | CarPT            | 支持 | 支持     | 支持     |
| 7    | 高清视界HDArea   | 支持 | 支持     | 支持     |
| 8    | 红豆饭HDFans     | 支持 | 支持     | 支持     |
| 9    | 时光HDTIME       | 支持 | 支持     | 支持     |
| 10   | MTeam            | 支持 | 支持     | 支持     |
| 11   | HDZONE           | 支持 | 支持     | 支持     |
| 12   | 冬樱WinterSakura | 支持 | 支持     | 支持     |
| 13   | 蚂蚁HDMayi       | 支持 | 支持     | 支持     |
| 14   | 自由农场         | 支持 | 支持     | 支持     |
| 15   | 铂金学院         | 支持 | 不支持   | 支持     |
| 16   | 烧包             | 无需 | 支持     | 支持     |
| 17   | 海棠             | 支持 | 支持     | 支持     |
| 18   | 欧神             | 支持 | 支持     | 支持     |
| 19   | 时间PTT          | 支持 | 支持     | 支持     |
| 20   | 海带             | 无需 | 支持     | 支持     |
| 21   | 白兔             | 支持 | 支持     | 支持     |
| 22   | 芒果             | 支持 | 支持     | 支持     |
| 23   | 艾薇             | 无需 | 支持     | 支持     |
| 24   | 老师             | 支持 | 支持     | 支持     |
| 25   | 马杀鸡           | 无需 | 支持     | 支持     |
| 26   | 欧绅             | 无需 | 支持     | 支持     |
| 27   | 备胎             | 无需 | 支持     | 支持     |
| 28   | 观众             | 支持 | 支持     | 支持     |
| 29   | 丐帮             | 支持 | 支持     | 支持     |
| 30   | 明教             | 支持 | 支持     | 支持     |
| 21   | 天空HDSKY        | 支持 | 支持     | 不支持   |
| 32   | 杜比             | 支持 | 支持     | 不支持   |
| 33   | 海胆             | 支持 | 支持     | 不支持   |
| 34   | 海豹             | 无需 | 不支持   | 不支持   |
| 35   | 明教             | 支持 | 支持     | 支持     |
| 36   | 月月             | 支持 | 支持     |          |
| 37   | 吐鲁番           | 支持 | 支持     |          |
| 38   | 城市             | 支持 | 支持     |          |
| 39   | 铂金家           | 支持 | 支持     |          |
| 40   | 梓喵             | 支持 | 支持     |          |
| 41   | TTG              |      |          |          |
|      |                  |      |          |          |
|      |                  |      |          |          |

### 捐助记录

- ## 感谢大佬捐助支持本项目！！！
- > viichien 大佬第一个捐助本项目，使我更有动力继续写下去！
  >
