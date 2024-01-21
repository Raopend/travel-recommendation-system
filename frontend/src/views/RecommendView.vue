<script setup>
import {reactive, ref} from "vue";
import recommendationRequest from "@/api/recommendation.js";
let tours = reactive([]);
let coverImages = ref([]);

const redirectToLink = (url) => {
    window.open(url, "_blank");
};
const userInfoJSON = localStorage.getItem('userInfo');

// 将 JSON 字符串解析为 JavaScript 对象
const userInfo = JSON.parse(userInfoJSON);
console.log(userInfo);
recommendationRequest.getRecommendedLandscapesByUserId(userInfo.id).then(res => {
    if (res.code === 200) {
        tours = res.data;
        for (let i = 0; i < tours.length; i++) {
            coverImages.value.push({
                id: tours[i].id,
                pic: tours[i].cover_image,
                display_name: tours[i].display_name,
                review_rating: tours[i].review_rating,
                address: tours[i].address,
                feature_reviews: tours[i].feature_reviews,
                url: tours[i].url
            });
        }
    }
});
</script>

<template>
    <div class="center-container">
        <br>
        <el-row>
            <el-col
                v-for="(o, index) in 1"
                :key="o"
                :span="15"
                :offset="index > 0 ? 2 : 0"
            >
                <el-card>
                    <div v-for="(i, index) in coverImages" :key="index" class="landscape-card">
                        <img :src="i.pic"
                             class="image"
                             alt=""/>
                        <div style="padding: 14px">
                            <span
                                style="color: black; font-size: 1.2em;"> {{ i.display_name }}&nbsp;&nbsp;&nbsp;&nbsp;</span>
                            <span style="color: red; font-size:1em;">评分：{{ i.review_rating }}</span>
                            <br>
                            <span>({{ i.address }})</span>
                            <div class="reviews">
                                {{ i.feature_reviews }}
                            </div>
                            <div class="bottom">
                                <!--            <time class="time">{{ currentDate }}</time>-->
                                <el-button text class="button" @click="redirectToLink(i.url)">
                                    放大查看
                                </el-button>
                            </div>
                        </div>
                    </div>
                </el-card>
            </el-col>
            <!-- 在右侧添加一个图片 -->
            <el-col :span="6" style="margin-left: 80px;">
                <img src="@/assets/recommendation_1.png" alt="" style="width: 100%; height: auto;">
            </el-col>
        </el-row>
    </div>
</template>

<style scoped>
.bottom {
    margin-top: 13px;
    line-height: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.button {
    padding: 0;
    min-height: auto;
}

.image {
    width: 70%;
    display: block;
    margin: 0 auto;
}

.reviews {
    font-size: 0.8em;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.center-container {
    margin: auto;
    text-align: center;
}
</style>