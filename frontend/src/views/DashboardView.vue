<script setup>

</script>
<template>
  <div class="classification-master">
    <br>
  <el-row class="flex-container">
    <el-col
        v-for="(o, index) in 1"
        :key="o"
        :span="15"
        :offset="index > 0 ? 2 : 0"
    >
<!--      <object data="../../graph/top20_reviews_count_bar_chart.html" type="text/html" width="600" height="400"></object>-->
      <iframe src="@/assets/top20_reviews_count_bar_chart.html"
              width="1100" height="600"
              frameborder="0"
              style="overflow: hidden; display: block;"/>

    </el-col>
    <el-col :span="5" style="margin-left: 160px" class="content-column">
      <div class="centered-content">最热门景点</div>
    </el-col>
  </el-row>

    <br>
    <el-row class="flex-container">
      <el-col :span="3" style="margin-left: 50px; margin-right: 20px" class="content-column">
        <div class="centered-content">大众热爱旅行去向</div>
      </el-col>
      <el-col
          v-for="(o, index) in 1"
          :key="o"
          :span="10"
          :offset="index > 0 ? 2 : 0"
      >
        <iframe src="../../graph/wordcloud.html"
                width="1000" height="600"
                frameborder="0"
                style="overflow: hidden; display: block;"/>

      </el-col>

      <br>
      <el-row class="flex-container">
        <el-col
            v-for="(o, index) in 1"
            :key="o"
            :span="15"
            :offset="index > 0 ? 2 : 0"
        >
          <iframe src="../../graph/pie_chart.html"
                  width="1100" height="600"
                  frameborder="0"
                  style="overflow: hidden; display: block;"/>

        </el-col>
        <el-col :span="5" style="margin-left: 160px" class="content-column">
          <div class="centered-content">热门旅游城市</div>
        </el-col>
      </el-row>
    </el-row>
  </div>
</template>

<style scoped>
.classification-master {
  padding-left: 1%;
  padding-right: 1%;
}

.flex-container{
  display: flex;
}
@media screen and (max-width: 1200px) {
  .classification-master {
    padding-left: 0;
    padding-right: 0;
  }
}

@media screen and (min-width: 1200px) and (max-width: 1400px) {
  .classification-master {
    padding-left: 10%;
    padding-right: 10%;
  }
}
.content-column {
  display: flex;
  align-items: center; /* 垂直居中 */
}
.centered-content {
  text-align: center;
  font-size: 35px;
}
iframe{
  overflow: hidden;
  display: block;
}
</style>