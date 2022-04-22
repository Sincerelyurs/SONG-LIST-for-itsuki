<template>
      <el-row class="flex__container">
    <el-col :span="12">
      <div class="demo-basic--circle">
        <div class="block"><el-avatar :size="300" :src="circleUrl"></el-avatar></div>
      </div>
    </el-col> 
  </el-row>

  
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
    .flex__container {
    display: flex;

    position: absolute;

    transform: translate(12%, -50%);

    justify-content: center;

    align-items: center;

    width: 100%;
    }
</style>