<script setup>
import {onMounted, reactive, ref} from "vue";
import axios from "axios";

let carousel = ref(null);
let tours = reactive([]);
let coverImages = ref([]);
const fetchLocationData = async () => {
    try {
        const response = await axios.get("items.json");
        // 将每行 JSON 对象拼接成一个数组
        const jsonArray = response.data.trim().split('\n');
        // 解析整个数组
        tours.value = jsonArray.map(jsonString => JSON.parse(jsonString));
        // 使用 for 循环将数据写入 coverImages 数组
        for (let i = 0; i < 10; i++) {
            console.log("Processing data at index", i, ":", tours.value[i]);
            coverImages.value.push({
                id: tours.value[i].id,
                pic: tours.value[i].cover_image,
                label: tours.value[i].display_name,
                url: tours.value[i].url
            });
        }
        console.log("Cover Images:", coverImages.value);
    } catch (error) {
        console.error("Error fetching location data:", error);
    }
};

onMounted(() => {
    fetchLocationData();
    console.log("Carousel:", carousel.value);
    console.log("Cover Images:", coverImages.value);
});
</script>

<template>
    <div class="main">
        <br>
        <el-carousel
            ref="carousel"
            class="carousel-first"
            trigger="hover"
            :interval="3000"
            height="35rem"
            type="card"
            arrow="always"
        >
            <el-carousel-item
                :label="coverImages.label"
                class="item"
                v-for="(i,index) in coverImages"
                :key="index">
                <a :href="i.url" target="_blank">
                    <el-image class="img" :src="i.pic" alt="概览"></el-image>
                </a>
            </el-carousel-item>
        </el-carousel>
    </div>
</template>

<style lang="less" scoped>
/deep/ .el-carousel__item {
  left: 6%;
}

/deep/ .el-carousel__button {
  background-color: #545c64;
  border-radius: 5px;
  color: #ffffff;
}

.main {
  width: 100%;
}

.item {
  width: 25rem;
  height: 100%;
  margin: 0 auto;

  .img {
    width: 100%;
    height: 80%;
    border-radius: 5px;
  }
}

@media screen and (max-width: 400px) {
  /deep/ .el-carousel__item {
    left: -14%;
  }
}

/* 响应式布局 - 当屏幕小于 600 像素宽时，用默认走马灯样式展示 */
@media screen and (min-width: 400px) and (max-width: 600px) {
  /deep/ .el-carousel__item {
    left: -9%;

  }
}

/* 响应式布局 - 当屏幕大于600像素 小于 3000像素 宽时，用card走马灯样式展示 */
@media screen and (min-width: 600px) and (max-width: 3000px) {
  /deep/ .el-carousel__item {
    left: 6%;
  }
}
</style>