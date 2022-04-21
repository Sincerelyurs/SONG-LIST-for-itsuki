<template>
  <div>
    <el-input type = "test" v-model="keyword" placeholder="请输入内容"></el-input>
    <div v-for="song in searchList" v-bind:key="song.Song_ID" id="articles">
          <div class="article-title">
              {{ song.Song_Name }}
          </div>
    </div>
  </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'SongList',
        data: function () {
            return {
                info: '',
                keyword:'',
                searchList:[],
            }
        },
        mounted() {
            axios
                .get('/api/song')
                .then(response => (this.info = response.data, this.searchList = response.data))
        },
        watch:{
            keyword:{
                immediate: true,
                handler(val){
                    this.searchList = this.info.filter((p)=>{
                    return p.Song_Name.indexOf(val) != -1})
                }
            }
        }
        // get_article_data: function () {
        //     let url = '/api/song';
        //     const page = Number(this.$route.query.page);
        //     if (!isNaN(page) && (page !== 0)) {
        //         url = url + '/?page=' + page;
        //     }
        //     axios
        //         .get(url)
        //         .then(response => (this.info = response.data))
}

</script>

<style scoped>
    #articles {
        padding: 10px;
    }

    .article-title {
        font-size: large;
        font-weight: bolder;
        color: black;
        text-decoration: none;
        padding: 5px 0 5px 0;
    }
</style>