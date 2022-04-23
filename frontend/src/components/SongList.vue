<template>
  <div>
    <el-row>
    <el-col :span="4"><div class="grid-content bg-purple"><el-button type="primary" plain @click="OnClick(0)" style="width:100%;background: #ffccff;">全部</el-button></div></el-col>
    <el-col :span="4"><div class="grid-content bg-purple"><el-button type="primary" plain @click="OnClick(1)" style="width:100%;background: #99ffcc;">国语</el-button></div></el-col>
    <el-col :span="4"><div class="grid-content bg-purple"><el-button type="primary" plain @click="OnClick(2)" style="width:100%;background: #66ffff;">英语</el-button></div></el-col>
    <el-col :span="4"><div class="grid-content bg-purple"><el-button type="primary" plain @click="OnClick(3)" style="width:100%;background: #00FA9A;">日语</el-button></div></el-col>
    <el-col :span="4"><div class="grid-content bg-purple"><el-button type="primary" plain @click="OnClick(4)" style="width:100%;background: #ffff99;">粤语</el-button></div></el-col>
    <el-col :span="4"><div class="grid-content bg-purple-light"><el-select v-model="value" clearable placeholder="请选择歌曲首字母" style="width:100%;"><el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"></el-option></el-select></div></el-col>
    </el-row>
    <el-input type = "test" v-model="keyword" placeholder="请输入歌名或歌手名"></el-input>
    <el-divider></el-divider>
    <el-table :data="searchList" :header-cell-style="{ background: '#0e192a', color: '#6666EE' }" :row-style="{ background: '#D9EFCB' }" @row-click="handle">
        <el-table-column prop="Song_Name" label="歌名" width="300px"></el-table-column>
        <el-table-column prop="Singer" label="歌手" width="240px"></el-table-column>
        <el-table-column prop="Language" label="语言"></el-table-column>
        <el-table-column prop="Remark" label="备注"></el-table-column>   
    </el-table>
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
                searchType:0,
                message: 'copy me',
                options: [
                    { value: 1, label: '全部'}, 
                    { value: 2, label: 'A'},
                    { value: 3, label: 'B'},
                    { value: 4, label: 'C'},
                    { value: 5, label: 'D'},
                    { value: 6, label: 'E'},
                    { value: 7, label: 'F'},
                    { value: 8, label: 'G'},
                    { value: 9, label: 'H'},
                    { value: 10, label: 'I'},
                    { value: 11, label: 'J'},
                    { value: 12, label: 'K'},
                    { value: 13, label: 'L'},
                    { value: 14, label: 'M'},
                    { value: 15, label: 'N'},
                    { value: 16, label: 'O'},
                    { value: 17, label: 'P'},
                    { value: 18, label: 'Q'},
                    { value: 19, label: 'R'},
                    { value: 20, label: 'S'},
                    { value: 21, label: 'T'},
                    { value: 22, label: 'U'},
                    { value: 23, label: 'V'},
                    { value: 24, label: 'W'},
                    { value: 25, label: 'X'},
                    { value: 26, label: 'Y'},
                    { value: 27, label: 'Z'},
                    { value: 28, label: '其他语言'},                     
                    ],
                    value: ''
                        }
                },
        mounted() {
            axios
                .get('/api/song')
                .then(response => (this.info = response.data, this.searchList = response.data))
        },
        watch:{
            keyword:{           
                handler(val){
                    this.searchList = this.info.filter((p)=>{
                    return p.Song_Name.indexOf(val) != -1 || p.Singer.indexOf(val) != -1})
                },
                immediate: true,
            },
            value:{
                handler(val){
                    if(val === 1){
                        this.searchList = this.info
                    }
                    else if(val === 2){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '1'})
                    }
                    else if(val === 3){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '2'})
                    }
                    else if(val === 4){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '3'})
                    }
                    else if(val === 5){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '4'})
                    }
                    else if(val === 6){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '5'})
                    }
                    else if(val === 7){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '6'})
                    }
                    else if(val === 8){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '7'})
                    }
                    else if(val === 9){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '8'})
                    }
                    else if(val === 10){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '9'})
                    }
                    else if(val === 11){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '10'})
                    }
                    else if(val === 12){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '11'})
                    }
                    else if(val === 13){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '12'})
                    }
                    else if(val === 14){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '13'})
                    }
                    else if(val === 15){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '14'})
                    }
                    else if(val === 16){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '15'})
                    }
                    else if(val === 17){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '16'})
                    }
                    else if(val === 18){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '17'})
                    }
                    else if(val === 19){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '18'})
                    }
                    else if(val === 20){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '19'})
                    }
                    else if(val === 21){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '20'})
                    }
                    else if(val === 22){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '21'})
                    }
                    else if(val === 23){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '22'})
                    }
                    else if(val === 24){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '23'})
                    }
                    else if(val === 25){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '24'})
                    }
                    else if(val === 26){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '25'})
                    }
                    else if(val === 27){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '26'})
                    }
                    else if(val === 28){
                        this.searchList = this.info.filter((p)=>{
                        return p.Initial == '27'})
                    }
                    else{
                        this.searchList = this.info
                    }
                }
            }
        },
        methods:{
            OnClick(num){
                if(num === 1){
                    axios
                    .get('/api/song/?search=国语')
                    .then(response => (this.info = response.data, this.searchList = response.data))
                }
                else if(num === 2){
                    axios
                    .get('/api/song/?search=英语')
                    .then(response => (this.info = response.data, this.searchList = response.data))
                }
                else if(num === 3){
                    axios
                    .get('/api/song/?search=日语')
                    .then(response => (this.info = response.data, this.searchList = response.data))
                }
                else if(num === 4){
                    axios
                    .get('/api/song/?search=粤语')
                    .then(response => (this.info = response.data, this.searchList = response.data))
                }
                else{
                    axios
                    .get('/api/song')
                    .then(response => (this.info = response.data, this.searchList = response.data))
                }
            },
            handle(row, event, column){
                this.message = "点歌 " + row.Song_Name
                this.$copyText(this.message)
                console.log(this.message)
                const h = this.$createElement;
                this.$notify({
                title: '复制成功',
                message: h('i', { style: 'color: teal'}, '成功复制' + "“" + row.Song_Name + "”" + '到剪切板，快戴上五级牌子到直播间点歌吧！')
                });
            },
            OnSelect(val){
                if(val == '选项1'){
                    console.log("yes")
                    this.searchList = this.info.filter((p)=>{
                    return p.Initial.indexOf(1) != -1})
                }
                else{
                    console.log("no")
                }

            },
        }

    }
</script>

<style lang="scss" scoped>
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
    .el-button{
        background: #535355;
        border-color: #9c9df1;
        color: #fff;
    }
</style>