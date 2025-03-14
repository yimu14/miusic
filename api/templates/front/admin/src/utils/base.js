const base = {
    get() {
        return {
            url : "http://localhost:8080/python1p21sd8o/",
            name: "python1p21sd8o",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于Python音乐平台设计和实现"
        } 
    }
}
export default base
