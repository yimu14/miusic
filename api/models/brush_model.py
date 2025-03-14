# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
# 个人信息
class yonghu(Base_model):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    zhanghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='账号' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    xingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='姓名' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    youxiang=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='邮箱' )
    shenfenzheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='身份证' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )

class remenyinle(Base_model):
    __doc__ = u'''remenyinle'''
    __tablename__ = 'remenyinle'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='用协'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    yinlefenlei=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='音乐分类' )
    fengmian=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    yuyan=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='语言' )
    zhuanji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='专辑' )
    shizhang=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='时长' )
    faxingfang=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='发行方' )
    geci=db.Column( db.Text,  nullable=True, unique=False,comment='歌词' )
    gequjianjie=db.Column( db.Text,  nullable=True, unique=False,comment='歌曲简介' )
    songname=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='歌名' )
    songfile=db.Column( db.Text, nullable=False, unique=False,comment='音乐文件' )
    singer=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='歌手' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    discussnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )

class yinlefenlei(Base_model):
    __doc__ = u'''yinlefenlei'''
    __tablename__ = 'yinlefenlei'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    yinlefenlei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='音乐分类' )

class yinlehaibao(Base_model):
    __doc__ = u'''yinlehaibao'''
    __tablename__ = 'yinlehaibao'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='是'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    gequmingcheng=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='歌曲名称' )
    yinlefenlei=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='音乐分类' )
    fengmian=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    geshou=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='歌手' )
    zhuanjimingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='专辑名称' )
    faxingriqi=db.Column( db.Date,  nullable=True, unique=False,comment='发行日期' )
    bofangliang=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='播放量' )
    goumailiang=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='购买量' )
    xiaichengdu=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='喜爱程度' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    discussnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )

class geshouxinxi(Base_model):
    __doc__ = u'''geshouxinxi'''
    __tablename__ = 'geshouxinxi'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='是'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    geshouxingming=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='歌手姓名' )
    geshouxingbie=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='歌手性别' )
    liupai=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='流派' )
    biaoqian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='标签' )
    chudaoriqi=db.Column( db.Date,  nullable=True, unique=False,comment='出道日期' )
    chengminggequ=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='成名歌曲' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    remengequ=db.Column( db.Text,  nullable=True, unique=False,comment='热门歌曲' )
    zhuanjijieshao=db.Column( db.Text,  nullable=True, unique=False,comment='专辑介绍' )
    geshoujieshao=db.Column( db.Text,  nullable=True, unique=False,comment='歌手介绍' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    discussnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )

class minyaoyinyue(Base_model):
    __doc__ = u'''minyaoyinyue'''
    __tablename__ = 'minyaoyinyue'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.Text,  nullable=True, unique=False,comment='标题' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    zuozhe=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='作者' )
    shoucang=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )
    share=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='分享数' )
    pinglun=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    bofang=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='播放数' )
    jieshao=db.Column( db.Text,  nullable=True, unique=False,comment='介绍' )
    xqdz=db.Column( db.Text,  nullable=True, unique=False,comment='详情地址' )

class forum(Base_model):
    __doc__ = u'''forum'''
    __tablename__ = 'forum'



    __authTables__={}
    __foreEndListAuth__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='帖子标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='帖子内容' )
    parentid=db.Column( db.BigInteger,default=0,  nullable=True, unique=False,comment='父节点id' )
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    username=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    isdone=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='状态' )
    istop=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='是否置顶' )
    toptime=db.Column( db.DateTime,  nullable=True, unique=False,comment='置顶时间' )

class syslog(Base_model):
    __doc__ = u'''syslog'''
    __tablename__ = 'syslog'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    username=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='用户名' )
    operation=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='用户操作' )
    method=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='请求方法' )
    params=db.Column( db.Text,  nullable=True, unique=False,comment='请求参数' )
    time=db.Column( db.BigInteger,default=0,  nullable=True, unique=False,comment='请求时长(毫秒)' )
    ip=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='IP地址' )

class newstype(Base_model):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    typename=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='分类名称' )

class news(Base_model):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'
    __intelRecom__='是'
    __browseClick__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    introduction=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    typename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='分类名称' )
    name=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='发布人' )
    headportrait=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )

class storeup(Base_model):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    refid=db.Column( db.BigInteger,default=0,  nullable=True, unique=False,comment='商品id' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='表名' )
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    type=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='类型' )
    inteltype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='推荐类型' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )

class aboutus(Base_model):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )

class systemintro(Base_model):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )

class discussremenyinle(Base_model):
    __doc__ = u'''discussremenyinle'''
    __tablename__ = 'discussremenyinle'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )

class discussyinlehaibao(Base_model):
    __doc__ = u'''discussyinlehaibao'''
    __tablename__ = 'discussyinlehaibao'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )

class discussgeshouxinxi(Base_model):
    __doc__ = u'''discussgeshouxinxi'''
    __tablename__ = 'discussgeshouxinxi'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger,default=0, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )

