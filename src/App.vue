<template style="margin: 0 0;">
  <div id="page">
    <el-container>
      <slheader />
      <!-- <el-header id="header"><h1>小树的歌单</h1></el-header> -->
      <el-main>
        <div id="avatar" style="height: 200px; width: 200px; margin: 0 auto">
          <el-avatar
            :size="200"
            :src="circleUrl"
            style="margin: 0 auto"
          ></el-avatar>
        </div>
        <el-divider content-position="center">挑个喜欢的类型吧~</el-divider>
        <div id="div0">
          <div>
            <el-button type="primary" id="b1" @click="OnClick(0)"
              >全部</el-button
            >
          </div>
          <div>
            <el-button type="primary" id="b1" @click="OnClick(1)"
              >国语</el-button
            >
          </div>
          <div>
            <el-button type="primary" id="b1" @click="OnClick(2)"
              >英语</el-button
            >
          </div>
          <div>
            <el-button type="primary" id="b1" @click="OnClick(3)"
              >粤语</el-button
            >
          </div>
          <div>
            <el-button type="primary" id="b1" @click="OnClick(4)"
              >日语</el-button
            >
          </div>
          <div>
            <el-button type="primary" id="b1" @click="OnClick(5)"
              >闽语</el-button
            >
          </div>
        </div>
        <el-row>
          <el-col :span="16"
            ><div class="grid-content bg-purple">
              <el-input
                placeholder="请输入歌名或歌手"
                prefix-icon="el-icon-search"
                v-model="keyword"
                clearable
              >
              </el-input></div
          ></el-col>
          <el-col :span="8"
            ><div class="grid-content bg-purple-light">
              <el-select
                v-model="value"
                clearable
                placeholder="首字母"
                style="width: 100%"
                ><el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                  style="width: 100%"
                ></el-option
              ></el-select></div
          ></el-col>
        </el-row>
        <el-table
          :data="searchList"
          :header-cell-style="{ background: '#0e192a', color: '#6666EE' }"
          :row-style="{ background: '#D9EFCB' }"
          @row-click="handle"
          :default-sort="{ prop: 'initial', order: 'ascending' }"
        >
          <el-table-column
            prop="initial"
            label="首字母"
            sortable
            width="100px"
          ></el-table-column>
          <el-table-column
            prop="songName"
            label="歌名"
            width="300px"
          ></el-table-column>
          <el-table-column
            prop="singer"
            label="歌手"
            width="240px"
          ></el-table-column>
          <el-table-column prop="language" label="语言"></el-table-column>
          <el-table-column prop="remark" label="备注"></el-table-column>
        </el-table>
      </el-main>
      <el-footer id="footer">Copyright © 2022 🌲树喵窝🌲</el-footer>
    </el-container>
  </div>
</template>

<script>
import slheader from "./components/myHeader.vue";
import slfooter from "./components/myFooter.vue";

