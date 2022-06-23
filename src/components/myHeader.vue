<template>
  <div id="header">
    <el-row>
      <el-col :span="6"
        ><div class="grid-content bg-purple">
          <el-button
            type="primary"
            icon="el-icon-video-camera-solid"
            id="button1"
            @click="register"
            >直播间</el-button
          >
        </div></el-col
      >
      <el-col :span="12"
        ><div class="grid-content bg-purple"><h1 id = "head">小树的歌单</h1></div></el-col
      >
      <el-col :span="6"
        ><div class="grid-content bg-purple">
          <el-button
            @click="drawer = true"
            type="primary"
            icon="el-icon-s-order"
            id="button1"
          >
            待学
          </el-button>
        </div></el-col
      >
    </el-row>
    <el-drawer title="我是标题" :visible.sync="drawer" :with-header="false">
      <span>待学歌单</span>
    </el-drawer>
    <hr />
  </div>
</template>

<script>
export default {
  name: "slheader",
  data() {
    return {
      drawer: false,
    };
  },
  methods: {
    register() {
      window.open("https://live.bilibili.com/790566", "_blank");
    },
  },
};
</script>

<style scoped>
#header {
  text-align: center;
  margin-top: 10px;
}
#button1 {
  text-align: left;
}
#head {
  font-size: 1rem;
}
</style>