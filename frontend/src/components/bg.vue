<template>
    <div class="loginbg">
        <img src="../assets/3.png">
        <img src="../assets/3.png">
        <img src="../assets/3.png">
        <img src="../assets/3.png">
        <img src="../assets/3.png">
        <img src="../assets/3.png">
    </div>
</template>

<script>
 export default {
        name: 'BG',
    }

</script>

<style>
    .loginbg{
        width: 100%;
        height:12000px;         /* 背景图片高度 */
        overflow: hidden;
        position: absolute;
        top: 0;
        z-index: -1;
    }
    .loginbg img{
        width: 100%;
    }

</style>