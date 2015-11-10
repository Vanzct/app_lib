# -*- coding:utf-8 -*-
__author__ = 'Van'


name = u"张成涛"
alias = u"张寻"
name_en = "Van"
sex = u"男"
birthday = "1990-04-13"
age = 25
location = u"北京，朝阳区－望京地铁站附近"
jiguan = u"内蒙古"
home_town = u"内蒙古 锡林郭勒盟 多伦县 大北沟镇 十七号村"
hukou = u"农村户口"

phone = "18612596605"
mail = "heidazhangchengtao@163.com"

intro = u"3年 伪全栈 程序猿"
target = u"寻找有激情＋有活力的团队，做有情怀＋有逼格 的事情"

declaration_title = u'有追求的活着'
declaration = u'活着绝对不是朝十晚七，温饱自足，伟大从来不是一个人应该承担的事情，' \
              u'跟好的团队做有意义的事情，饱满的活着，也许做着做着就改变世界了呢'

employment_experience = [
    {
        # 创业团队
        "company_name": u"每每体育",
        "company_tag": u"运动社交",
        "depart": u"技术开发",
        "role": u"全栈工程师",
        "start_date": "2015-7",
        "end_date": "2015-11",
        "detail": u"被朋友拉去创业，也正好是我喜欢的项目，所以就加入了每每体育，每每体育要做一款全方位服务于运动活动的应用，"
                  u"初始名字叫－找炼， 找炼能解决我在运动活的中的很多痛点，虽然对钱方很不舍，还是决定离开。"
                  u"在每每的4个月，用磨刀做过产品原型，自己写了Club应用整个后台，后来在android同事离开后接手整理android代码，"
                  u"开发了图片分发网站，后来产品转向微信端，开始写前段。无奈资金没有及时得到补充，项目搁浅。",
        "experiences": [
            {
                "name": u"Club应用后台",
                "description": u"Club是一款服务于团队组织活动的应用，后台功能包括俱乐部的创建管理，活动的创建管理，个人信息和团队关系"
                               u"，俱乐部和活动的加入退出等，使用Ruby on Rails, 数据库使用MongoDb,图片存储使用七牛云服务，"
                               u"以及使用LeanCloud提供的短信验证服务",

                "role": u"因为团队第一个技术擅长Ruby，所以我用了两周时间学习了Ruby"
                        u"并在之后的一个月里独立开发了Club的后台大部分功能,在过程中了解并使用如七牛，Leancloud等云服务，"
                        u"数据库选用MongoDb,一切选择都只为更快的开发速度",

                "time": u"1个月"
            },
            {
                "name": u"Android客户端代码整理",
                "description": u"由于Android同事的离开，零时接管Android代码的开发，并继续开发了部分功能",

                "role": u"Android同事是一个对新技术有追求的同学，用了很多流行不久的框架，如Dagger,DataBinding等,"
                        u"将应用过分解耦，使得Android开发很难上手，并且开发速率缓慢，花了三周时间做了新的平衡，调整了结构",

                "time": u"1个月"
            },
            {
                "name": u"微信服务号开发",
                "description": u"由于新产品经理的入住，产品转向微信端，开发了图片浏览分发模块，地图模块和个人信息模块",

                "role": u"使用 AngularJs和Bootstrap框架开发微信服务号前端",

                "time": u"1个月"
            }
        ]

    },
    {
        # 钱方
        "company_name": u"钱方科技",
        "company_tag": u"电商",
        "depart": u"数据平台",
        "role": u"数据挖掘工程师",
        "start_date": "2014-11",
        "end_date": "2015-06",
        "detail": u"在钱方可以时间不长，离开也实属无奈，在钱方的半年里学会很多东西，也给我很大的空间。在钱方科技，主要是"
                  u"配置优化了Jenkins平台，使得项目发布更简单便捷；写了喵喵微店应用运营数据实时可视化和日报表Web；写了"
                  u"新项目日志收集和数据可视化Web.",
        "experiences": [
            {
                "name": u"运营数据可视化及日报表",
                "description": u"为了更实时的将运营数据显示给公司同事，让同事们能感知的到数据的改变，将运营数据实时的展现"
                               u"在Web页面上，并且将每天的汇总日报邮件发送给相关同事",
                "role": u"负责整个Web前后端的开发。前端使用H5，Jquery及highChart等，后台使用PHP读取Oracle里的数据，服务器"
                        u"Linux系统，截图使用PhontomJs，定时发送邮件使用Jenkins定时服务" ,
                "time": u"3周"
            },
            {
                "name": u"Jenkins服务搭建",
                "description": u"Jenkins是一个非常专业的支持持续集成的服务软件，可以通过简单的配置实现各种后台服务及客户端程序"
                               u"的发布上线，有良好的权限控制系统",
                "role": u"负责iOS应用和android应用的自动化发布部署，负责开发人员发布上线权限设置" ,
                "time": u"3周"
            },
            {
                "name": u"日志收集和数据可视化",
                "description": u"由于钱方的战略转移和新产品的开发，为了更好的跟踪项目数据和服务异常，决定从日志中收集数据，并且"
                               u"是绝对实时的日志收集和展示，数据展示的信息有运营数据和服务异常数据",
                "role": u"负责整个Web的开发和部署，后台语言使用Python，数据存储使用Mongodb和Redis，前端使用Bootstrap＋Jquery"
                        u"＋Less＋highChart，实时数据显示使用WebSocket",
                "time": u"2个月"
            }
        ]
    },
    {
        "company_name": u"搜狐畅游17173",
        "company_tag": u"游戏媒体",
        "depart": u"质量部，卓越运作",
        "start_date": "2013-11",
        "end_date": "2014-11",
        "detail": u"在搜狐畅游17173一年时间，因为android自动化测试经验进入，"
                  u"却一直未做自动化测试相关工作，做了一些内部项目数据收集分析及数据可视化的web项目，"
                  u"在17173一年时间里充实的工作让我学到了很多。不仅技术上学习掌握了很多东西，在团队合作"
                  u"及敏捷开发等方面也收获颇丰。在17173的工作结束于畅游内部地震，卓越运作部门全体裁员",
        "experiences": [
            {
                "name": u"内部项目数据可视化",
                "description": u"对公司内各种工具平台进行数据挖掘和分析，包括缺陷管理数据(Jira,Redmine)、"
                               u"项目管理数据、SVN和Trello等平台的数据，进行数据分析和可视化，"
                               u"用以监控内部项目状态。",
                "role": u"开发数据平台web系统主要功能，包括图表展现、图表编辑、权限、邮件发送等。"
                        u"使用技术：PHP/HTML5/JS/CSS/D3/Highcharts/Mysql/和Python 等；使用平台：Linux",
                "time": u"6个月"
            },
            {
                "name": u"移动应用的持续集成/交付",
                "description": u"为节约人力成本，提高开发与测试间合作效率，避免人为误操作，开发一套移动应用"
                               u"二维码交付平台。首先通过Jenkins对接应用版本控制系统（SVN），实现持续集成过程。"
                               u"持续集成产物为具有良好目录结构的目录结构。然后利用Web系统实现应用二维码扫描交"
                               u"付方式，即测试人员用手机扫描二维码可直接下载安装应用",
                "role": u"独立开发完成，实现Jenkins上的持续集成平台的搭建与配置，包括IOS和Android应用的自动编译打包，"
                        u"先后用JSP和PHP开发了两套Web系统，PHP版又经历了多次优化和重构。使用技术："
                        u"Java/PHP/HTML/JS/CSS和Mysql ;使用平台：Linux;Web容器Tomcat和Nginx。",
                "time": u"3个月"
            },
        ]
    },
    {
        "company_name": u"北京东软",
        "company_tag": u"外包服务",
        "depart": u"质量部，卓越运作",
        "start_date": "2012-07",
        "end_date": "2013-07",
        "detail": u"在东软参与东软内部的产品项目－易测云系统，一款类似于Testin测试云的云测系统，在项目中负责测试框架的开发和"
                  u"部分后台服务的开发。",
        "experiences": [
            {
                "name": u"Robotium和Athrun合并",
                "description": u"负责易测云项目手机端新测试框架的开发工作",
                "role": u"负责将Robotium框架和Athrun框架功能合并和优化工作，对Android测试底层代码有深入了解。"
                        u"对Robotium每一个函数都很清楚。与同事合作完成开发，使用技术：Java。",
                "time": u"3个月"
            },
            {
                "name": u"Android应用自动化遍历",
                "description": u"实现对市面上多数Android应用的自动遍历功能，主要属于UI测试，提供UI截图。"
                               u"其实是从底层对Robotium做了重构和优化，然后增加了应用路径识别算法方面的功能，"
                               u"将图片经过通信上传服务器",
                "role": u"独立完成架构设计与开发工作，主要语言Java,涉及到电脑手机间通信、多线程、文件读写、"
                        u"XML处理和图片处理等技术点。实现了微信、墨迹、糗百等多种应用的遍历。过程中阅读大量Android官方"
                        u"和非官方文档。使用技术：Java",
                "time": u"3个月"
            }
        ]
    }
]
tech_title = U"一个 伪全栈 程序猿的技术之路"
why_not = U"为什么是一个<span class='special'>伪</span>全栈 程序猿，因为要学习的地方还很多，很多想掌握的技术还没有掌握。" \
          U"毕业以后读了很多技术和互联网思维方面的书，随着用到的技术越来越多，看的书越来越多，对技术的理解也愈发深刻。"
