<template>
  <div>
    <div v-for="song in info" v-bind:key="song.Song_ID" id="articles">
          <div class="article-title">
              {{ song.Song_Name }}
          </div>
    </div>
  </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'App',
        data: function () {
            return {
                info: '',
            }
        },
        mounted() {
            axios
                .get('/api/song')
                .then(response => (this.info = response.data))
        },
    }
</script>

<style>
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