export default {
  name: "App",
  components: { slheader, slfooter },
  data() {
    return {
      circleUrl: "https://s3.bmp.ovh/imgs/2022/05/18/1dd3c6637527dd35.png",
      keyword: "",
      searchList: [],
      message: "copy me",
      totalList: [
        {
          songID: 1,
          songName: "阿楚姑娘",
          singer: "梁凡",
          language: "国语",
          initial: "A",
          remark: "",
        },
        {
          songID: 3,
          songName: "雪落下的声音",
          singer: "陆虎",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 5,
          songName: "One Last Kiss",
          singer: "宇多田光",
          language: "日语",
          initial: "O",
          remark: "",
        },
        {
          songID: 6,
          songName: "爱你",
          singer: "王心凌",
          language: "国语",
          initial: "A",
          remark: "",
        },
        {
          songID: 7,
          songName: "爱",
          singer: "莫文蔚",
          language: "国语",
          initial: "A",
          remark: "",
        },
        {
          songID: 8,
          songName: "爱如潮水",
          singer: "张信哲",
          language: "国语",
          initial: "O",
          remark: "",
        },
        {
          songID: 9,
          songName: "爱就一个字",
          singer: "张信哲",
          language: "国语",
          initial: "A",
          remark: "",
        },
        {
          songID: 10,
          songName: "暧昧",
          singer: "杨丞琳",
          language: "国语",
          initial: "A",
          remark: "",
        },
        {
          songID: 11,
          songName: "宝贝",
          singer: "张悬",
          language: "国语",
          initial: "B",
          remark: "",
        },
        {
          songID: 12,
          songName: "不难",
          singer: "徐佳莹",
          language: "国语",
          initial: "B",
          remark: "",
        },
        {
          songID: 13,
          songName: "不痛",
          singer: "张韶涵",
          language: "国语",
          initial: "B",
          remark: "",
        },
        {
          songID: 14,
          songName: "不够成熟",
          singer: "BY2",
          language: "国语",
          initial: "B",
          remark: "",
        },
        {
          songID: 15,
          songName: "半句再见",
          singer: "孙燕姿",
          language: "国语",
          initial: "B",
          remark: "",
        },
        {
          songID: 16,
          songName: "别找我麻烦",
          singer: "蔡健雅",
          language: "国语",
          initial: "B",
          remark: "",
        },
        {
          songID: 17,
          songName: "别再为他流泪",
          singer: "梁静茹",
          language: "国语",
          initial: "B",
          remark: "",
        },
        {
          songID: 18,
          songName: "不潮不用花钱",
          singer: "林俊杰",
          language: "国语",
          initial: "B",
          remark: "",
        },
        {
          songID: 19,
          songName: "不为谁而作的歌",
          singer: "林俊杰",
          language: "国语",
          initial: "B",
          remark: "",
        },
        {
          songID: 20,
          songName: "传奇",
          singer: "王菲",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 22,
          songName: "纯白",
          singer: "V.K克&双笙",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 23,
          songName: "参商",
          singer: "不才",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 24,
          songName: "崇拜",
          singer: "梁静茹",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 25,
          songName: "彩虹",
          singer: "周杰伦",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 26,
          songName: "刺猬",
          singer: "孙依哲",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 27,
          songName: "天后",
          singer: "陈势安",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 28,
          songName: "趁早",
          singer: "张惠妹",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 29,
          songName: "超负荷",
          singer: "斯琴高丽",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 30,
          songName: "从前慢",
          singer: "刘胡轶",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 31,
          songName: "错的人",
          singer: "萧亚轩",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 32,
          songName: "创造101",
          singer: "火箭少女101",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 33,
          songName: "匆匆那年",
          singer: "王菲",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 34,
          songName: "纯阳雪",
          singer: "末路XXX",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 35,
          songName: "残酷月光",
          singer: "林宥嘉",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 36,
          songName: "此生与你，不过相逢",
          singer: "上古呐",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 37,
          songName: "电灯胆",
          singer: "邓丽欣",
          language: "粤语",
          initial: "D",
          remark: "",
        },
        {
          songID: 38,
          songName: "大鱼",
          singer: "周深",
          language: "国语",
          initial: "D",
          remark: "",
        },
        {
          songID: 39,
          songName: "大眠",
          singer: "王心凌",
          language: "国语",
          initial: "D",
          remark: "",
        },
        {
          songID: 40,
          songName: "兜圈",
          singer: "林宥嘉",
          language: "国语",
          initial: "D",
          remark: "",
        },
        {
          songID: 41,
          songName: "倒带",
          singer: "蔡依林",
          language: "国语",
          initial: "D",
          remark: "",
        },
        {
          songID: 42,
          songName: "带我走",
          singer: "杨丞琳",
          language: "国语",
          initial: "D",
          remark: "",
        },
        {
          songID: 43,
          songName: "单向箭头",
          singer: "双笙",
          language: "国语",
          initial: "D",
          remark: "",
        },
        {
          songID: 44,
          songName: "等你下课",
          singer: "周杰伦",
          language: "国语",
          initial: "D",
          remark: "",
        },
        {
          songID: 45,
          songName: "疯子",
          singer: "许哲佩",
          language: "国语",
          initial: "F",
          remark: "",
        },
        {
          songID: 46,
          songName: "拂雪",
          singer: "不才",
          language: "国语",
          initial: "F",
          remark: "",
        },
        {
          songID: 47,
          songName: "分身",
          singer: "单以纯",
          language: "国语",
          initial: "F",
          remark: "",
        },
        {
          songID: 48,
          songName: "发如雪",
          singer: "周杰伦",
          language: "国语",
          initial: "F",
          remark: "",
        },
        {
          songID: 49,
          songName: "分手快乐",
          singer: "梁静茹",
          language: "国语",
          initial: "F",
          remark: "",
        },
        {
          songID: 50,
          songName: "飞鸟和她",
          singer: "圈9&不才",
          language: "国语",
          initial: "F",
          remark: "",
        },
        {
          songID: 51,
          songName: "皈依",
          singer: "皈依小能手",
          language: "国语",
          initial: "G",
          remark: "",
        },
        {
          songID: 52,
          songName: "咖喱咖喱",
          singer: "给电影人的情书",
          language: "国语",
          initial: "G",
          remark: "",
        },
        {
          songID: 53,
          songName: "给我一个理由忘记",
          singer: "A-Lin",
          language: "国语",
          initial: "G",
          remark: "",
        },
        {
          songID: 54,
          songName: "搁浅",
          singer: "周杰伦",
          language: "国语",
          initial: "G",
          remark: "",
        },
        {
          songID: 55,
          songName: "呼吸决定",
          singer: "Fine乐团",
          language: "国语",
          initial: "H",
          remark: "",
        },
        {
          songID: 56,
          songName: "红豆",
          singer: "王菲",
          language: "国语",
          initial: "H",
          remark: "",
        },
        {
          songID: 57,
          songName: "画心",
          singer: "张靓颖",
          language: "国语",
          initial: "H",
          remark: "",
        },
        {
          songID: 58,
          songName: "后来",
          singer: "刘若英",
          language: "国语",
          initial: "H",
          remark: "",
        },
        {
          songID: 59,
          songName: "海底",
          singer: "一只榴莲",
          language: "国语",
          initial: "H",
          remark: "",
        },
        {
          songID: 60,
          songName: "红颜旧",
          singer: "刘涛",
          language: "国语",
          initial: "H",
          remark: "",
        },
        {
          songID: 61,
          songName: "黄昏晓",
          singer: "王心凌",
          language: "国语",
          initial: "H",
          remark: "",
        },
        {
          songID: 62,
          songName: "后会无期",
          singer: "王心凌",
          language: "国语",
          initial: "H",
          remark: "",
        },
        {
          songID: 63,
          songName: "会呼吸的痛",
          singer: "梁静茹",
          language: "国语",
          initial: "H",
          remark: "",
        },
        {
          songID: 64,
          songName: "化身孤岛的鲸",
          singer: "不才",
          language: "国语",
          initial: "H",
          remark: "",
        },
        {
          songID: 65,
          songName: "挥着翅膀的女孩",
          singer: "容祖儿",
          language: "国语",
          initial: "H",
          remark: "",
        },
        {
          songID: 66,
          songName: "记得",
          singer: "张惠妹",
          language: "国语",
          initial: "J",
          remark: "",
        },
        {
          songID: 67,
          songName: "剪爱",
          singer: "张惠妹",
          language: "国语",
          initial: "J",
          remark: "",
        },
        {
          songID: 68,
          songName: "矜持",
          singer: "王菲",
          language: "国语",
          initial: "J",
          remark: "",
        },
        {
          songID: 69,
          songName: "江南",
          singer: "林俊杰",
          language: "国语",
          initial: "J",
          remark: "",
        },
        {
          songID: 70,
          songName: "九张机",
          singer: "叶炫清",
          language: "国语",
          initial: "J",
          remark: "",
        },
        {
          songID: 71,
          songName: "锦鲤抄",
          singer: "云の泣&银临",
          language: "国语",
          initial: "J",
          remark: "",
        },
        {
          songID: 72,
          songName: "寂寞不痛",
          singer: "A-Lin",
          language: "国语",
          initial: "J",
          remark: "",
        },
        {
          songID: 73,
          songName: "街角的祝福",
          singer: "戴佩妮",
          language: "国语",
          initial: "J",
          remark: "",
        },
        {
          songID: 74,
          songName: "克卜勒",
          singer: "孙燕姿",
          language: "国语",
          initial: "K",
          remark: "",
        },
        {
          songID: 75,
          songName: "可念不可说",
          singer: "崔子格",
          language: "国语",
          initial: "K",
          remark: "",
        },
        {
          songID: 76,
          songName: "可惜没如果",
          singer: "林俊杰",
          language: "国语",
          initial: "K",
          remark: "",
        },
        {
          songID: 77,
          songName: "刻在我心底的名字",
          singer: "卢广仲",
          language: "国语",
          initial: "K",
          remark: "",
        },
        {
          songID: 78,
          songName: "空白格",
          singer: "蔡健雅",
          language: "国语",
          initial: "K",
          remark: "",
        },
        {
          songID: 79,
          songName: "快乐的旅行",
          singer: "自然卷乐团",
          language: "国语",
          initial: "K",
          remark: "",
        },
        {
          songID: 80,
          songName: "冷战",
          singer: "杨丞琳",
          language: "国语",
          initial: "L",
          remark: "",
        },
        {
          songID: 81,
          songName: "旅行的意义",
          singer: "陈绮贞",
          language: "国语",
          initial: "L",
          remark: "",
        },
        {
          songID: 82,
          songName: "流着泪说分手",
          singer: "苏立生",
          language: "国语",
          initial: "L",
          remark: "",
        },
        {
          songID: 83,
          songName: "恋爱困难少女",
          singer: "ChillChill",
          language: "国语",
          initial: "L",
          remark: "",
        },
        {
          songID: 84,
          songName: "迷迭香",
          singer: "周杰伦",
          language: "国语",
          initial: "M",
          remark: "",
        },
        {
          songID: 85,
          songName: "眉间雪",
          singer: "晴愔",
          language: "国语",
          initial: "M",
          remark: "",
        },
        {
          songID: 86,
          songName: "陌生人",
          singer: "蔡健雅",
          language: "国语",
          initial: "M",
          remark: "",
        },
        {
          songID: 87,
          songName: "梦里花",
          singer: "张韶涵",
          language: "国语",
          initial: "M",
          remark: "",
        },
        {
          songID: 88,
          songName: "慢慢喜欢你",
          singer: "莫文蔚",
          language: "国语",
          initial: "M",
          remark: "",
        },
        {
          songID: 89,
          songName: "美丽新世界",
          singer: "S.H.E",
          language: "国语",
          initial: "M",
          remark: "",
        },
        {
          songID: 90,
          songName: "宁夏",
          singer: "梁静茹",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 91,
          songName: "逆光",
          singer: "孙燕姿",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 92,
          songName: "年轮",
          singer: "张碧晨",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 93,
          songName: "南山南",
          singer: "马頔",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 94,
          songName: "年轮说",
          singer: "杨丞琳",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 95,
          songName: "你的甜蜜",
          singer: "范晓萱",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 96,
          songName: "年少有为",
          singer: "李荣浩",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 97,
          songName: "匿名的好友",
          singer: "杨丞琳",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 98,
          songName: "你给我听好",
          singer: "陈奕迅",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 99,
          songName: "你在终点等我",
          singer: "王菲",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 100,
          songName: "柠檬草的味道",
          singer: "蔡依林",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 101,
          songName: "你是我的风景",
          singer: "何洁",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 102,
          songName: "那年夏天宁静的夏",
          singer: "王心凌",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 103,
          songName: "你的微笑",
          singer: "F.I.R飞儿乐团",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 104,
          songName: "欧若拉",
          singer: "张韶涵",
          language: "国语",
          initial: "O",
          remark: "",
        },
        {
          songID: 105,
          songName: "泡沫",
          singer: "邓紫棋",
          language: "国语",
          initial: "P",
          remark: "",
        },
        {
          songID: 106,
          songName: "平凡的一天",
          singer: "毛不易",
          language: "国语",
          initial: "P",
          remark: "",
        },
        {
          songID: 107,
          songName: "漂洋过海来看你",
          singer: "金智娟（娃娃）",
          language: "国语",
          initial: "P",
          remark: "",
        },
        {
          songID: 108,
          songName: "晴天",
          singer: "周杰伦",
          language: "国语",
          initial: "Q",
          remark: "",
        },
        {
          songID: 109,
          songName: "情歌",
          singer: "梁静茹",
          language: "国语",
          initial: "Q",
          remark: "",
        },
        {
          songID: 110,
          songName: "棋子",
          singer: "王菲",
          language: "国语",
          initial: "Q",
          remark: "",
        },
        {
          songID: 111,
          songName: "琴师",
          singer: "音频怪物",
          language: "国语",
          initial: "Q",
          remark: "",
        },
        {
          songID: 112,
          songName: "庆祝",
          singer: "杨丞琳",
          language: "国语",
          initial: "Q",
          remark: "",
        },
        {
          songID: 113,
          songName: "青花瓷",
          singer: "周杰伦",
          language: "国语",
          initial: "Q",
          remark: "",
        },
        {
          songID: 114,
          songName: "牵丝戏",
          singer: "银临&Aki阿杰",
          language: "国语",
          initial: "Q",
          remark: "",
        },
        {
          songID: 115,
          songName: "恰雪来故",
          singer: "晴愔",
          language: "国语",
          initial: "Q",
          remark: "",
        },
        {
          songID: 116,
          songName: "绮梦夜谈",
          singer: "虫某人",
          language: "国语",
          initial: "Q",
          remark: "",
        },
        {
          songID: 117,
          songName: "亲密爱人",
          singer: "梅艳芳",
          language: "国语",
          initial: "Q",
          remark: "",
        },
        {
          songID: 118,
          songName: "奇妙能力歌",
          singer: "陈粒",
          language: "国语",
          initial: "Q",
          remark: "",
        },
        {
          songID: 119,
          songName: "如此",
          singer: "何佳乐",
          language: "国语",
          initial: "R",
          remark: "",
        },
        {
          songID: 120,
          songName: "入海",
          singer: "毛不易",
          language: "国语",
          initial: "R",
          remark: "",
        },
        {
          songID: 121,
          songName: "日不落",
          singer: "蔡依林",
          language: "国语",
          initial: "R",
          remark: "",
        },
        {
          songID: 122,
          songName: "如果没有你",
          singer: "莫文蔚",
          language: "国语",
          initial: "R",
          remark: "",
        },
        {
          songID: 123,
          songName: "如果有来生",
          singer: "谭维维",
          language: "国语",
          initial: "R",
          remark: "",
        },
        {
          songID: 124,
          songName: "树",
          singer: "许哲佩",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 125,
          songName: "傻子",
          singer: "林宥嘉",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 126,
          songName: "舍离断",
          singer: "何佳乐",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 127,
          songName: "说爱我",
          singer: "梁一贞",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 128,
          songName: "说爱你",
          singer: "蔡依林",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 129,
          songName: "岁月神偷",
          singer: "金玟岐",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 130,
          songName: "失落沙洲",
          singer: "徐佳莹",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 131,
          songName: "说散就散",
          singer: "JC陈永彤",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 132,
          songName: "身骑白马",
          singer: "徐佳莹",
          language: "闽语",
          initial: "S",
          remark: "",
        },
        {
          songID: 133,
          songName: "时间煮雨",
          singer: "郁可唯",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 134,
          songName: "山川挽歌",
          singer: "宠儿&Assen捷&Tacke竹桑",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 135,
          songName: "私奔到月球",
          singer: "五月天&陈绮贞",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 136,
          songName: "盛夏的果实",
          singer: "莫文蔚",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 137,
          songName: "十万毫升泪水",
          singer: "蔡健雅",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 138,
          songName: "她说",
          singer: "林俊杰",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 139,
          songName: "妥协",
          singer: "蔡依林",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 140,
          songName: "天黑黑",
          singer: "孙燕姿",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 141,
          songName: "同手同脚",
          singer: "温岚",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 142,
          songName: "兔子先生",
          singer: "洛天依",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 143,
          songName: "天天想你",
          singer: "张雨生",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 144,
          songName: "棠梨煎雪",
          singer: "Aki银临",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 145,
          songName: "突然好想你",
          singer: "五月天",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 146,
          songName: "他还是不懂",
          singer: "S.H.E",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 147,
          songName: "听见下雨的声音",
          singer: "魏如昀",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 148,
          songName: "我要你",
          singer: "任素汐",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 149,
          songName: "我怀念的",
          singer: "孙燕姿",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 150,
          songName: "我生我死",
          singer: "不才",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 151,
          songName: "我要快乐",
          singer: "张惠妹",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 152,
          songName: "无人之岛",
          singer: "任然",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 153,
          songName: "我最闪亮",
          singer: "黄星羱",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 154,
          songName: "完美情人",
          singer: "邓福如",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 155,
          songName: "我恨我爱你",
          singer: "张惠妹",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 156,
          songName: "危险派对",
          singer: "王以太&刘至佳",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 157,
          songName: "我真的受伤了",
          singer: "张学友",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 158,
          songName: "我要我们在一起",
          singer: "范晓萱",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 159,
          songName: "我知道你很难过",
          singer: "蔡依林",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 160,
          songName: "我知道",
          singer: "BY2",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 161,
          songName: "我的一个道姑朋友",
          singer: "LON",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 162,
          songName: "我的悲伤是水做的",
          singer: "洛天依",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 163,
          songName: "心动",
          singer: "陈洁仪",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 164,
          songName: "小半",
          singer: "陈粒",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 165,
          songName: "心墙",
          singer: "郭静",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 166,
          songName: "喜欢",
          singer: "阿肆",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 167,
          songName: "小幸运",
          singer: "田馥甄",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 168,
          songName: "喜欢你",
          singer: "陈洁仪",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 169,
          songName: "想自由",
          singer: "林宥嘉",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 170,
          songName: "喜帖街",
          singer: "谢安琪",
          language: "粤语",
          initial: "X",
          remark: "",
        },
        {
          songID: 171,
          songName: "小城大事",
          singer: "杨千嬅",
          language: "粤语",
          initial: "X",
          remark: "",
        },
        {
          songID: 172,
          songName: "香格里拉",
          singer: "魏如萱",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 173,
          songName: "下一个天亮",
          singer: "郭静",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 174,
          songName: "心愿便利贴",
          singer: "元若蓝&大Q秉洛",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 175,
          songName: "小小",
          singer: "容祖儿",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 176,
          songName: "雨爱",
          singer: "杨丞琳",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 177,
          songName: "鱼",
          singer: "陈绮贞",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 178,
          songName: "野子",
          singer: "苏运莹",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 179,
          songName: "也罢",
          singer: "鲁向卉",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 180,
          songName: "烟火",
          singer: "陈绮贞",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 181,
          songName: "仰望",
          singer: "杨丞琳",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 182,
          songName: "鱼仔",
          singer: "卢广仲",
          language: "闽语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 183,
          songName: "樱花草",
          singer: "Sweety",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 184,
          songName: "月牙湾",
          singer: "飞儿乐团",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 185,
          songName: "一眼万年",
          singer: "林俊杰",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 186,
          songName: "与你有关",
          singer: "泠鸢yousa",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 187,
          songName: "一直很安静",
          singer: "阿桑",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 188,
          songName: "易燃易爆炸",
          singer: "陈粒",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 189,
          songName: "有一种悲伤",
          singer: "A-Lin",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 190,
          songName: "一样的月光",
          singer: "徐佳莹",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 191,
          songName: "永不失联的爱",
          singer: "Eric周兴哲",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 192,
          songName: "越长大越孤单",
          singer: "牛奶咖啡",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 193,
          songName: "勇气",
          singer: "梁静茹",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 194,
          songName: "约定",
          singer: "王菲",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 195,
          songName: "一个像秋天一个像夏天",
          singer: "范玮琪",
          language: "国语",
          initial: "Y",
          remark: "",
        },
        {
          songID: 196,
          songName: "最长的电影",
          singer: "周杰伦",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 197,
          songName: "走马",
          singer: "陈粒",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 198,
          songName: "知足",
          singer: "五月天",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 200,
          songName: "左边",
          singer: "杨丞琳",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 201,
          songName: "指望",
          singer: "郁可唯",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 202,
          songName: "钟无艳",
          singer: "谢安琪",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 203,
          songName: "追光者",
          singer: "岑宁儿",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 204,
          songName: "至少还有你",
          singer: "林忆莲",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 205,
          songName: "朝花只拾一半",
          singer: "杨千嬅",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 206,
          songName: "致姗姗来迟的你",
          singer: "阿肆&林宥嘉",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 207,
          songName: "最熟悉的陌生人",
          singer: "萧亚轩",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 208,
          songName: "怎样",
          singer: "戴佩妮",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 209,
          songName: "Close To You",
          singer: "Carpenters",
          language: "英语",
          initial: "C",
          remark: "",
        },
        {
          songID: 210,
          songName: "群青",
          singer: "YOASOBI",
          language: "日语",
          initial: "Q",
          remark: "",
        },
        {
          songID: 211,
          songName: "糸",
          singer: "中岛美嘉 (なかしま みか)",
          language: "日语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 212,
          songName: "123木头人",
          singer: "黑Girl",
          language: "国语",
          initial: "M",
          remark: "",
        },
        {
          songID: 213,
          songName: "R&B All Night",
          singer: "knowknow&Higher Brothers",
          language: "国语",
          initial: "R",
          remark: "",
        },
        {
          songID: 214,
          songName: "Forever Young",
          singer: "艾怡良",
          language: "国语",
          initial: "F",
          remark: "",
        },
        {
          songID: 215,
          songName: "Fly me to the moon",
          singer: "Bart Howard",
          language: "英语",
          initial: "F",
          remark: "",
        },
        {
          songID: 216,
          songName: "I Love You 3000 Ⅱ",
          singer: "Stephanie Poetri&王嘉尔",
          language: "国语",
          initial: "I",
          remark: "",
        },
        {
          songID: 217,
          songName: "カタオモイ(单相思)",
          singer: "Aimer",
          language: "日语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 218,
          songName: "Heavenly Days",
          singer: "新垣结衣 (あらがき ゆい)",
          language: "日语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 219,
          songName: "离岛之歌",
          singer: "东山奈央 (とうやま なお)",
          language: "日语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 220,
          songName: "人生は夢だらけ",
          singer: "椎名林檎 (しいな りんご)",
          language: "日语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 222,
          songName: "やさしさの種子",
          singer: "岩男潤子 (いわお じゅんこ)",
          language: "日语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 223,
          songName: "なんでもないや（没什么大不了的）",
          singer: "RADWIMPS",
          language: "日语",
          initial: "JA",
          remark: "没什么大不了的",
        },
        {
          songID: 224,
          songName: "扉をあけて（打开心扉）",
          singer: "ANZA (大山アンザ)",
          language: "日语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 225,
          songName: "雪の華",
          singer: "中岛美嘉 (なかしま みか)",
          language: "日语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 226,
          songName: "SAKURA",
          singer: "生物股长 (いきものがかり)",
          language: "日语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 227,
          songName: "愛してる",
          singer: "高铃 (Callin')",
          language: "日语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 228,
          songName: "僕が死のうと思ったのは",
          singer: "中岛美嘉 (なかしま みか)",
          language: "日语",
          initial: "JA",
          remark: "曾经我也想过一了百了",
        },
        {
          songID: 229,
          songName: "また あした (明天见)",
          singer: "悠木碧 (ゆうき あおい)",
          language: "日语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 230,
          songName: "なきむし",
          singer: "沢井美空 (さわい みく)",
          language: "日语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 231,
          songName: "心做し",
          singer: "GUMI",
          language: "国语",
          initial: "JA",
          remark: "",
        },
        {
          songID: 232,
          songName: "离音",
          singer: "林孟璇",
          language: "国语",
          initial: "L",
          remark: "",
        },
        {
          songID: 233,
          songName: "靠近",
          singer: "罗震环",
          language: "国语",
          initial: "K",
          remark: "",
        },
        {
          songID: 234,
          songName: "嘉宾",
          singer: "张远",
          language: "国语",
          initial: "J",
          remark: "",
        },
        {
          songID: 235,
          songName: "老伴",
          singer: "李荣浩",
          language: "国语",
          initial: "L",
          remark: "",
        },
        {
          songID: 236,
          songName: "台风",
          singer: "叶文辉",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 237,
          songName: "当你",
          singer: "王心凌",
          language: "国语",
          initial: "D",
          remark: "",
        },
        {
          songID: 238,
          songName: "十年",
          singer: "陈奕迅",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 239,
          songName: "晚婚",
          singer: "江蕙",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 240,
          songName: "天后",
          singer: "陈势安",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 241,
          songName: "不该",
          singer: "周杰伦&张惠妹",
          language: "国语",
          initial: "B",
          remark: "",
        },
        {
          songID: 242,
          songName: "菊花台",
          singer: "周杰伦",
          language: "国语",
          initial: "J",
          remark: "",
        },
        {
          songID: 243,
          songName: "笑忘书",
          singer: "王菲",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 244,
          songName: "我愿意",
          singer: "王菲",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 245,
          songName: "我不配",
          singer: "周杰伦",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 246,
          songName: "热气球",
          singer: "黄淑惠",
          language: "国语",
          initial: "R",
          remark: "",
        },
        {
          songID: 247,
          songName: "猜不透",
          singer: "丁当",
          language: "国语",
          initial: "C",
          remark: "",
        },
        {
          songID: 248,
          songName: "我爱他",
          singer: "丁当",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 249,
          songName: "甜蜜蜜",
          singer: "邓丽君",
          language: "国语",
          initial: "T",
          remark: "",
        },
        {
          songID: 250,
          songName: "连名带姓",
          singer: "张惠妹",
          language: "国语",
          initial: "L",
          remark: "",
        },
        {
          songID: 251,
          songName: "南海姑娘",
          singer: "邓丽君",
          language: "国语",
          initial: "N",
          remark: "",
        },
        {
          songID: 252,
          songName: "爱的天国",
          singer: "王心凌",
          language: "国语",
          initial: "A",
          remark: "",
        },
        {
          songID: 253,
          songName: "夏天的风",
          singer: "温岚",
          language: "国语",
          initial: "X",
          remark: "",
        },
        {
          songID: 254,
          songName: "爱情转移",
          singer: "陈奕迅",
          language: "国语",
          initial: "A",
          remark: "《富士山下》国语版",
        },
        {
          songID: 255,
          songName: "孤岛星愿",
          singer: "陈子晴",
          language: "国语",
          initial: "G",
          remark: "",
        },
        {
          songID: 256,
          songName: "昨日青空",
          singer: "尤长靖",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 257,
          songName: "第二杯半价",
          singer: "纳豆nado",
          language: "国语",
          initial: "D",
          remark: "",
        },
        {
          songID: 258,
          songName: "不完美小孩",
          singer: "TFBOYS",
          language: "国语",
          initial: "B",
          remark: "",
        },
        {
          songID: 259,
          songName: "当时的月亮",
          singer: "王菲",
          language: "国语",
          initial: "D",
          remark: "",
        },
        {
          songID: 260,
          songName: "爱的华尔兹",
          singer: "严艺丹",
          language: "国语",
          initial: "A",
          remark: "",
        },
        {
          songID: 261,
          songName: "没那么简单",
          singer: "黄小琥",
          language: "国语",
          initial: "M",
          remark: "",
        },
        {
          songID: 262,
          songName: "说好的幸福呢",
          singer: "周杰伦",
          language: "国语",
          initial: "S",
          remark: "",
        },
        {
          songID: 263,
          songName: "当爱已成往事",
          singer: "林忆莲&李宗盛",
          language: "国语",
          initial: "D",
          remark: "",
        },
        {
          songID: 264,
          songName: "给电影人的情书",
          singer: "蔡琴",
          language: "国语",
          initial: "G",
          remark: "",
        },
        {
          songID: 265,
          songName: "这世界那么多人",
          singer: "莫文蔚",
          language: "国语",
          initial: "Z",
          remark: "",
        },
        {
          songID: 266,
          songName: "我用什么把你留住",
          singer: "福禄寿FloruitShow",
          language: "国语",
          initial: "W",
          remark: "",
        },
        {
          songID: 267,
          songName: "燕尾蝶",
          singer: "梁静茹",
          language: "国语",
          initial: "Y",
          remark: "",
        },
      ],
      options: [
        { value: 1, label: "全部" },
        { value: 2, label: "A" },
        { value: 3, label: "B" },
        { value: 4, label: "C" },
        { value: 5, label: "D" },
        { value: 6, label: "E" },
        { value: 7, label: "F" },
        { value: 8, label: "G" },
        { value: 9, label: "H" },
        { value: 10, label: "I" },
        { value: 11, label: "J" },
        { value: 12, label: "K" },
        { value: 13, label: "L" },
        { value: 14, label: "M" },
        { value: 15, label: "N" },
        { value: 16, label: "O" },
        { value: 17, label: "P" },
        { value: 18, label: "Q" },
        { value: 19, label: "R" },
        { value: 20, label: "S" },
        { value: 21, label: "T" },
        { value: 22, label: "U" },
        { value: 23, label: "V" },
        { value: 24, label: "W" },
        { value: 25, label: "X" },
        { value: 26, label: "Y" },
        { value: 27, label: "Z" },
        { value: 28, label: "其他语言" },
      ],
      value: "",
    };
  },
  methods: {
    handle(row, event, column) {
      this.message = "点歌 " + row.songName;
      this.$copyText(this.message);
      const h = this.$createElement;
      this.$notify({
        title: "复制成功",
        message: h(
          "i",
          { style: "color: teal" },
          "成功复制" +
            "“" +
            row.songName +
            "”" +
            "到剪切板，快戴上五级牌子到直播间点歌吧！"
        ),
      });
    },
    OnClick(num) {
      this.keyword = "";
      this.value = "";
      if (num === 1) {
        this.searchList = this.totalList.filter((p) => {
          return p.language == "国语";
        });
      } else if (num === 2) {
        this.searchList = this.totalList.filter((p) => {
          return p.language == "英语";
        });
      } else if (num === 3) {
        this.searchList = this.totalList.filter((p) => {
          return p.language == "粤语";
        });
      } else if (num === 4) {
        this.searchList = this.totalList.filter((p) => {
          return p.language == "日语";
        });
      } else if (num === 5) {
        this.searchList = this.totalList.filter((p) => {
          return p.language == "闽语";
        });
      } else {
        this.searchList = this.totalList;
      }
    },
  },
  watch: {
    keyword: {
      handler(val) {
        this.searchList = this.totalList.filter((p) => {
          return p.songName.indexOf(val) != -1 || p.singer.indexOf(val) != -1;
        });
      },
      immediate: true,
    },
    value: {
      handler(val) {
        this.searchList = this.totalList.filter((p) => {
          return (
            p.songName.indexOf(this.keyword) != -1 ||
            p.singer.indexOf(this.keyword) != -1
          );
        });
        if (val === 1) {
          this.searchList = this.searchList;
        } else if (val === 2) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "A";
          });
        } else if (val === 3) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "B";
          });
        } else if (val === 4) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "C";
          });
        } else if (val === 5) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "D";
          });
        } else if (val === 6) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "E";
          });
        } else if (val === 7) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "F";
          });
        } else if (val === 8) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "G";
          });
        } else if (val === 9) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "H";
          });
        } else if (val === 10) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "I";
          });
        } else if (val === 11) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "J";
          });
        } else if (val === 12) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "K";
          });
        } else if (val === 13) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "L";
          });
        } else if (val === 14) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "M";
          });
        } else if (val === 15) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "N";
          });
        } else if (val === 16) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "O";
          });
        } else if (val === 17) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "P";
          });
        } else if (val === 18) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "Q";
          });
        } else if (val === 19) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "R";
          });
        } else if (val === 20) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "S";
          });
        } else if (val === 21) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "T";
          });
        } else if (val === 22) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "U";
          });
        } else if (val === 23) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "V";
          });
        } else if (val === 24) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "W";
          });
        } else if (val === 25) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "X";
          });
        } else if (val === 26) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "Y";
          });
        } else if (val === 27) {
          this.searchList = this.searchList.filter((p) => {
            return p.initial == "Z";
          });
        } else if (val === 28) {
          this.searchList = this.searchList.filter((p) => {
            return p.language == "日语" || p.language == "英语";
          });
        } else {
          this.searchList = this.searchList;
        }
      },
    },
  },
};
</script>

