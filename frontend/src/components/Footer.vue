<template>
    <!--  br 标签给页脚留出位置  -->
    <div id="footer">
        <p>Copyright © 2022 🌲树喵窝🌲</p>
    </div>
</template>

<script>
    export default {
        name: 'Footer'
    }
</script>

<style scoped>
    #footer {
        position: fixed;
        left: 0;
        bottom: 0;
        height: 50px;
        width: 100%;
        background: whitesmoke;
        text-align: center;
        font-weight: bold;
    }
</style>