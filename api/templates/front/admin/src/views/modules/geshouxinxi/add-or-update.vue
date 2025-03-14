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
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="歌手姓名" prop="geshouxingming">
					<el-input v-model="ruleForm.geshouxingming" placeholder="歌手姓名" clearable  :readonly="ro.geshouxingming"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else class="input" label="歌手姓名" prop="geshouxingming">
					<el-input v-model="ruleForm.geshouxingming" placeholder="歌手姓名" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="select" v-if="type!='info'"  label="歌手性别" prop="geshouxingbie">
					<el-select :disabled="ro.geshouxingbie" v-model="ruleForm.geshouxingbie" placeholder="请选择歌手性别" >
						<el-option
							v-for="(item,index) in geshouxingbieOptions"
							v-bind:key="index"
							:label="item"
							:value="item">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else class="input" label="歌手性别" prop="geshouxingbie">
					<el-input v-model="ruleForm.geshouxingbie"
						placeholder="歌手性别" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="流派" prop="liupai">
					<el-input v-model="ruleForm.liupai" placeholder="流派" clearable  :readonly="ro.liupai"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else class="input" label="流派" prop="liupai">
					<el-input v-model="ruleForm.liupai" placeholder="流派" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="标签" prop="biaoqian">
					<el-input v-model="ruleForm.biaoqian" placeholder="标签" clearable  :readonly="ro.biaoqian"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else class="input" label="标签" prop="biaoqian">
					<el-input v-model="ruleForm.biaoqian" placeholder="标签" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="date" v-if="type!='info'" label="出道日期" prop="chudaoriqi">
					<el-date-picker
						format="yyyy 年 MM 月 dd 日"
						value-format="yyyy-MM-dd"
						v-model="ruleForm.chudaoriqi" 
						type="date"
						:readonly="ro.chudaoriqi"
						placeholder="出道日期"
					></el-date-picker> 
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="input" v-else-if="ruleForm.chudaoriqi" label="出道日期" prop="chudaoriqi">
					<el-input v-model="ruleForm.chudaoriqi" placeholder="出道日期" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="成名歌曲" prop="chengminggequ">
					<el-input v-model="ruleForm.chengminggequ" placeholder="成名歌曲" clearable  :readonly="ro.chengminggequ"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else class="input" label="成名歌曲" prop="chengminggequ">
					<el-input v-model="ruleForm.chengminggequ" placeholder="成名歌曲" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="upload" v-if="type!='info' && !ro.touxiang" label="头像" prop="touxiang">
					<file-upload
						tip="点击上传头像"
						action="file/upload"
						:limit="3"
						:multiple="true"
						:fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
						@change="touxiangUploadChange"
					></file-upload>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="upload" v-else-if="ruleForm.touxiang" label="头像" prop="touxiang">
					<img v-if="ruleForm.touxiang.substring(0,4)=='http'" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.touxiang.split(',')[0]" width="100" height="100">
					<img v-else class="upload-img" style="margin-right:20px;" v-bind:key="index" v-for="(item,index) in ruleForm.touxiang.split(',')" :src="$base.url+item" width="100" height="100">
				</el-form-item>
			</template>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="textarea" v-if="type!='info'" label="热门歌曲" prop="remengequ">
					<el-input
					  style="min-width: 200px; max-width: 600px;"
					  type="textarea"
					  :rows="8"
					  placeholder="热门歌曲"
					  v-model="ruleForm.remengequ" >
					</el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else-if="ruleForm.remengequ" label="热门歌曲" prop="remengequ">
					<span :style='{"border":"1px solid rgba(0,0,0,0.3)","padding":"0 10px","boxShadow":"0 0 6px rgba(0,0,0,0.3)","borderRadius":"4px","color":"#333","background":"#fff","display":"inline-block","fontSize":"14px","lineHeight":"40px","fontWeight":"500"}'>{{ruleForm.remengequ}}</span>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' class="textarea" v-if="type!='info'" label="专辑介绍" prop="zhuanjijieshao">
					<el-input
					  style="min-width: 200px; max-width: 600px;"
					  type="textarea"
					  :rows="8"
					  placeholder="专辑介绍"
					  v-model="ruleForm.zhuanjijieshao" >
					</el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else-if="ruleForm.zhuanjijieshao" label="专辑介绍" prop="zhuanjijieshao">
					<span :style='{"border":"1px solid rgba(0,0,0,0.3)","padding":"0 10px","boxShadow":"0 0 6px rgba(0,0,0,0.3)","borderRadius":"4px","color":"#333","background":"#fff","display":"inline-block","fontSize":"14px","lineHeight":"40px","fontWeight":"500"}'>{{ruleForm.zhuanjijieshao}}</span>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-if="type!='info'"  label="歌手介绍" prop="geshoujieshao">
					<editor 
						style="min-width: 200px; max-width: 600px;"
						v-model="ruleForm.geshoujieshao" 
						class="editor" 
						action="file/upload">
					</editor>
				</el-form-item>
				<el-form-item :style='{"width":"49%","margin":"0 0 20px 0"}' v-else-if="ruleForm.geshoujieshao" label="歌手介绍" prop="geshoujieshao">
                    <span :style='{"border":"1px solid rgba(0,0,0,0.3)","padding":"0 10px","boxShadow":"0 0 6px rgba(0,0,0,0.3)","borderRadius":"4px","color":"#333","background":"#fff","display":"inline-block","fontSize":"14px","lineHeight":"40px","fontWeight":"500"}' v-html="ruleForm.geshoujieshao"></span>
                </el-form-item>
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
				geshouxingming : false,
				geshouxingbie : false,
				liupai : false,
				biaoqian : false,
				chudaoriqi : false,
				chengminggequ : false,
				touxiang : false,
				remengequ : false,
				zhuanjijieshao : false,
				geshoujieshao : false,
				thumbsupnum : false,
				crazilynum : false,
				discussnum : false,
				storeupnum : false,
			},
			
			
			ruleForm: {
				geshouxingming: '',
				geshouxingbie: '',
				liupai: '',
				biaoqian: '',
				chudaoriqi: '',
				chengminggequ: '',
				touxiang: '',
				remengequ: '',
				zhuanjijieshao: '',
				geshoujieshao: '',
			},
		
			geshouxingbieOptions: [],

			
			rules: {
				geshouxingming: [
					{ required: true, message: '歌手姓名不能为空', trigger: 'blur' },
				],
				geshouxingbie: [
					{ required: true, message: '歌手性别不能为空', trigger: 'blur' },
				],
				liupai: [
				],
				biaoqian: [
				],
				chudaoriqi: [
				],
				chengminggequ: [
				],
				touxiang: [
				],
				remengequ: [
				],
				zhuanjijieshao: [
				],
				geshoujieshao: [
				],
				thumbsupnum: [
					{ validator: validateIntNumber, trigger: 'blur' },
				],
				crazilynum: [
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
						if(o=='geshouxingming'){
							this.ruleForm.geshouxingming = obj[o];
							this.ro.geshouxingming = true;
							continue;
						}
						if(o=='geshouxingbie'){
							this.ruleForm.geshouxingbie = obj[o];
							this.ro.geshouxingbie = true;
							continue;
						}
						if(o=='liupai'){
							this.ruleForm.liupai = obj[o];
							this.ro.liupai = true;
							continue;
						}
						if(o=='biaoqian'){
							this.ruleForm.biaoqian = obj[o];
							this.ro.biaoqian = true;
							continue;
						}
						if(o=='chudaoriqi'){
							this.ruleForm.chudaoriqi = obj[o];
							this.ro.chudaoriqi = true;
							continue;
						}
						if(o=='chengminggequ'){
							this.ruleForm.chengminggequ = obj[o];
							this.ro.chengminggequ = true;
							continue;
						}
						if(o=='touxiang'){
							this.ruleForm.touxiang = obj[o];
							this.ro.touxiang = true;
							continue;
						}
						if(o=='remengequ'){
							this.ruleForm.remengequ = obj[o];
							this.ro.remengequ = true;
							continue;
						}
						if(o=='zhuanjijieshao'){
							this.ruleForm.zhuanjijieshao = obj[o];
							this.ro.zhuanjijieshao = true;
							continue;
						}
						if(o=='geshoujieshao'){
							this.ruleForm.geshoujieshao = obj[o];
							this.ro.geshoujieshao = true;
							continue;
						}
						if(o=='thumbsupnum'){
							this.ruleForm.thumbsupnum = obj[o];
							this.ro.thumbsupnum = true;
							continue;
						}
						if(o=='crazilynum'){
							this.ruleForm.crazilynum = obj[o];
							this.ro.crazilynum = true;
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
            this.geshouxingbieOptions = "男,女".split(',')
			
		},
    // 多级联动参数

    info(id) {
      this.$http({
        url: `geshouxinxi/info/${id}`,
        method: "get"
      }).then(({ data }) => {
        if (data && data.code === 0) {
        this.ruleForm = data.data;
        //解决前台上传图片后台不显示的问题
        let reg=new RegExp('../../../upload','g')//g代表全部
        this.ruleForm.geshoujieshao = this.ruleForm.geshoujieshao.replace(reg,'../../../python1p21sd8o/upload');
        } else {
          this.$message.error(data.msg);
        }
      });
    },


    // 提交
    onSubmit() {
	if(this.ruleForm.touxiang!=null) {
		this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
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
					url: "geshouxinxi/page", 
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
								url: `geshouxinxi/${!this.ruleForm.id ? "save" : "update"}`,
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
											this.parent.geshouxinxiCrossAddOrUpdateFlag = false;
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
				url: `geshouxinxi/${!this.ruleForm.id ? "save" : "update"}`,
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
							this.parent.geshouxinxiCrossAddOrUpdateFlag = false;
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
      this.parent.geshouxinxiCrossAddOrUpdateFlag = false;
      this.parent.contentStyleChange();
    },
    touxiangUploadChange(fileUrls) {
	    this.ruleForm.touxiang = fileUrls;
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
