import VueRouter from 'vue-router'

//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Forum from '../pages/forum/list'
import ForumAdd from '../pages/forum/add'
import ForumDetail from '../pages/forum/detail'
import MyForumList from '../pages/forum/myForumList'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import payList from '../pages/pay'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import remenyinleList from '../pages/remenyinle/list'
import remenyinleDetail from '../pages/remenyinle/detail'
import remenyinleAdd from '../pages/remenyinle/add'
import yinlefenleiList from '../pages/yinlefenlei/list'
import yinlefenleiDetail from '../pages/yinlefenlei/detail'
import yinlefenleiAdd from '../pages/yinlefenlei/add'
import yinlehaibaoList from '../pages/yinlehaibao/list'
import yinlehaibaoDetail from '../pages/yinlehaibao/detail'
import yinlehaibaoAdd from '../pages/yinlehaibao/add'
import geshouxinxiList from '../pages/geshouxinxi/list'
import geshouxinxiDetail from '../pages/geshouxinxi/detail'
import geshouxinxiAdd from '../pages/geshouxinxi/add'
import minyaoyinyueList from '../pages/minyaoyinyue/list'
import minyaoyinyueDetail from '../pages/minyaoyinyue/detail'
import minyaoyinyueAdd from '../pages/minyaoyinyue/add'
import syslogList from '../pages/syslog/list'
import syslogDetail from '../pages/syslog/detail'
import syslogAdd from '../pages/syslog/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'
import aboutusList from '../pages/aboutus/list'
import aboutusDetail from '../pages/aboutus/detail'
import aboutusAdd from '../pages/aboutus/add'
import systemintroList from '../pages/systemintro/list'
import systemintroDetail from '../pages/systemintro/detail'
import systemintroAdd from '../pages/systemintro/add'
import discussremenyinleList from '../pages/discussremenyinle/list'
import discussremenyinleDetail from '../pages/discussremenyinle/detail'
import discussremenyinleAdd from '../pages/discussremenyinle/add'
import discussyinlehaibaoList from '../pages/discussyinlehaibao/list'
import discussyinlehaibaoDetail from '../pages/discussyinlehaibao/detail'
import discussyinlehaibaoAdd from '../pages/discussyinlehaibao/add'
import discussgeshouxinxiList from '../pages/discussgeshouxinxi/list'
import discussgeshouxinxiDetail from '../pages/discussgeshouxinxi/detail'
import discussgeshouxinxiAdd from '../pages/discussgeshouxinxi/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'forum',
					component: Forum
				},
				{
					path: 'forumAdd',
					component: ForumAdd
				},
				{
					path: 'forumDetail',
					component: ForumDetail
				},
				{
					path: 'myForumList',
					component: MyForumList
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'remenyinle',
					component: remenyinleList
				},
				{
					path: 'remenyinleDetail',
					component: remenyinleDetail
				},
				{
					path: 'remenyinleAdd',
					component: remenyinleAdd
				},
				{
					path: 'yinlefenlei',
					component: yinlefenleiList
				},
				{
					path: 'yinlefenleiDetail',
					component: yinlefenleiDetail
				},
				{
					path: 'yinlefenleiAdd',
					component: yinlefenleiAdd
				},
				{
					path: 'yinlehaibao',
					component: yinlehaibaoList
				},
				{
					path: 'yinlehaibaoDetail',
					component: yinlehaibaoDetail
				},
				{
					path: 'yinlehaibaoAdd',
					component: yinlehaibaoAdd
				},
				{
					path: 'geshouxinxi',
					component: geshouxinxiList
				},
				{
					path: 'geshouxinxiDetail',
					component: geshouxinxiDetail
				},
				{
					path: 'geshouxinxiAdd',
					component: geshouxinxiAdd
				},
				{
					path: 'minyaoyinyue',
					component: minyaoyinyueList
				},
				{
					path: 'minyaoyinyueDetail',
					component: minyaoyinyueDetail
				},
				{
					path: 'minyaoyinyueAdd',
					component: minyaoyinyueAdd
				},
				{
					path: 'syslog',
					component: syslogList
				},
				{
					path: 'syslogDetail',
					component: syslogDetail
				},
				{
					path: 'syslogAdd',
					component: syslogAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
				{
					path: 'aboutus',
					component: aboutusList
				},
				{
					path: 'aboutusDetail',
					component: aboutusDetail
				},
				{
					path: 'aboutusAdd',
					component: aboutusAdd
				},
				{
					path: 'systemintro',
					component: systemintroList
				},
				{
					path: 'systemintroDetail',
					component: systemintroDetail
				},
				{
					path: 'systemintroAdd',
					component: systemintroAdd
				},
				{
					path: 'discussremenyinle',
					component: discussremenyinleList
				},
				{
					path: 'discussremenyinleDetail',
					component: discussremenyinleDetail
				},
				{
					path: 'discussremenyinleAdd',
					component: discussremenyinleAdd
				},
				{
					path: 'discussyinlehaibao',
					component: discussyinlehaibaoList
				},
				{
					path: 'discussyinlehaibaoDetail',
					component: discussyinlehaibaoDetail
				},
				{
					path: 'discussyinlehaibaoAdd',
					component: discussyinlehaibaoAdd
				},
				{
					path: 'discussgeshouxinxi',
					component: discussgeshouxinxiList
				},
				{
					path: 'discussgeshouxinxiDetail',
					component: discussgeshouxinxiDetail
				},
				{
					path: 'discussgeshouxinxiAdd',
					component: discussgeshouxinxiAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