techs = [
    {
        "name": "Java",
        "tags": ["Java", "Spring", "Tomcat", "Ant", "Roobtium", "UiAutomate", u"设计模式", u"多线程", u"异常"],
        "detail": U"使用Java是从大学开始，后来工作的前两年也都是在用Java，用过JSP，也用过SSH三大框架，后来在东软做云测平台，"
                  U"开始接触Android开发和云测平台，当时主要的语言就是Java，有一阵子每天醒来都能感觉自己在做跟代码相关的梦，"
                  U"为了解决工作中的技术难点，开了很多资料和博客，还有Android官方文档。后来学习了设计模式的知识和JVM相关知识，"
                  U"之后又学了PHP, Python, Ruby 和Js等语言，到现在还是最喜欢Java，当然每种语言都有它的设计哲学，我个人认为"
                  U"Java是最典雅的一门语言，使用Java写过小游戏，写过网站（J2EE），写过Android自动化框架，写过云测平台整个后台，"
                  U"写过过Android简单的应用"
    },
    {
        "name": "Python",
        "tags": ["Python", "Flask", "Uwsgi", "peewee", "pymongo", "qiniu", "redis", "websocket"],
        "detail": U"学习Python是在搜狐畅游工作中，用于收集畅游各种项目数据，随后就越来越多的使用Python写东西了。用Python写"
                  U"东西无疑是非常高效的，用Python写了爬虫，写过数据收集，写过网站后台等等。"
    },
    {
        "name": "Php",
        "tags": ["Jquery", "angularJs", "highchart", "npm", "bower", "bootstrap"],
        "detail": U"最初学Js时候是使用Jquery写简单的动画和异步数据处理，甚至很长时间以为Jquery就是Js，后来看了许多Js的"
                  U"书才理解的"


    },
    {
        "name": "Js",
        "tags": ["Jquery", "angularJs", "highchart", "npm", "bower", "bootstrap"],
        "detail": U"最初学Js时候是使用Jquery写简单的动画和异步数据处理，甚至很长时间以为Jquery就是Js，后来看了许多Js的"
                  U"书才理解异步原理和回调机制。"
    },
    {
        "name": "Ruby",
        "tags": ["Jquery", "angularJs", "highchart", "npm", "bower", "bootstrap"],
        "detail": U"最初学Js时候是使用Jquery写简单的动画和异步数据处理，甚至很长时间以为Jquery就是Js，后来看了许多Js的"
                  U"书才理解异步原理和回调机制。"
    },
]


