<template>
	<div class="addEdit-block" :style='{"width":"100%","padding":"30px","margin":"0","color":"#fff","background":"none"}'>
		<el-form
			:style='{"padding":"30px","boxShadow":"none","borderRadius":"6px","alignItems":"flex-start","flexWrap":"wrap","display":"flex"}'
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="180px"
		>
			<template >
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="歌曲名称" prop="gequmingcheng">
					<el-input v-model="ruleForm.gequmingcheng" placeholder="歌曲名称" clearable  :readonly="ro.gequmingcheng"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else class="input" label="歌曲名称" prop="gequmingcheng">
					<el-input v-model="ruleForm.gequmingcheng" placeholder="歌曲名称" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="select" v-if="type!='info'"  label="音乐分类" prop="yinlefenlei">
					<el-select :disabled="ro.yinlefenlei" v-model="ruleForm.yinlefenlei" placeholder="请选择音乐分类" >
						<el-option
							v-for="(item,index) in yinlefenleiOptions"
							v-bind:key="index"
							:label="item"
							:value="item">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else class="input" label="音乐分类" prop="yinlefenlei">
					<el-input v-model="ruleForm.yinlefenlei"
						placeholder="音乐分类" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="upload" v-if="type!='info' && !ro.fengmian" label="封面" prop="fengmian">
					<file-upload
						tip="点击上传封面"
						action="file/upload"
						:limit="3"
						:multiple="true"
						:fileUrls="ruleForm.fengmian?ruleForm.fengmian:''"
						@change="fengmianUploadChange"
					></file-upload>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="upload" v-else-if="ruleForm.fengmian" label="封面" prop="fengmian">
					<img v-if="ruleForm.fengmian.substring(0,4)=='http'" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.fengmian.split(',')[0]" width="100" height="100">
					<img v-else class="upload-img" style="margin-right:20px;" v-bind:key="index" v-for="(item,index) in ruleForm.fengmian.split(',')" :src="$base.url+item" width="100" height="100">
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="歌手" prop="geshou">
					<el-input v-model="ruleForm.geshou" placeholder="歌手" clearable  :readonly="ro.geshou"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else class="input" label="歌手" prop="geshou">
					<el-input v-model="ruleForm.geshou" placeholder="歌手" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="专辑名称" prop="zhuanjimingcheng">
					<el-input v-model="ruleForm.zhuanjimingcheng" placeholder="专辑名称" clearable  :readonly="ro.zhuanjimingcheng"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else class="input" label="专辑名称" prop="zhuanjimingcheng">
					<el-input v-model="ruleForm.zhuanjimingcheng" placeholder="专辑名称" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="date" v-if="type!='info'" label="发行日期" prop="faxingriqi">
					<el-date-picker
						format="yyyy 年 MM 月 dd 日"
						value-format="yyyy-MM-dd"
						v-model="ruleForm.faxingriqi" 
						type="date"
						:readonly="ro.faxingriqi"
						placeholder="发行日期"
					></el-date-picker> 
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="input" v-else-if="ruleForm.faxingriqi" label="发行日期" prop="faxingriqi">
					<el-input v-model="ruleForm.faxingriqi" placeholder="发行日期" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="播放量" prop="bofangliang">
					<el-input v-model.number="ruleForm.bofangliang" placeholder="播放量" clearable  :readonly="ro.bofangliang"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else class="input" label="播放量" prop="bofangliang">
					<el-input v-model="ruleForm.bofangliang" placeholder="播放量" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="购买量" prop="goumailiang">
					<el-input v-model.number="ruleForm.goumailiang" placeholder="购买量" clearable  :readonly="ro.goumailiang"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else class="input" label="购买量" prop="goumailiang">
					<el-input v-model="ruleForm.goumailiang" placeholder="购买量" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="喜爱程度" prop="xiaichengdu">
					<el-input v-model="ruleForm.xiaichengdu" placeholder="喜爱程度" clearable  :readonly="ro.xiaichengdu"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else class="input" label="喜爱程度" prop="xiaichengdu">
					<el-input v-model="ruleForm.xiaichengdu" placeholder="喜爱程度" readonly></el-input>
				</el-form-item>
			</template>
			<el-form-item :style='{"width":"100%","padding":"0","margin":"0"}' class="btn">
				<el-button class="btn3"  v-if="type!='info'" type="success" @click="onSubmit">
					<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","height":"40px"}'></span>
					提交
				</el-button>
				<el-button class="btn4" v-if="type!='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","height":"40px"}'></span>
					取消
				</el-button>
				<el-button class="btn5" v-if="type=='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan" :style='{"margin":"0 2px","fontSize":"14px","color":"#fff","height":"40px"}'></span>
					返回
				</el-button>
			</el-form-item>
		</el-form>
    

  </div>