<style >
#app {
  font-family: Georgia, Arial, sans-serif;
}
.el-avatar el-avatar--circle {
  margin: 0 auto;
}
/* 背景 */
#page {
  background-color: rgb(185, 246, 225);
  min-height: 2000px;
  margin: 0;
}
#header {
  text-align: center;
  margin-top: 20px;
}
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

#b1 {
  width: 100%;
  background-color: rgb(198, 229, 194);
}
#s1 {
  width: 100%;
}

#div0 {
  height: 150px;
  width: 60%;
  margin: 0 auto;
  margin-top: 40px;
}

#div0 div {
  float: left;
  height: 40px;
}
#block {
  margin: 0 auto;
}
/* 1行三个div */
@media screen and (min-device-width: 400px) {
  #div0 div {
    width: 33.3%;
  }

  #div0 div:nth-child(1) {
  }

  #div0 div:nth-child(2) {
  }

  #div0 div:nth-child(3) {
  }
}

/* 2行三个div */
@media screen and (min-device-width: 300px) and (max-device-width: 399px) {
  #div0 div {
    width: 50%;
  }

  #div0 div:nth-child(1) {
  }

  #div0 div:nth-child(2) {
  }

  #div0 div:nth-child(3) {
  }
}

/* 3行三个div */
@media screen and (min-device-width: 200px) and (max-device-width: 299px) {
  #div0 div {
    width: 100%;
  }

  #div0 div:nth-child(1) {
  }

  #div0 div:nth-child(2) {
  }

  #div0 div:nth-child(3) {
  }
}
</style>
