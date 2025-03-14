import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Board from '@/views/board'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
    import news from '@/views/modules/news/list'
    import aboutus from '@/views/modules/aboutus/list'
    import yinlehaibao from '@/views/modules/yinlehaibao/list'
    import geshouxinxi from '@/views/modules/geshouxinxi/list'
    import syslog from '@/views/modules/syslog/list'
    import remenyinle from '@/views/modules/remenyinle/list'
    import forum from '@/views/modules/forum/list'
    import minyaoyinyue from '@/views/modules/minyaoyinyue/list'
    import discussyinlehaibao from '@/views/modules/discussyinlehaibao/list'
    import systemintro from '@/views/modules/systemintro/list'
    import yonghu from '@/views/modules/yonghu/list'
    import discussgeshouxinxi from '@/views/modules/discussgeshouxinxi/list'
    import discussremenyinle from '@/views/modules/discussremenyinle/list'
    import yinlefenlei from '@/views/modules/yinlefenlei/list'
    import config from '@/views/modules/config/list'
    import newstype from '@/views/modules/newstype/list'


//2.配置路由   注意：名字
export const routes = [{
    path: '/',
    name: '系统首页',
    component: Index,
    children: [{
      // 这里不设置值，是把main作为默认页面
      path: '/',
      name: '系统首页',
      component: Home,
      meta: {icon:'', title:'center', affix: true}
    }, {
      path: '/updatePassword',
      name: '修改密码',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/pay',
      name: '支付',
      component: pay,
      meta: {icon:'', title:'pay'}
    }, {
      path: '/center',
      name: '个人信息',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/news',
        name: '通知公告',
        component: news
      }
      ,{
	path: '/aboutus',
        name: '关于我们',
        component: aboutus
      }
      ,{
	path: '/yinlehaibao',
        name: '音乐海报',
        component: yinlehaibao
      }
      ,{
	path: '/geshouxinxi',
        name: '歌手信息',
        component: geshouxinxi
      }
      ,{
	path: '/syslog',
        name: '系统日志',
        component: syslog
      }
      ,{
	path: '/remenyinle',
        name: '热门音乐',
        component: remenyinle
      }
      ,{
	path: '/forum',
        name: '音乐论坛',
        component: forum
      }
      ,{
	path: '/minyaoyinyue',
        name: '民谣音乐',
        component: minyaoyinyue
      }
      ,{
	path: '/discussyinlehaibao',
        name: '音乐海报评论',
        component: discussyinlehaibao
      }
      ,{
	path: '/systemintro',
        name: '系统简介',
        component: systemintro
      }
      ,{
	path: '/yonghu',
        name: '用户',
        component: yonghu
      }
      ,{
	path: '/discussgeshouxinxi',
        name: '歌手信息评论',
        component: discussgeshouxinxi
      }
      ,{
	path: '/discussremenyinle',
        name: '热门音乐评论',
        component: discussremenyinle
      }
      ,{
	path: '/yinlefenlei',
        name: '音乐分类',
        component: yinlefenlei
      }
      ,{
	path: '/config',
        name: '轮播图管理',
        component: config
      }
      ,{
	path: '/newstype',
        name: '通知公告分类',
        component: newstype
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/board',
    name: 'board',
    component: Board,
    meta: {icon:'', title:'board'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '*',
    component: NotFound
  }
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
  mode: 'hash',
  /*hash模式改为history*/
  routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
   return originalPush.call(this, location).catch(err => err)
}
export default router;
