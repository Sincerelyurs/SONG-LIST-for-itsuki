<template>
    <div>
        <BG/>
        <Header/>
        <div class = "box1">  
            <Portrait/>       
        </div>

        <div class = "box2">  
            <Button/>       
        </div>
        
        <div class = "box2">
            <Infomation/>
        </div>

        <div class = "box3">  
            <SongList/>
        </div>

         <div class = "box4">  
            <Footer/>
        </div>
    </div>
</template>

<script>
    import Portrait from './components/Portrait'
    import SongList from './components/SongList'
    import BG from './components/bg'
    import Infomation from './components/infomation'
    import Footer from './components/Footer'
    import Header from './components/Header'
    import Button from './components/Button'
    export default {
        name: 'App',
        components: { Portrait, SongList, BG, Infomation, Footer, Header, Button }
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
        display: flex;
        margin:0 auto;
        width: 60%;
    }

    .box3{
        /* display: flex; */
        margin:0 auto;
        width: 60%;
    }
    .box4{
        /* display: flex; */
        margin:0 auto;
        width: 60%;
    }
</style>