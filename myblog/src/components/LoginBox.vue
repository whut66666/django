<template>
  <div id="login" @click.self="hideSelf">
    <div id="loginbox">
      <div class="form">
        <div v-if="target==1 || target==2" class="item">
          <div class="span">用户名:</div>
          <input v-model="username" type="text" placeholder="输入用户名" />
        </div>
        <div v-if="target==1 || target==2" class="item">
          <div  class="span">密码:</div>
          <input v-model="password" type="password" placeholder="输入密码" />
        </div>
        <div v-if="target == 2" class="item">
          <div class="span">重复密码:</div>
          <input v-model="password2" type="password" placeholder="再次输入密码"/>
        </div>

        <div v-if="target==3" class="item">
          <div class="span">网站名称:</div>
          <input v-model="sitename" type="text" placeholder="输入网站名称" />
        </div>

        <div v-if="target==3" class="item">
          <div class="span">图片上传:</div>
          <input id="uploadLogo" type="file"  style="width:70px" />
        </div>

        <button v-if="target == 1" @click="toLogin">登录</button>
        <button v-if="target == 2" @click="toRegister">注册</button>
        <button v-if="target == 3" @click="toLoad">确定</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";
export default {
  name: "LoginBox",
  props: ["target"],
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      sitename:""
    };
  },
  mounted() {
    console.log(this.target);
  },
  methods: {
    // 隐藏登录注册组件
    hideSelf() {
      this.$emit("hidelogin");
    },
    // 注册
    toRegister() {
      if (
        this.username.length > 0 &&
        this.password.length > 0 &&
        this.password2.length > 0
      ) {
        if (this.password != this.password2) {
          alert("两次密码输入不一致");
        } else {
          axios({
            url: "http://127.0.0.1:9000/register/",
            data: Qs.stringify({
              username: this.username,
              password: this.password,
              password2: this.password2,
            }),
            method: "post",
          }).then((res) => {
            console.log(res);
            switch (res.data) {
                case 'same':
                    alert('该用户名已存在')
                    break;
            }
          });
        }
      }else{
          alert('缺少必填项')
      }
    },
    // 登录
    toLogin() {
      console.log(this.username, this.password);
      if (this.username.length > 0 && this.password.length > 0) {
        axios({
          url: "http://127.0.0.1:9000/login/",
          data: Qs.stringify({
            username: this.username,
            password: this.password,
          }),
          method: "post",
        }).then((res) => {
          console.log(res);
          switch (res.data) {
            case "nouser":
              alert("没有该用户名");
              break;
            case "pwderr":
              alert("密码错误");
              break;
            default:
              console.log(res.data.token);
              alert("登陆成功");
          }
        });
      } else {
        alert("用户名和密码不能为空！");
      }
    },
    toLoad(){
        
    }
  },
};
</script>

<style>
#login {
  position: absolute;
  top: 0;
  width: 700px;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #00000020;
}
#loginbox {
  width: 300px;
  height: 300px;
  border: 1px solid #000;
  margin: 0 auto;
  background: #00000090;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
}
#loginbox .form .item {
  font-weight: 500;
  margin: 10px auto;
}
#loginbox .form .item .span {
  float: left;
  width: 80px;
}
</style>