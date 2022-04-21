<template>
    <div>  
        <BG/>
        <Portrait/>
        <SongList/>
        
    </div>
</template>

<script>
    import Portrait from './components/Portrait.vue'
    import SongList from './components/SongList.vue'
    import BG from './components/bg.vue'
    export default {
        name: 'App',
        components: { Portrait, SongList, BG}
    }
</script>

<style>
    #app {
        font-family: Georgia, Arial, sans-serif;
        margin-left: 40px;
        margin-right: 40px;
    }
</style>