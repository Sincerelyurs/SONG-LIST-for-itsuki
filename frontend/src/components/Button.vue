<template>
    <div class="butt">
        <br><br><br><br>
        <div class="butt">
            <el-button type="primary" plain @click="register">前往小树直播间</el-button><br/><br/>
        </div>  
    </div>
    
</template>

<script>
 export default {
        name: 'Button',
        methods:{
            register () {
                window.open('https://live.bilibili.com/790566', '_blank')
            }
        }
    }
</script>

<style>
    .butt{
         margin:0 auto;
    }
</style>