</template>
<script>
import { 
	isIntNumer,
} from "@/utils/validate";
export default {
	data() {
		var validateIntNumber = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isIntNumer(value)) {
				callback(new Error("请输入整数"));
			} else {
				callback();
			}
		};
		return {
			id: '',
			type: '',
			
			
			ro:{
				gequmingcheng : false,
				yinlefenlei : false,
				fengmian : false,
				geshou : false,
				zhuanjimingcheng : false,
				faxingriqi : false,
				bofangliang : false,
				goumailiang : false,
				xiaichengdu : false,
				clicktime : false,
				clicknum : false,
				discussnum : false,
				storeupnum : false,
			},
			
			
			ruleForm: {
				gequmingcheng: '',
				yinlefenlei: '',
				fengmian: '',
				geshou: '',
				zhuanjimingcheng: '',
				faxingriqi: '',
				bofangliang: '',
				goumailiang: '',
				xiaichengdu: '',
				clicktime: '',
			},
		
			yinlefenleiOptions: [],

			
			rules: {
				gequmingcheng: [
					{ required: true, message: '歌曲名称不能为空', trigger: 'blur' },
				],
				yinlefenlei: [
					{ required: true, message: '音乐分类不能为空', trigger: 'blur' },
				],
				fengmian: [
				],
				geshou: [
				],
				zhuanjimingcheng: [
				],
				faxingriqi: [
				],
				bofangliang: [
					{ validator: validateIntNumber, trigger: 'blur' },
				],
				goumailiang: [
					{ validator: validateIntNumber, trigger: 'blur' },
				],
				xiaichengdu: [
				],
				clicktime: [
				],
				clicknum: [
					{ validator: validateIntNumber, trigger: 'blur' },
				],
				discussnum: [
					{ validator: validateIntNumber, trigger: 'blur' },
				],
				storeupnum: [
					{ validator: validateIntNumber, trigger: 'blur' },
				],
			}
		};
	},
	props: ["parent"],
	computed: {



	},
    components: {
    },
	created() {
	},
	methods: {
		
		// 下载
		download(file){
			window.open(`${file}`)
		},
		// 初始化
		init(id,type) {
			if (id) {
				this.id = id;
				this.type = type;
			}
			if(this.type=='info'||this.type=='else'){
				this.info(id);
			}else if(this.type=='logistics'){
				this.logistics=false;
				this.info(id);
			}else if(this.type=='cross'){
				var obj = this.$storage.getObj('crossObj');
				for (var o in obj){
						if(o=='gequmingcheng'){
							this.ruleForm.gequmingcheng = obj[o];
							this.ro.gequmingcheng = true;
							continue;
						}
						if(o=='yinlefenlei'){
							this.ruleForm.yinlefenlei = obj[o];
							this.ro.yinlefenlei = true;
							continue;
						}
						if(o=='fengmian'){
							this.ruleForm.fengmian = obj[o];
							this.ro.fengmian = true;
							continue;
						}
						if(o=='geshou'){
							this.ruleForm.geshou = obj[o];
							this.ro.geshou = true;
							continue;
						}
						if(o=='zhuanjimingcheng'){
							this.ruleForm.zhuanjimingcheng = obj[o];
							this.ro.zhuanjimingcheng = true;
							continue;
						}
						if(o=='faxingriqi'){
							this.ruleForm.faxingriqi = obj[o];
							this.ro.faxingriqi = true;
							continue;
						}
						if(o=='bofangliang'){
							this.ruleForm.bofangliang = obj[o];
							this.ro.bofangliang = true;
							continue;
						}
						if(o=='goumailiang'){
							this.ruleForm.goumailiang = obj[o];
							this.ro.goumailiang = true;
							continue;
						}
						if(o=='xiaichengdu'){
							this.ruleForm.xiaichengdu = obj[o];
							this.ro.xiaichengdu = true;
							continue;
						}
						if(o=='clicktime'){
							this.ruleForm.clicktime = obj[o];
							this.ro.clicktime = true;
							continue;
						}
						if(o=='clicknum'){
							this.ruleForm.clicknum = obj[o];
							this.ro.clicknum = true;
							continue;
						}
						if(o=='discussnum'){
							this.ruleForm.discussnum = obj[o];
							this.ro.discussnum = true;
							continue;
						}
						if(o=='storeupnum'){
							this.ruleForm.storeupnum = obj[o];
							this.ro.storeupnum = true;
							continue;
						}
				}
			}
			// 获取用户信息
			this.$http({
				url: `${this.$storage.get('sessionTable')}/session`,
				method: "get"
			}).then(({ data }) => {
				if (data && data.code === 0) {
					var json = data.data;
				} else {
					this.$message.error(data.msg);
				}
			});
            this.$http({
				url: `option/yinlefenlei/yinlefenlei`,
				method: "get"
            }).then(({ data }) => {
				if (data && data.code === 0) {
					this.yinlefenleiOptions = data.data;
				} else {
					this.$message.error(data.msg);
				}
            });
			
		},
    // 多级联动参数

    info(id) {
      this.$http({
        url: `yinlehaibao/info/${id}`,
        method: "get"
      }).then(({ data }) => {
        if (data && data.code === 0) {
        this.ruleForm = data.data;
        //解决前台上传图片后台不显示的问题
        let reg=new RegExp('../../../upload','g')//g代表全部
        } else {
          this.$message.error(data.msg);
        }
      });
    },


    // 提交
    onSubmit() {
	if(this.ruleForm.fengmian!=null) {
		this.ruleForm.fengmian = this.ruleForm.fengmian.replace(new RegExp(this.$base.url,"g"),"");
	}
var objcross = this.$storage.getObj('crossObj');
      //更新跨表属性
       var crossuserid;
       var crossrefid;
       var crossoptnum;
       if(this.type=='cross'){
                var statusColumnName = this.$storage.get('statusColumnName');
                var statusColumnValue = this.$storage.get('statusColumnValue');
                if(statusColumnName!='') {
                        var obj = this.$storage.getObj('crossObj');
                       if(statusColumnName && !statusColumnName.startsWith("[")) {
                               for (var o in obj){
                                 if(o==statusColumnName){
                                   obj[o] = statusColumnValue;
                                 }
                               }
                               var table = this.$storage.get('crossTable');
                             this.$http({
                                 url: `${table}/update`,
                                 method: "post",
                                 data: obj
                               }).then(({ data }) => {});
                       } else {
                               crossuserid=this.$storage.get('userid');
                               crossrefid=obj['id'];
                               crossoptnum=this.$storage.get('statusColumnName');
                               crossoptnum=crossoptnum.replace(/\[/,"").replace(/\]/,"");
                        }
                }
        }
		this.$refs["ruleForm"].validate(valid => {
			if (valid) {
				if(crossrefid && crossuserid) {
					this.ruleForm.crossuserid = crossuserid;
					this.ruleForm.crossrefid = crossrefid;
					let params = { 
						page: 1, 
						limit: 10, 
						crossuserid:this.ruleForm.crossuserid,
						crossrefid:this.ruleForm.crossrefid,
					} 
				this.$http({ 
					url: "yinlehaibao/page", 
					method: "get", 
					params: params 
				}).then(({ 
					data 
				}) => { 
					if (data && data.code === 0) { 
						if(data.data.total>=crossoptnum) {
							this.$message.error(this.$storage.get('tips'));
							return false;
						} else {
							this.$http({
								url: `yinlehaibao/${!this.ruleForm.id ? "save" : "update"}`,
								method: "post",
								data: this.ruleForm
							}).then(({ data }) => {
								if (data && data.code === 0) {
									this.$message({
										message: "操作成功",
										type: "success",
										duration: 1500,
										onClose: () => {
											this.parent.showFlag = true;
											this.parent.addOrUpdateFlag = false;
											this.parent.yinlehaibaoCrossAddOrUpdateFlag = false;
											this.parent.search();
											this.parent.contentStyleChange();
										}
									});
								} else {
									this.$message.error(data.msg);
								}
							});

						}
					} else { 
				} 
			});
		} else {
			this.$http({
				url: `yinlehaibao/${!this.ruleForm.id ? "save" : "update"}`,
				method: "post",
			   data: this.ruleForm
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.$message({
						message: "操作成功",
						type: "success",
						duration: 1500,
						onClose: () => {
							this.parent.showFlag = true;
							this.parent.addOrUpdateFlag = false;
							this.parent.yinlehaibaoCrossAddOrUpdateFlag = false;
							this.parent.search();
							this.parent.contentStyleChange();
						}
					});
				} else {
					this.$message.error(data.msg);
			   }
			});
		 }
         }
		});
    },
    // 获取uuid
    getUUID () {
      return new Date().getTime();
    },
    // 返回
    back() {
      this.parent.showFlag = true;
      this.parent.addOrUpdateFlag = false;
      this.parent.yinlehaibaoCrossAddOrUpdateFlag = false;
      this.parent.contentStyleChange();
    },
    fengmianUploadChange(fileUrls) {
	    this.ruleForm.fengmian = fileUrls;
    },
  }
};
</script>
<style lang="scss" scoped>
	.amap-wrapper {
		width: 100%;
		height: 500px;
	}
	
	.search-box {
		position: absolute;
	}
	
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
	  	  padding: 0 10px 0 0;
	  	  color: #000;
	  	  font-weight: 500;
	  	  width: 180px;
	  	  font-size: 15px;
	  	  line-height: 40px;
	  	  text-align: right;
	  	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
	  margin-left: 180px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
	  	  border: 1px solid rgba(0,0,0,0.3);
	  	  border-radius: 4px;
	  	  padding: 0 12px;
	  	  box-shadow: 0 0 6px rgba(0,0,0,0.3);
	  	  background: #fff;
	  	  width: 400px;
	  	  font-size: 14px;
	  	  height: 40px;
	  	}
	.add-update-preview .el-input-number /deep/ .el-input__inner {
		text-align: left;
	  	  border: 1px solid rgba(0,0,0,0.3);
	  	  border-radius: 4px;
	  	  padding: 0 12px;
	  	  box-shadow: 0 0 6px rgba(0,0,0,0.3);
	  	  background: #fff;
	  	  width: 400px;
	  	  font-size: 14px;
	  	  height: 40px;
	  	}
	.add-update-preview .el-input-number /deep/ .el-input-number__decrease {
		display: none;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__increase {
		display: none;
	}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
	  	  border: 0;
	  	  border-radius: 4px;
	  	  padding: 0 10px;
	  	  box-shadow: 0 0 6px rgba(0,0,0,0.3);
	  	  outline: none;
	  	  color: #000;
	  	  background: #fff;
	  	  width: 200px;
	  	  font-size: 14px;
	  	  height: 40px;
	  	}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
	  	  border: 0;
	  	  border-radius: 4px;
	  	  padding: 0 10px 0 30px;
	  	  box-shadow: 0 0 6px rgba(0,0,0,0.3);
	  	  outline: none;
	  	  background: #fff;
	  	  width: 200px;
	  	  font-size: 14px;
	  	  height: 40px;
	  	}
	
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .upload .upload-img {
	  	  cursor: pointer;
	  	  border-radius: 6px;
	  	  box-shadow: 0 0 6px rgba(0,0,0,0.3);
	  	  background: #fff;
	  	  width: 120px;
	  	  font-size: 32px;
	  	  line-height: 80px;
	  	  text-align: center;
	  	  height: 80px;
	  	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
	  	  cursor: pointer;
	  	  border-radius: 6px;
	  	  box-shadow: 0 0 6px rgba(0,0,0,0.3);
	  	  background: #fff;
	  	  width: 120px;
	  	  font-size: 32px;
	  	  line-height: 80px;
	  	  text-align: center;
	  	  height: 80px;
	  	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
	  	  cursor: pointer;
	  	  border-radius: 6px;
	  	  box-shadow: 0 0 6px rgba(0,0,0,0.3);
	  	  background: #fff;
	  	  width: 120px;
	  	  font-size: 32px;
	  	  line-height: 80px;
	  	  text-align: center;
	  	  height: 80px;
	  	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
	  	  border: 0;
	  	  border-radius: 4px;
	  	  padding: 12px;
	  	  box-shadow: 0 0 6px rgba(0,0,0,0.3);
	  	  outline: none;
	  	  background: #fff;
	  	  width: 400px;
	  	  font-size: 14px;
	  	  height: 120px;
	  	}
	
	.add-update-preview .btn .btn1 {
				border: 1px solid  rgba(0,0,0,0.3);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 24px;
				margin: 4px;
				outline: none;
				color: #fff;
				background:  rgba(0,0,0,0.3);
				width: auto;
				font-size: 14px;
				height: 40px;
			}
	
	.add-update-preview .btn .btn1:hover {
				opacity: 0.8;
			}
	
	.add-update-preview .btn .btn2 {
				border: 1px solid  rgba(0,0,0,0.3);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 24px;
				margin: 4px;
				outline: none;
				color: #fff;
				background:  rgba(0,0,0,0.3);
				width: auto;
				font-size: 14px;
				height: 40px;
			}
	
	.add-update-preview .btn .btn2:hover {
				opacity: 0.8;
			}
	
	.add-update-preview .btn .btn3 {
				border: 1px solid  rgba(0,0,0,0.3);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 24px;
				margin: 4px;
				outline: none;
				color: #fff;
				background:  rgba(0,0,0,0.3);
				width: auto;
				font-size: 14px;
				height: 40px;
			}
	
	.add-update-preview .btn .btn3:hover {
				opacity: 0.8;
			}
	
	.add-update-preview .btn .btn4 {
				border: 1px solid  rgba(0,0,0,0.3);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 24px;
				margin: 4px;
				outline: none;
				color: #fff;
				background:  rgba(0,0,0,0.3);
				width: auto;
				font-size: 14px;
				height: 40px;
			}
	
	.add-update-preview .btn .btn4:hover {
				opacity: 0.8;
			}
	
	.add-update-preview .btn .btn5 {
				border: 1px solid  rgba(0,0,0,0.3);
				cursor: pointer;
				border-radius: 4px;
				padding: 0 24px;
				margin: 4px;
				outline: none;
				color: #fff;
				background:  rgba(0,0,0,0.3);
				width: auto;
				font-size: 14px;
				height: 40px;
			}
	
	.add-update-preview .btn .btn5:hover {
				opacity: 0.8;
			}
</style>
