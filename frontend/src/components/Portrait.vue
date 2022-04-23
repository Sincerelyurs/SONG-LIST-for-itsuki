<template>
  <div class="box1">
    <br/><br/>
    <el-avatar :size="300" :src="circleUrl"></el-avatar>
  </div>
</template>
<script>
  export default {
    name: 'Portrait',
    data () {
      return {
        circleUrl: 'https://5fou.com/i/2022/04/21/12ctwkc.png',
      }
    }
  }
</script>

<style scoped>
    .demo-basic--circle {
      margin: 0 auto;
    }
    .box1 {
      height: 300px;
      width: 300px;
      margin: 0 auto;
    }

</style>