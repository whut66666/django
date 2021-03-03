<template>
  <div id="userlist">
    <div v-for="user in imglist" :key="user.id" class="user">
      <img :src="apiurl+user.headImg" alt />
      <p>{{user.nickName}}</p>
      <button @click="deleteUser(user.id)">删除</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'
export default {
  data() {
    return {
      apiurl:'http://127.0.0.1:9000/upload/',
      imglist:[],
      menuId:1
    }
  },
  mounted() {
    this.getUserList(this.menuId)
  },
  watch:{
    $route(to){
      this.menuId = to.query.menuId
      this.getUserList(this.menuId)
    }
  },
  methods:{
    // 从这里开始进行后端的请求
    getUserList(id){
      console.log('开始获取分类用户列表'+id);
      axios({
        url:'http://127.0.0.1:9000/get-user-list/',
        type:'json',
        params:{
          // id:id
          id
        },
        method:'get'
      }).then((res)=>{
        console.log(res.data);
        this.imglist = res.data
      })
    },
    // 删除用户
    deleteUser(id) {
      console.log(id);
      axios({
        url:'http://127.0.0.1:9000/get-user-list/',
        type:'json',
        data: Qs.stringify({
          id
        }),
        // method:'delete',
        method:'post',
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
      }).then((res)=>{
        console.log(res);
        if(res.data=='ok'){
          this.getUserList(this.menuId)
        }
      })
    },
  }
};
</script>

<style scoped>
</style>