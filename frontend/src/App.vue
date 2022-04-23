<template>
    <div>
        <BG/>
        <div class = "box1">  
            <Portrait/>       
        </div>

        <div class = "box2">
            <Infomation/>
        </div>

        <div class = "box3">  
            <SongList/>
        </div>
    </div>
</template>

<script>
    import Portrait from './components/Portrait'
    import SongList from './components/SongList'
    import BG from './components/bg'
    import Infomation from './components/infomation'
    export default {
        name: 'App',
        components: { Portrait, SongList, BG, Infomation }
    }
</script>

<style>
    /* #app {
        font-family: Georgia, Arial, sans-serif;
        margin-left: 60px;
        margin-right: 60px;
    } */
    .box1 {
        margin:0 auto;
    }

    .box2 {
        margin:0 auto;
        width: 60%;
    }

    .box3{
        /* display: flex; */
        margin:0 auto;
        width: 60%;
    }
</style>