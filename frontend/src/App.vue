<template>
    <div>
        <BG/>
        <div class = "flex__container">  
            <Portrait/>       
        </div>
        <div class = "body_container">  
            <SongList/>
        </div>
    </div>
</template>

<script>
    import Portrait from './components/Portrait'
    import SongList from './components/SongList'
    import BG from './components/bg'
    export default {
        name: 'App',
        components: { Portrait, SongList, BG}
    }
</script>

<style>
    #app {
        font-family: Georgia, Arial, sans-serif;
        margin-left: 60px;
        margin-right: 60px;
    }
    .flex__container {
        justify-content: center;

        align-items: center;

        width: 100%;

        top: 25%;

        left:5%;
    }

    .body_container{
        /* display: flex; */

        justify-content: center;

        align-items: center;

        width: 80%;

        position: absolute;

        top: 75%;

        transform: translate(12%, -50%);
    }
</style>