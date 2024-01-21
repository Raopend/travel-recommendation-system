<script setup>
import {onMounted, reactive, ref} from "vue";
import axios from "axios";

let landscapes = reactive([]);
let coverImages = ref([]);
const fetchLocationData = async () => {
    try {
        const response = await axios.get("top_20_locations.json");
        const jsonArray = response.data.trim().split('\n');
        landscapes.value = jsonArray.map(jsonString => JSON.parse(jsonString));

        for (let i = 0; i < 20; i++) {
            coverImages.value.push({
                id: landscapes.value[i].id,
                pic: landscapes.value[i].cover_image,
                label: landscapes.value[i].display_name,
                url: landscapes.value[i].url
            });
        }
    } catch (error) {
        console.error("Error fetching location data:", error);
    }
};
onMounted(() => {
    fetchLocationData();
});
</script>

<template>
    <div class="center-container">
        <div class="landscape-carousel">
            <div class="carousel-title">
                <img src="@/assets/star.jfif" alt="Icon" class="title-icon"/>
                最多人去
            </div>
            <div class="card-container">
                <div v-for="(coverImage, index) in coverImages" :key="index" class="landscape-card">
                    <a :href="coverImage.url" target="_blank">
                        <img :src="coverImage.pic" alt="Landscape Image"/>
                    </a>
                    <div class="landscape-label">{{ coverImage.label }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.landscape-carousel {
    width: 80%;
    margin: auto;
}

.carousel-title {
    font-size: 24px;
    color: #e52a0d;
    font-weight: bold;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
}

.title-icon {
    width: 24px;
    height: 24px;
    margin-right: 8px;
}

.card-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px; /* 间隔调整，可以根据需要调整 */
    justify-content: space-between;
}

.landscape-card {
    width: 22%; /* 调整卡片宽度 */
    height: 300px; /* 调整卡片高度 */
    margin-bottom: 1rem;
    position: relative;
}

img {
    width: 100%;
    height: 100%; /* 图片高度设置为100%填充卡片 */
    object-fit: cover; /* 图片保持比例，覆盖整个容器 */
}

.landscape-label {
    position: absolute;
    bottom: 10%;
    left: 50%;
    transform: translateX(-50%);
    font-size: 18px;
    color: #fff;
    font-weight: bold;
}

.center-container {
    margin: auto;
    text-align: center;
}
</style>