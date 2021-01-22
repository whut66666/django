<template>
  <div id="home">
    <div>
      <button v-if="loginType == false" @click="tologin(1)">登录</button>
      <button v-if="loginType == false" @click="tologin(2)">注册</button>
      <button v-if="loginType == true">个人中心</button>
      <button v-if="loginType == true" @click="tologin(3)">修改</button>
      <div class="header">
        <h1>{{siteinfo.sitename}}</h1>
        <img :src="siteinfo.logo" alt="" />
      </div>
      <hr />
      <div class="content">
        <div class="menu">
          <div v-for="item in menuList" :key="item.id" class="item">
            <div
              v-if="item.id == choosed"
              style="background: #777; color: #fff"
            >
              <a to="/" style="color: #fff">{{
                item.text
              }}</a>
            </div>
            <div v-else @click="chooseMenu(item.id)">
              <a to="/" style="color: #000">{{
                item.text
              }}</a>
            </div>
          </div>
        </div>
        <div class="userlist">
          <p>{{choosed_text}}</p>
          <hr />
          <router-view />
        </div>
      </div>
      <hr />
    </div>
    <LoginBox v-if="boxtarget" :target="boxtarget" @hidelogin="hidelogin"></LoginBox>
    <div class="foot">Copyright © 2020 Li Junchao</div>
  </div>
</template>

<script>
import axios from "axios";
import LoginBox from "../src/components/LoginBox"
export default {
  components:{
    LoginBox
  },
  data() {
    return {
      menuList: [],
      choosed: 1,
      choosed_text:'Django后端',
      boxtarget:0,
      siteinfo:{},
      loginType:false
    };
  },
  mounted() {
    try{
      if(window.localStorage.getItem('token').length>0){
      this.loginType = true
    }
    } catch(error) {
      console.log(error);
    }
    
    this.getMenuList();
  },
  methods: {
    getMenuList() {
      console.log("开始获取分类");
      axios({
        url: "http://127.0.0.1:9000/get-menu-list/",
        type: "json",
        method: "get",
      }).then((res) => {
        this.menuList = res.data.menu_data;
        this.siteinfo = res.data.siteinfo
        console.log(this.menuList);
      });
    },
    chooseMenu(id) {
      this.choosed = id;
      for (let index = 0; index < this.menuList.length; index++) {
        if(id == this.menuList[index].id){
          this.choosed_text = this.menuList[index].text;
        }
      }
      // 进行路由传参跳转
      this.$router.push({path:'/',query:{menuId:id}})
    },
    // 用来展示登录框
    tologin(value) {
      this.boxtarget = value;
    },
    // 用来隐藏登录组件
    hidelogin(){
      this.boxtarget = 0;
    }
  },
};
</script>

<style>
</style>
